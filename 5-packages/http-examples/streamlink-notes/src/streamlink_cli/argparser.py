import argparse
import numbers
import re
from string import printable
from textwrap import dedent

from streamlink import logger
from streamlink.utils.args import (
    boolean, comma_list, comma_list_filter, filesize, keyvalue, num
)
from streamlink.utils.times import hours_minutes_seconds
from .constants import (
    LIVESTREAMER_VERSION, STREAM_PASSTHROUGH, DEFAULT_PLAYER_ARGUMENTS, DEFAULT_STREAM_METADATA, SUPPORTED_PLAYERS
)
from .utils import find_default_player

_printable_re = re.compile(r"[{0}]".format(printable))
_option_re = re.compile(r"""
    (?P<name>[A-z-]+) # A option name, valid characters are A to z and dash.
    \s*
    (?P<op>=)? # Separating the option and the value with a equals sign is
               # common, but optional.
    \s*
    (?P<value>.*) # The value, anything goes.
""", re.VERBOSE)


# customized ArgumentParser

class ArgumentParser(arparse.ArgumentParser):
    def convert_arg_line_to_args(self, line):
        # strip characters beginning of line 
        match = _printable_re.search(line)
        if not match:
            return 
        line = line[match.start():].strip() # match.start() is the index of the match

        option = _option_re.match(line)
        if not option:
            return 

        name, value = option.group("name", "value") # https://docs.python.org/2/library/re.html#re.MatchObject.group
        if name and value:
            yield u"--{0}={1}".format(name, value)
        elif name: 
            yield u"--{0}".format(name)
    

class HelpFormatter(argparse.RawDescriptionHelpFormatter):
    """help formatter can be indented and contain new lines
    """

    def __init__(self, max_help_position=4, *args, **kwargs):
        kwargs["max_help_position"] = max_help_position

    def _split_lines(self, text, width):
        text = dedent(text).strip() + "\n\n"
        return text.splitlines()


def build_parser():
    parser = ArgumentParser(
        prog="streamlink",
        fromfile_prefix_chars="@",
        formatter_class=HelpFormatter,
        add_help=False,
        usage="%(prog)s [OPTIONS] <URL> [STREAM]",
        description=dedent("""
        Streamlink is command-line utility that extracts streams from various
        services and pipes them into a video player of choice.
        """)        
    )

    positional = parser.add_argument_group("Positional arguments") # add option groups to organize
    positional.add_argument(
        "url",
        metavars="URL",
        nargs="?", # one argument to be consumed (if not present, the value formd efault)
        help="""
        A URL to attempt to extract streams from 
        """
    )
    positional.add_argument(
        "stream",
        metavar="STREAM",
        nargs="?",
        type=comma_list, # type= can take any callable that takes a single string argument and returns the converted value
        help="""
        stream to play
        """
    )

    general = aparser.add_argument_group("General options")
    general.add_argument(
        "-h", "--help",
        action="store_true",
        help="""
        Show help message and exit
        """
    )
    general.add_argument(
        "-V", "--version",
        action="version",
        version="%(prog)s {0}".format(LIVESTREAMER_VERSION),
        help="""
        Show version number and exit.
        """
    )
    general.add_argument(
        "--plugins",
        action="store_true",
        help="""
        Print a list of plugins
        """
    )

    output = parser.add_argument_group("File output options")
    output.add_argument(
        "-o", "--output",
        metavar="FILENAME",
        help="""
        Write stream data to FILENAME instead of playing it.

        You will be prompted if the file already exists.
        """
    )

    stream = parser.add_argument_group("Stream options")
    stream.add_argument(
        "--url",
        dest="url_param",
        metavar="URL",
        help="""
        A URL to attempt to extract streams from.
        """
    )
    stream.add_argument(
        "--default-stream",
        type=comma_list,
        metavar="STREAM",
        help="""
        Stream to play.
        """
    )
    stream.add_argument(
        "--retry-streams",
        metavar="DELAY",
        type=num(float, min=0),
        help="""
        Retry
        """
    )

    return parser 

__all__ = ["build_parser"]
