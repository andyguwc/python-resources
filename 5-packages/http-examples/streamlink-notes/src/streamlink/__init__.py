from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
__title__ = "streamlink"
__license__ = "Simplified BSD"
__author__ = "Streamlink"
__copyright__ = "Copyright 2020 Streamlink"
__credits__ = []

from .api import streams
from .exceptions import (StreamlinkError, PluginError, NoStreamsError,
                         NoPluginError, StreamError)
from .session import Streamlink
