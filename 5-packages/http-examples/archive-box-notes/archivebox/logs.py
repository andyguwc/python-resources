# deal with logging 

import sys
from datetime import datetime
from config import ANSI, REPO_DIR, OUTPUT_DIR


# globals are bad, mmkay
_LAST_RUN_STATS = {
    'skipped': 0,
    'succeeded': 0,
    'failed': 0,

    'parsing_start_ts': 0,
    'parsing_end_ts': 0,

    'indexing_start_ts': 0,
    'indexing_end_ts': 0,

    'archiving_start_ts': 0,
    'archiving_end_ts': 0,

    'links': {},
}

def pretty_path(path):
    """convert paths like .../ArchiveBox/archivebox/../output/abc into output/abc"""
    return path.replace(REPO_DIR + '/', '')


def log_parsing_started(source_file):
    start_ts = datetime.now()
    _LAST_RUN_STATS['parse_start_ts'] = start_ts
    print('{green}[*] [{}] Parsing new links from output/sources/{}...{reset}'.format(
        start_ts.strftime('%Y-%m-%d %H:%M:%S'),
        source_file.rsplit('/', 1)[-1],
        **ANSI,
    ))


def log_parsing_finished(num_new_links, parser_name):
    print('    > Adding {} new links to index (parsed import as {})'.format(
        num_new_links,
        parser_name,
    ))