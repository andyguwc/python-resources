
import argparse
import errno
import logging
import os
import platform
from collections import OrderedDict
from gettext import gettext

import requests
import sys
import signal
import webbrowser

from contextlib import closing
from distutils.version import StrictVersion
from functools import partial
from itertools import chain
from socks import __version__ as socks_version
from time import sleep
from websocket import __version__ as websocket_version

from streamlink import __version__ as streamlink_version
from streamlink import (Streamlink, StreamError, PluginError,
                        NoPluginError)
from streamlink.cache import Cache
from streamlink.exceptions import FatalPluginError
from streamlink.stream import StreamProcess
from streamlink.plugins.twitch import TWITCH_CLIENT_ID
from streamlink.plugin import PluginOptions
from streamlink.utils import LazyFormatter

import streamlink.logger as logger
from .argparser import build_parser
from .compat import stdout, is_win32
from streamlink.utils.encoding import maybe_encode
from .console import ConsoleOutput, ConsoleUserInputRequester
from .constants import CONFIG_FILES, PLUGINS_DIR, STREAM_SYNONYMS, DEFAULT_STREAM_METADATA
from .output import FileOutput, PlayerOutput
from .utils import NamedPipe, HTTPServer, ignored, progress, stream_to_url

ACCEPTABLE_ERRNO = (errno.EPIPE, errno.EINVAL, errno.ECONNRESET)
try:
    ACCEPTABLE_ERRNO += (errno.WSAECONNABORTED,)
except AttributeError:
    pass  # Not windows
QUIET_OPTIONS = ("json", "stream_url", "subprocess_cmdline", "quiet")

args = console = streamlink = plugin = stream_fd = output = None

log = logging.getLogger("streamlink.cli")


def handle_stream(plugin, streams, stream_name):
    """Decides what to do with the selected stream.

    Depending on arguments it can be one of these:
     - Output internal command-line
     - Output JSON represenation
     - Continuously output the stream over HTTP
     - Output stream data to selected output
    """
    stream_name = resolve_stream_name(streams, stream_name)
    stream = streams[stream_name]

    # Print internal command-lin eif this stream uses a subprocess 
    if args.subprocess_cmdline:
        if isinstance(stream, SteamProcess):
            try:
                cmdline = stream.cmdline()
            except StreamError as err: 
                console.exit("{0}", err)
            
            console.msg("{0}", cmdline)
        else:
            console.exit("The stream specified cannot be translated to a command")
    
    # Print JSOn representation of the stream 
    elif console.json:
        console.msg_json(stream)
    
    elif args.stream_url:
        try:
            console.msg("{0}", stream.to_url())
        except TypeError:
            console.exit()

    # Output to stream
    else:
        alt_streams = list(filter(lambda k: stream_name + "_alt" in k, 
                                  sorted(stream.keys())))
        file_output = args.output or args.stdout 
    
    for stream_name in [stream_name] + alt_streams: 
        stream  = streams[stream_name]
        stream_type = type(stream).shortname()

        if stream_type in args.player_passthrough and not file_output:
            log.info("Opening stream: {0} ({1})".format(stream_name,
                                                            stream_type))
            success = output_stream_passthrough(plugin, stream)
        elif args.player_external_http:
            return output_stream_http(plugin, streams, external=True,
                            port=args.player_external_http_port)
        elif args.player_continuous_http and not file_output:
            return output_stream_http(plugin, streams)
        else:
            log.info("Opening stream: {0} ({1})".format(stream_name,
                                                        stream_type))

            success = output_stream(plugin, stream)

        if success:
            break


def fetch_streams(plugin):
    """Fetches streams using correct parameters"""
    retur plugin.streams(stream_types=args.stream_types, 
                         sorting_excludes=args.stream_sorting_excludes)


# very good implementation of retry 
def fetch_streams_with_retry(plugin, interval, count):
    """Attempts to fetch sterams repeatedly until some are returned or limit hit."""
    try:
        streams = fetch_streams(plugin)
    except PluginError as err: 
        log.error(u"{0}".format(err))
        streams = None

    if not streams:
        log.info("waiting for streams, retrying every {}"
                 "second(s)".format(interval))
    
    attempts = 0 
    while not streams:
        sleep(interval)

        try:
            streams = fetch_streams(plugin)
        except FatalPluginError:
            raise 
        except PluginError as err:
            log.error(u"{0}".format(err))
        
        if count > 0:
            attempts += 1
            if attemps > count:
                break
    
    return streams


def resolve_stream_name(streams, stream_name):
    """Returns the real stream name of a synonym."""

    if stream_name in STREAM_SYNONYMS and stream_name in streams:
        for name, stream in streams.items():
            if stream is streams[stream_name] and name not in STREAM_SYNONYMS:
                return name

    return stream_name


def format_valid_streams(plugin, streams):
    """Formats a dict of streams.

    Filters out synonyms and displays them next to
    the stream they point to.

    Streams are sorted according to their quality
    (based on plugin.stream_weight).

    """

    delimiter = ", "
    validstreams = []

    for name, stream in sorted(streams.items(),
                               key=lambda stream: plugin.stream_weight(stream[0])):
        if name in STREAM_SYNONYMS:
            continue

        def synonymfilter(n):
            return stream is streams[n] and n is not name

        synonyms = list(filter(synonymfilter, streams.keys()))

        if len(synonyms) > 0:
            joined = delimiter.join(synonyms)
            name = "{0} ({1})".format(name, joined)

        validstreams.append(name)

    return delimiter.join(validstreams)

    
def handle_url():
    """The URL handler.

    Attempts to resolve the URL to a plugin and then attempts
    to fetch a list of available streams.

    Proceeds to handle stream if user specified a valid one,
    otherwise output list of valid streams.
    """
    try: 
        plugin = streamlink.resolve_url(args.url)
        setup_plugin_options(streamlink, plugin)
        log.info("Found matching plugin {0} for URL {1}".format(
                 plugin.module, args.url))
        
        plugin_args = []
        for parg in plugin.arguments:
            value = plugin.get_option(parg.dest)
            if value:
                plugin_args.append((parg, value))
        
        if args.retry_max or args.retry_streams:
            retry_streams = 1
            retry_max = 0
            if args.retry_streams:
                retry_streams = args.retry_streams
            if args.retry_max:
                retry_max = args.retry_max
            streams = fetch_streams_with_retry(plugin, retry_streams,
                                               retry_max)
        else:
            streams = fetch_stream(plugin)
    
    except




# use both config file and the parser to populate this namespace 
def setup_args(parser, config_files=[], ignore_unknown=False):
    """Parses arguments"""
    global args 
    arglist = sys.argv[1:] # arg list starts with the sys.argv (except first "streamlink")
    
    # then load arguments from config files 
    # not ArgumentParser takes this parameter fromfile_prefix_chars="@"
    for config_file in filter(os.path.isfile, config_file): 
        arglist.insert(0, "@"+config_file)
    
    args, unknown = parser.parse_known_args(arglist)
    if unknown and not ignore_unknown: 
        msg = gettext('unrecognized arguments" %s')
        parser.error(msg % ' '.join(known))
    
    # force lowercase to allow case-insensitive lookup 
    if args.stream: 
        args.stream = [stream.lower() for stream in args.stream]

    if not args.url and args.url_param: 
        args.url = args.url_param 


def setup_config_args(parser):
    config_files = []

    if args.url:
        with ignored(NoPluginError):
            plugin = streamlink.resolve_url(args.url)
            config_files += ["{0}.{1}".format(fn, plugin.module) for fn in CONFIG_FILES]
    
    if args.config:
        config_files += list(reversed(args.config))

    else:
        # only load first available default config 
        for config_file in filter(os.path.isfile, CONFIG_FILES):
            config_files.append(config_file)
            break 

    if config_files:
        setup_args(parser, config_files)

# important - setup the console here that other functions can refer to 
def setup_console(output):
    """Console setup."""
    global console

    # All console related operations is handled via the ConsoleOutput class
    console = ConsoleOutput(output, streamlink)
    console.json = args.json

    # Handle SIGTERM just like SIGINT
    signal.signal(signal.SIGTERM, signal.default_int_handler)


def setup_plugins(extra_plugin_dir=None):
    if os.path.isdir(PLUGINS_DIR):
        load_plugins([PLUGINS_DIR])
    
    if extra_plugin_dir:
        load_plugins(extra_plugin_dir)


def setup_streamlink():
    """Creates the Streamlink session."""
    global streamlink

    streamlink = Streamlink({"user-input-requester": ConsoleUserInputRequester(console)})


def setup_options():
    """Sets Streamlink options."""
    if args.hls_live_edge:
        streamlink.set_option("hls-live-edge", args.hls_live_edge)

    if args.hls_segment_stream_data:
        streamlink.set_option("hls-segment-stream-data", args.hls_segment_stream_data)

    if args.hls_segment_attempts:
        streamlink.set_option("hls-segment-attempts", args.hls_segment_attempts)

# can pass in 
def setup_plugin_args(session, parser):
    """Set Streamlink plugin options."""
    plugin_args = parser.add_argument_group("Plugin options")
    for pname, plugin in session.plugins.items():
        defaults = {}
        for parg in plugin.arguments: 
            plugin_args.add_argument(parg.argument_name(pname), **parg.options)
            defaults[parg.dest] = parg.default 
        
        plugin.options = PluginOptions(defaults)


def setup_plugin_options(session, plugin):
    """Sets Streamlink plugin options."""
    pname = plugin.module
    required = OrderedDict({})
    for parg in plugin.arguments:
        if parg.options.get("help") != argparse.SUPPRESS:
            if parg.required:
                required[parg.name] = parg
            value = getattr(args, parg.namespace_dest(pname))
            session.set_plugin_option(pname, parg.dest, value)
            # if the value is set, check to see if any of the required arguments are not set
            if parg.required or value:
                try:
                    for rparg in plugin.arguments.requires(parg.name):
                        required[rparg.name] = rparg
                except RuntimeError:
                    log.error("{0} plugin has a configuration error and the arguments "
                              "cannot be parsed".format(pname))
                    break
    if required:
        for req in required.values():
            if not session.get_plugin_option(pname, req.dest):
                prompt = req.prompt or "Enter {0} {1}".format(pname, req.name)
                session.set_plugin_option(pname, req.dest,
                                          console.askpass(prompt + ": ")
                                          if req.sensitive else
                                          console.ask(prompt + ": "))


def main():
    error_code = 0 
    parser = build_parser()
    setup_args(parser, ignore_unknown=True) # populate the global args variable

    # Console output should be on stderr if we are outputting a stream to stdout 
    if args.stdout or args.output == "-" or args.record_and_pipe:
        console_out = sys.stderr
    else: 
        console_out = sys.stdout 
    
    # We don't want log output when are printing JSON 
    silent_log = any(getattr(args, attr) for attr in QUIET_OPTIONS)
    log_level = args.loglevel if not silent_log else "none"
    setup_logging(console_out, log_level)
    setup_console(console_out)

    # set up streamlink session
    setup_streamlink()
    # load additional plugins
    setup_plugins(args.plugin_dirs)
    # add to the parser the plugin args 
    setup_plugin_args(streamlink, parser)
    # call setup args again once the plugin specific args have been added
    setup_args(parser)
    setup_config_args(parser)

    # update the logging level if changed by a plugin specific config
    log_level = args.loglevel if not silent_log else "none"
    logger.root.setLevel(log_level)

    setup_http_session()
    check_root()
    log_current_versions()
    
    if args.plugins:
            print_plugins()
    elif args.can_handle_url:
        try:
            streamlink.resolve_url(args.can_handle_url)
        except NoPluginError:
            error_code = 1
        except KeyboardInterrupt:
            error_code = 130
    elif args.can_handle_url_no_redirect:
        try:
            streamlink.resolve_url_no_redirect(args.can_handle_url_no_redirect)
        except NoPluginError:
            error_code = 1
        except KeyboardInterrupt:
            error_code = 130
    elif args.url:
        try:
            setup_options()
            handle_url() # this is the main call handle_url -> handle_stream -> different stream options
        except KeyboardInterrupt:
            # Close output
            if output:
                output.close()
            console.msg("Interrupted! Exiting...")
            error_code = 130
        finally:
            if stream_fd:
                try:
                    log.info("Closing currently open stream...")
                    stream_fd.close()
                except KeyboardInterrupt:
                    error_code = 130
    elif args.twitch_oauth_authenticate:
        authenticate_twitch_oauth()
    elif args.help:
        parser.print_help()
    else:
        usage = parser.format_usage()
        msg = (
            "{usage}\nUse -h/--help to see the available options or "
            "read the manual at https://streamlink.github.io"
        ).format(usage=usage)
        console.msg(msg)

    sys.exit(error_code)