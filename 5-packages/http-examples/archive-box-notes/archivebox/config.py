import os
import re 
import sys
import shutil

from subprocess import run, PIPE, DEVNULL 


# lots of configs
# use os.path.abspath
try:
    OUTPUT_DIR = os.path.abspath(os.getenv('OUTPUT_DIR'))
except Exception:
    OUTPUT_DIR = None
    
ARCHIVE_DIR_NAME = 'archive'
SOURCES_DIR_NAME = 'sources'
ARCHIVE_DIR = os.path.join(OUTPUT_DIR, ARCHIVE_DIR_NAME)
SOURCES_DIR = os.path.join(OUTPUT_DIR, SOURCES_DIR_NAME)