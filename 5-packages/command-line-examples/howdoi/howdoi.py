# https://github.com/gleitz/howdoi/blob/master/howdoi/howdoi.py#L68

import argparse
import os 
import sys 
import requests 

from requests.exceptions import ConnectionError, SSLError
from cachelib import FileSystemCache, NullCache
from pyquery import PyQuery as pq

'''
set up url arguments and headers 
'''
# based on SSL, use http or https
if os.getenv('HOWDOI_DISABLE_SSL'):
    SCHEME = 'http://'
    VERIFY_SSL_CERTIFICATE = False
else:
    SCHEME = 'https://'
    VERIFY_SSL_CERTIFICATE = True

SUPPORTED_SEARCH_ENGINES = ('google', 'bing', 'duckduckgo')
URL = os.getenv('HOWDOI_URL') or 'stackoverflow.com'

# search URLs
SEARCH_URLS = {
    'bing': SCHEME + 'www.bing.com/search?q=site:{0}%20{1}&hl=en',
    'google': SCHEME + 'www.google.com/search?q=site:{0}%20{1}&hl=en',
    'duckduckgo': SCHEME + 'duckduckgo.com/?q=site:{0}%20{1}&t=hj&ia=web'
}


'''
set up cache
'''

# Set up cache 
CACHE_EMPTY_VAL = "NULL"
CACHE_DIR = appdirs.use_cache_dir('howdoi')
CACHE_ENTRY_MAX = 128

if os.getenv('HOWDOI_DISABLE_CACHE'):
    cache = NullCache()
else:
    cache = FileSystemCache(CACHE_DIR, CACHE_ENTRY_MAX, default_timeout=0)


# start a session
howdoi_session = requests.session()


'''
get data
'''
# result proxies 
def get_result(url):
    try:
        # here we can customize proxies and certificates 
        return howdoi_session.get(url).text 
    
    # catch SSL exceptions
    except requests.exceptions.SSLError as e:
        _print_err('Encountered an SSL Error. Try using HTTP instead of '
                   'HTTPS by setting the environment variable "HOWDOI_DISABLE_SSL".\n')
        raise e


def get_answer(args, links):
    link = get_link_at_pos(links, args['pos'])
    if not link:
        return False 
    if args.get('link'):
        return link 
    
    # cache the pages 
    cache_key = link 
    page = cache.get(link)
    if not page:
        page = get_result(link + '?answertab=votes')
        cache.set(cache_key, page)
    
    # using pyquery to parse the html
    html = pq(page)
    first_answer = html('.answer').eq(0)

    instructions = first_answer.find('pre') or first_answer.find('code')
    args['tags'] = [t.text for t in html('.post-tag')]

    if not instructions and not args['all']:
        text = get_text(first_answer.find('.pos_text').eq(0))

    elif args['all']:
        texts = []
        for html_tag in first_answer.items('.post-text > *'):
            current_text = get_text(html_tag)
            if current_text:
                if html_tag[0].tag in ['pre', 'code']:
                    texts.append(_format_output(current_text, args))
                else:
                    texts.append(current_text)
        text = '\n'.join(texts)
    else:
        text = _format_output(get_text(instructions.eq(0)), args)
    if text is None:
        text = NO_ANSWER_MSG
    text = text.strip()
    return text

# look up the cache first
# if not there trigger the get_instructions 
def howdoi(args):
    args['query'] = ' '.join(args['query']).replace('?','')
    # enable result caching 
    cache_key = str(args)
    res = cache.get(cache_key)
    if res:
        return res 
    
    # when call things related to http connection, use the try
    try:
        res = get_instructions(args)
        if not res:
            res = 'Sorry, coudn\'t find any help with that topic\n'
        cache.set(cache_key, res)
        return res

    except (ConnectionError, SSLError):
        return 'Failed to establish connection\n'

'''
parser 
'''
def get_parser():
    parser = argparse.ArgumentParser(description='instant coding answers via command line')
    # metavar helps replace the name in help messages 
    # this main argument means if I run $python3 howdoi test this question, then args['query'] = ['test', 'this', 'question']
    parser.add_argument('query', metavar='QUERY', type=str, nargs='*', help='the question to answer')
    parser.add_argument('-p', '--pos', help='select answer in specified position (default: 1)', default=1, type=int)
    # binary variable, store the variable as true 
    parser.add_argument('-a', '--all', help='display the full text of the answer', action='store_true')
    parser.add_argument('-l', '--link', help='display only the answer link',
                        action='store_true')
    parser.add_argument('-c', '--color', help='enable colorized output',
                        action='store_true')
    parser.add_argument('-n', '--num-answers', help='number of answers to return', default=1, type=int)
    parser.add_argument('-C', '--clear-cache', help='clear the cache',
                        action='store_true')
    parser.add_argument('-v', '--version', help='displays the current version of howdoi',
                        action='store_true')
    # overwrite the existing args with dest later we can use args['search_engine'] to overwrite
    parser.add_argument('-e', '--engine', help='change search engine for this query only (google, bing, duckduckgo)',
                        dest='search_engine', nargs="?", default='google')    
    return parser 


'''
command line 
'''
def command_line_runner():
    parser = get_parser()
    args = vars(parser.parse_args())

    if args['clear_cache']:
        if _clear_cache():
            print('Cache cleared successfully')
        else:
            print('Clearing cache failed')
        return 

    # if args not there print help
    if not args['query']:
        parser.print_help()
    
    # args has both the parsed args and the env variables now
    if os.getenv('HOWDOI_COLORIZE'):
        args['color'] = True 
    
    if not args['search_engine'] in SUPPORTED_SEARCH_ENGINES:
        print('unsupported engine. Supported engines are: %s' % ', '.join(SUPPORTED_SEARCH_ENGINES))
        return 

    # overwrite env variables 
    elif args['search_engine'] != 'google':
        os.environ['HOWDOI_SEARCH_ENGINE'] = args['search_engine']
    
    # print out results
    utf8_result = howdoi(args).encode('utf-8', 'ignore')
    if sys.version < '3':
        print(utf8_result)
    else:
        # write out the content
        sys.stdout.buffer.write(utf8_result)
    # close the sesssion to release connection
    howdoi_session.close()


if __name__ == '__main__':
    command_line_runner()
    # parser = get_parser()
    # args=vars(parser.parse_args())  # this makes sure args is a dictionary
    # print(args['all'])
    # print(type(args['pos']))
    # print(args['query'])
    # print(args)