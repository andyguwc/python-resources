# https://github.com/pirate/ArchiveBox/blob/master/archivebox/util.py
import os 
import re 
import sys 
import time 

from urllib.request import Request, urlopen
from urllib.parse import urlparse, quote
from decimal import Decimal
from datetime import datetime

from config import (
    SOURCES_DIR,
    ARCHIVE_DIR,
)

from logs import pretty_path

try:
    import chardet
    detect_encoding = lambda rawdata: chardet.detect(rawdata)["encoding"]
except ImportError:
    detect_encoding = lambda rawdata: "utf-8"

# make sure it's URL format
URL_REGEX = re.compile(
    r'http[s]?://'                    # start matching from allowed schemes
    r'(?:[a-zA-Z]|[0-9]'              # followed by allowed alphanum characters
    r'|[$-_@.&+]|[!*\(\),]'           #    or allowed symbols
    r'|(?:%[0-9a-fA-F][0-9a-fA-F]))'  #    or allowed unicode bytes (?:) matches whatever regular expression inside the parentheses
    r'[^\]\[\(\)<>\""\'\s]+',         # stop parsing at these symbols
    re.IGNORECASE,
)


def save_stdin_source(raw_text):
    if not os.path.exists(SOURCES_DIR):
        os.makedirs(SOURCES_DIR)
    
    ts = str(datetime.now().timestamp()).split('.',1)[0]

    source_path = os.path.join(SOURCES_DIR, '{}-{}.txt'.format('stdin', ts))

    with open(source_path, 'w', encoding='utf-8') as f: 
        f.write(raw_text)
    
    return source_path 


# show progressed download 
def save_remote_source(url, timeout=TIMEOUT):
    """download a given url's content into output/sources/domain-<timestamp>.txt"""

    if not os.path.exists(SOURCES_DIR):
        os.makedirs(SOURCES_DIR)

    ts = str(datetime.now().timestamp()).split('.', 1)[0]

    source_path = os.path.join(SOURCES_DIR, '{}-{}.txt'.format(domain(url), ts))

    print('{}[*] [{}] Downloading {}{}'.format(
        ANSI['green'],
        datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        url,
        ANSI['reset'],
    ))
    timer = TimedProgress(timeout, prefix='      ')
    try:
        downloaded_xml = download_url(url, timeout=timeout)
        timer.end()
    except Exception as e:
        timer.end()
        print('{}[!] Failed to download {}{}\n'.format(
            ANSI['red'],
            url,
            ANSI['reset'],
        ))
        print('    ', e)
        raise SystemExit(1)

    with open(source_path, 'w', encoding='utf-8') as f:
        f.write(downloaded_xml)

    print('    > {}'.format(pretty_path(source_path)))

    return source_path


# using the Request package to download url 
def download_url(url, timeout=TIMEOUT):
    """Download the contents of a remote url and return the text"""

    req = Request(url, headers={'User-Agent': WGET_USER_AGENT})

    if CHECK_SSL_VALIDITY:
        resp = urlopen(req, timeout=timeout)
    else:
        import ssl 
        insecure = ssl._create_unverified_context()
        resp = urlopen(req, timeout=timeout, context=insecure)
    
    rawdata = resp.read()
    encoding = resp.headers.get_content_charset() or detect_encoding(rawdata)
    return rawdata.decode(encoding)


# using assert to check data structure 
# customized assert error messages 

def check_link_structure(link):
    """check data is valid"""
    assert isinstance(link, dict)
    assert isinstance(link.get('url'), str)
    assert len(link['url']) > 2 
    assert len(re.findall(URL_REGEX, link['url'])) == 1 # using URL_REGEX
    if 'history' in link:
        assert isinstance(link['history'], dict), 'history must be a Dict'
        for key, val in link['history'].items():
            assert isinstance(key, str)
            assert isinstance(val, list), 'history must be a Dict[str, List], got: {}'.format(link['history'])

def check_links_structure(links):
    """make sure data is valid"""
    assert isinstance(links, list)
    if links:
        check_link_structure(links[0])

# import function to change file mode type
def chmod_file(path, cwd='.', permissions=OUTPUT_PERMISSIONS, timeout=30):
    # OUTPUT_PERMISSIONS = os.getenv('OUTPUT_PERMISSIONS','755')
    """chmod -R <permissions> <cwd>/<path>"""

    if not os.path.exists(os.path.join(cwd, path)):
        raise Exception('Failed to chmod: {} does not exist (did the previous step fail?)'.format(path))
    
    chmod_result = run(['chmod', '-R', permissions, path], cwd=cwd, stdout=DEVNULL, stderr=PIPE, timeout=timeout)

    if chmod_result.returncode == 1:
        print('     ', chmod_result.stderr.decode())
        raise Exception('Failed to chmod {}/{}'.format(cwd, path))


# subprocess.run 
def run(*popenargs, input=None, capture_output=False, timeout=None, check=False, **kwargs):
    """Patched of subprocess.run to fix blocking io making timeout=innefective"""

    if input is not None:
        if 'stdin' in kwargs:
            raise ValueError('stdin and input arguments may not both be used.')
        kwargs['stdin'] = PIPE

    if capture_output:
        if ('stdout' in kwargs) or ('stderr' in kwargs):
            raise ValueError('stdout and stderr arguments may not be used '
                             'with capture_output.')
        kwargs['stdout'] = PIPE
        kwargs['stderr'] = PIPE

    with Popen(*popenargs, **kwargs) as process:
        try:
            stdout, stderr = process.communicate(input, timeout=timeout)
        except TimeoutExpired:
            process.kill()
            try:
                stdout, stderr = process.communicate(input, timeout=2)
            except:
                pass
            raise TimeoutExpired(popenargs[0][0], timeout)
        except BaseException:
            process.kill()
            # We don't call process.wait() as .__exit__ does that for us.
            raise 
        retcode = process.poll()
        if check and retcode:
            raise CalledProcessError(retcode, process.args,
                                     output=stdout, stderr=stderr)
    return CompletedProcess(process.args, retcode, stdout, stderr)