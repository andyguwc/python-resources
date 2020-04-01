import argparse
import os
import platform
import sys
from typing import List, Union

import requests
from pygments import __version__ as pygments_version
from requests import __version__ as requests_version

from httpie import __version__ as httpie_version
from httpie.client import collect_messages
from httpie.context import Environment
from httpie.downloads import Downloader
from httpie.output.writer import write_message, write_stream
from httpie.plugins import plugin_manager
from httpie.status import ExitStatus, http_status_to_exit_status


def main(
    args=sys.argv,
    env = Environment(),
    ):
    program_name, *args = args # parse out specific argument, save rest to a list
    env.program_name = os.path.basename(program_name)
    args = decode_raw_args(args, env.stdin_encoding)
    plugin_manager.load_installed_plugins()

    from httpie.cli.definition import parser 

    if env.config.default_options:
        args = env.config.default_options + args 
    
    include_debug_info = '--debug' in args
    include_traceback = include_debug_info or '--traceback' in args

    if include_debug_info:
        print_debug_info(env)
        if args == ['--debug']:
            return ExitStatus.SUCCESS

    exit_status = ExitStatus.SUCCESS

    try: 
        parsed_args = parser.parse_args(
            args=args,
            env=env,
        )
    except KeyboardInterrupt:
        env.stderr.write('\n')
        if include_traceback:
            raise 
        exit_status = ExitStatus.ERROR_CTRL_C
    except SystemExit as e:
        if e.code != ExitStatus.SUCCESS:
            env.stderr.write('\n')
            if include_traceback:
                raise 
            exit_status = ExitStatus.Error 
    else:
        try:
            exit_status = program(
                args=parsed_args,
                env=env,
            )
        except KeyboardInterrupt:
            env.stderr.write('\n')
            if include_traceback:
                raise
            exit_status = ExitStatus.ERROR_CTRL_C
        except SystemExit as e:
            if e.code != ExitStatus.SUCCESS:
                env.stderr.write('\n')
                if include_traceback:
                    raise
                exit_status = ExitStatus.ERROR
        except requests.Timeout:
            exit_status = ExitStatus.ERROR_TIMEOUT
            env.log_error(f'Request timed out ({parsed_args.timeout}s).')
        except requests.TooManyRedirects:
            exit_status = ExitStatus.ERROR_TOO_MANY_REDIRECTS
            env.log_error(
                f'Too many redirects'
                f' (--max-redirects=parsed_args.max_redirects).'
            )
        except Exception as e:
            # TODO: Further distinction between expected and unexpected errors.
            msg = str(e)
            if hasattr(e, 'request'):
                request = e.request
                if hasattr(request, 'url'):
                    msg = (
                        f'{msg} while doing a {request.method}'
                        f' request to URL: {request.url}'
                    )
            env.log_error(f'{type(e).__name__}: {msg}')
            if include_traceback:
                raise
            exit_status = ExitStatus.ERROR

    return exit_status


def program(
    args,
    env
    ):
    """
    The main program without error handling.

    """
    exit_status = ExitStatus.SUCCESS
    downloader = None 

    try:
        if args.download:
            args.follow = True  # --download implies --follow.
            downloader = Downloader(
                output_file=args.output_file,
                progress_file=env.stderr,
                resume=args.download_resume
            )
            downloader.pre_request(args.headers)