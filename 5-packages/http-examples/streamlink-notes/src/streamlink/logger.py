# important definition of loggers
import logging
import sys
import warnings
from logging import NOTSET, ERROR, WARN, INFO, DEBUG, CRITICAL
from threading import Lock

from streamlink.compat import is_py2
from streamlink.utils.encoding import maybe_encode

TRACE = 5
_levelToName = dict([(CRITICAL, "critical"), (ERROR, "error"), (WARN, "warning"), (INFO, "info"), (DEBUG, "debug"),
                     (TRACE, "trace"), (NOTSET, "none")])
_nameToLevel = dict([(name, level) for level, name in _levelToName.items()])

# add level names
for level, name in _levelToName.items():
    logging.addLevelName(level, name)

# use this for config options
levels = [name for _, name in _levelToName.items()]
_config_lock = Lock()



