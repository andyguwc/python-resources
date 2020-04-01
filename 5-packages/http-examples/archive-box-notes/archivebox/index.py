# deal with reading and writing to indexes

import os
import json

from datetime import datetime
from string import Template
try:
    from distutils.dir_util import copy_tree
except ImportError:
    print('[X] Missing "distutils" python package. To install it, run:')
    print('    pip install distutils')

from config import (
    OUTPUT_DIR,
    TEMPLATES_DIR,
    GIT_SHA,
    FOOTER_INFO,
)
from util import (
    chmod_file,
    urlencode,
    derived_link_info,
    check_link_structure,
    check_links_structure,
    wget_output_path,
    latest_output,
)
from parse import parse_links
from links import validate_links
from logs import (
    log_indexing_process_started,
    log_indexing_started,
    log_indexing_finished,
    log_parsing_started,
    log_parsing_finished,
)

TITLE_LOADING_MSG = 'Not yet archived...'


# homepage index for all the links 
# finished flag used to rewrite again later
def write_links_index(out_dir, links, finished=False):
    """create index.html file for a given list of links"""
    log_indexing_process_started()
    check_links_structure(links)

    log_indexing_started(out_dir, 'index.json')
    write_json_links_index(out_dir, links)
    log_indexing_finished(out_dir, 'index.json')
    
    log_indexing_started(out_dir, 'index.html')
    write_html_links_index(out_dir, links, finished=finished)
    log_indexing_finished(out_dir, 'index.html')


def load_links_index(out_dir=OUTPUT_DIR, import_path=None):
    """parse and load existing index with any new links form import_path merged in"""
    
    existing_links = []
    if out_dir:
        existing_links = parse_json_links_index(out_dir)
        check_links_structure(existing_link)

    new_links = []
    if import_path: 
        # parse and validate import file 
        # this serves as a logging function
        log_parsing_started(import_path)
        raw_links, parser_name = parse_links(import_path)
        new_links = validate_links(raw_links)
        check_links_structure(new_links)

    # merge existing links in out_dir and new links
    all_links = validate_links(existing_links + new_links)
    
    return all_links, new_links


def write_json_links_index(out_dir, links):
    """write the json links index to a given path"""

    check_links_structure(links)

    path = os.path.join(out_dir, 'index.json')

    index_json = {
        'info': 'ArchiveBox Index',
        'help': 'https://github.com/pirate/ArchiveBox',
        'version': GIT_SHA,
        'num_links': len(links),
        'updated': str(datetime.now().timestamp()),
        'links': links,
    }

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(index_json, f, indent=4, default=str)

    chmod_file(path)
    # very important, change file mode here 


def write_html_links_index(out_dir, links, finished=False):
    """write the html link index to a given path"""

    check_links_structure(links)

    path = os.path.join(out_dir, 'index.html')

    copy_tree(os.path.join(TEMPLATES_DIR, 'static'), os.path.join(out_dir, 'static'))

    with open(os.path.join(out_dir, 'robots.txt'), 'w+') as f:
        f.write('User-agent: *\nDisallow: /')

    with open(os.path.join(TEMPLATES_DIR, 'index.html'), 'r', encoding='utf-8') as f:
        index_html = f.read()

    with open(os.path.join(TEMPLATES_DIR, 'index_row.html'), 'r', encoding='utf-8') as f:
        link_row_html = f.read()

    full_links_info = (derived_link_info(link) for link in links)

    link_rows = '\n'.join(
        Template(link_row_html).substitute(**{
            **link,
            'title': (
                link['title']
                or (link['base_url'] if link['is_archived'] else TITLE_LOADING_MSG)
            ),
            'favicon_url': (
                os.path.join('archive', link['timestamp'], 'favicon.ico')
                # if link['is_archived'] else 'data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs='
            ),
            'archive_url': urlencode(
                wget_output_path(link) or 'index.html'
            ),
        })
        for link in full_links_info
    )

    template_vars = {
        'num_links': len(links),
        'date_updated': datetime.now().strftime('%Y-%m-%d'),
        'time_updated': datetime.now().strftime('%Y-%m-%d %H:%M'),
        'footer_info': FOOTER_INFO,
        'git_sha': GIT_SHA,
        'short_git_sha': GIT_SHA[:8],
        'rows': link_rows,
        'status': 'finished' if finished else 'running',
    }

    with open(path, 'w', encoding='utf-8') as f:
        f.write(Template(index_html).substitute(**template_vars))

    chmod_file(path)


def parse_json_links_index(out_dir=OUTPUT_DIR):
    """parse an archive index json file and return the list of links"""
    index_path = os.path.join(out_dir. 'index.json')
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f: 
            links = json.load(f)['links']
            check_link_structure(links)
            return links 
    
    return [] 