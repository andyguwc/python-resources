# can run directly using python archive.py
# https://github.com/pirate/ArchiveBox/blob/master/archivebox/archive.py

# lots of imports 
import os
import sys

from links import links_after_timestamp
from index import write_links_index, load_links_index
from archive_methods import archive_link
# import config
from config import (
    ARCHIVE_DIR,
    ONLY_NEW,
    OUTPUT_DIR,
    GIT_SHA,
)
from util import (
    save_remote_source,
    save_stdin_source,
)
from logs import (
    log_archiving_started,
    log_archiving_paused,
    log_archiving_finished,
)


__VERSION__ = GIT_SHA[:9]


# print_help
def print_help():
    print('ArchiveBox: The self-hosted internet archive.\n')
    print("Documentation:")
    print("    https://github.com/pirate/ArchiveBox/wiki\n")
    print("UI Usage:")


# good implementation for triggering help messages
# calling by main(*sys.argv)
def main(*args):
    if set(args).intersection(('-h', '--help', 'help')) or len(args) > 2:
        print_help()
        raise SystemExit(0)

    if set(args).intersection(('--version', 'version')):
        print('ArchiveBox version {}'.format(__VERSION__))
        raise SystemExit(0) 

    # handle CLI arguments
    import_path, resume = None, None 
    if len(args) == 2:
        # if the argument is a string, it's a import path file to import 
        # if it's a number, it's a timestamp tp resume archiving from 
        if args[1].replace('.','').isdigit():
            import_path, resume = None, args[1]
        else:
            import_path, resume = args[1], None 
        
    # set up output folder
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    
    # handle ingesting urls piped in through stdin 
    # (e.g. if use does cat example_urls.txt | ./archive)
    if not sus.stdin.isatty():
        stdin_raw_text = sys.stdin.read()
        if stdin_raw_text and import_path:
            print(
                '[X] You should pass either a path as an argument, '
                'or pass a list of links via stdin, but not both.\n'
            )
            print_help()
            raise SystemExit(1)
        if stdin_raw_text:
            import_path = save_stdin_source(stdin_raw_text)

    # handle ingesting urls from a remote file.feed 
    if import_path and any(import_path.startswith(s) for s in ('http://', 'https://', 'ftp://')):
        import_path = save_remote_source(import_path)

    # run the main archive update process
    update_archive_data(import_path=import_path, resume=resume)


def update_archive_data(import_path=None, resume=None):
    """Main entrance point
    """
    # step 1: load list of links form existing index 
    # merge in and dedupe new links from import path 
    all_links, new_links = load_links_index(out_dir=OUTPUT_DIR, import_path=import_path)

    # step 2: write updated index with deduped old and new links back to disk 
    write_links_index(out_dir=OUTPUT_DIR, links=all_links)

    # step 3: run the archive methods for each link 
    links = new_links if ONLY_NEW else all_links
    log_archiving_started(len(links), resume)

    # important note here - iterate through (if keyboard interrupt print out the stop)
    idx, link = 0, 0 
    try: 
        for idx, link in enumerate(links_after_timestamp(links, resume)):
            links_dir = os.path.join(ARCHIVE_DIR, link['timestamp'])
            archive_link(link_dir, link)
    
    except KeyboardInterrupt: 
        log_archiving_paused(len(links), idx, link and link['timestamp'])
        raise SystemExit(0)

    except:
        print()
        raise 

    log_archiving_finished(len(links))

    # Step 4: Re-write links index with updated titles, icons, and resources
    all_links, _ = load_links_index(out_dir=OUTPUT_DIR)
    write_links_index(out_dir=OUTPUT_DIR, links=all_links, finished=True)


if __name__ == '__main__':
    main(*sys.argv)