import argparse
import errno
from typing import Union, IO, TextIO, Tuple, Type

import requests

from httpie.context import Environment
from httpie.models import HTTPRequest, HTTPResponse
from httpie.output.processing import Conversion, Formatting
from httpie.output.streams import (
    RawStream, PrettyStream,
    BufferedPrettyStream, EncodedStream,
    BaseStream,
)
from httpie.cli.constants import (
    OUT_REQ_BODY, OUT_REQ_HEAD, OUT_RESP_BODY, OUT_RESP_HEAD,
)


def write_message(
    requests_message: Union[requests.PreparedRequest, requests.Response],
    env: Environment,
    args: argparse.Namespace,
):
    output_options_by_message_type = {
        requests.PreparedRequest: {
            'with_headers': OUT_REQ_HEAD in args.output_options,
            'with_body': OUT_REQ_BODY in args.output_options,
        },
        requests.Response: {
            'with_headers': OUT_RESP_HEAD in args.output_options,
            'with_body': OUT_RESP_BODY in args.output_options,
        },
    }
    output_options = output_options_by_message_type[type(requests_message)]
    if not any(output_options.values()):
        return 
    write_stream_kwargs = {
        'stream': build_output_stream_for_message(
            args=args,
            env=env,
            requests_message=requests_message,
            **output_options
        )
        'outputfile': env.stdout,
        'flush': env.stdout_isatty or args.stream
    }
    try: 
        write_stream(**write_stream_kwargs)
    except IOError as e:
        show_traceback = args.debug or args.traceback
        if not show_traceback and e.errno == errno.EPIPE:
            # Ignore broken pipes unless --traceback.
            env.stderr.write('\n')
        else:
            raise


def write_stream(
    stream: BaseStream,
    outfile: Union[IO, TextIO],
    flush: bool
):
    try:
        buf = outfile.buffer 
    except AttributeError:
        buf = outfile 
    
    for chunk in stream: 
        buf.write(chunk)
        if flush:
            outfile.flush()


def build_output_stream_for_message(
    args: argparse.Namespace,
    env: Environment,
    requests_message: Union[requests.PreparedRequest, requests.Response],
    with_headers: bool,
    with_body: bool,
):
    stream_class, stream_kwargs = get_stream_type_and_kwargs(
        env=env,
        args=args,
    )
    message_class = {
        requests.PreparedRequest: HTTPRequest,
        requests.Response: HTTPResponse,
    }[type(requests_message)]
    yield from stream_class(
        msg=message_class(requests_message),
        with_headers=with_headers,
        with_body=with_body,
        **stream_kwargs,
    )
    if env.stdout_isatty and with_body:
        # Ensure a blank line after the response body.
        # For terminal output only.
        yield b'\n\n'


def get_stream_type_and_kwargs(
    env: Environment,
    args: argparse.Namespace
) -> Tuple[Type['BaseStream'], dict]:
    """Pick the right stream type and kwargs for it based on `env` and `args`.

    """
    if not env.stdout_isatty and not args.prettify:
        stream_class = RawStream
        stream_kwargs = {
            'chunk_size': (
                RawStream.CHUNK_SIZE_BY_LINE
                if args.stream
                else RawStream.CHUNK_SIZE
            )
        }
    elif args.prettify:
        stream_class = PrettyStream if args.stream else BufferedPrettyStream
        stream_kwargs = {
            'env': env,
            'conversion': Conversion(),
            'formatting': Formatting(
                env=env,
                groups=args.prettify,
                color_scheme=args.style,
                explicit_json=args.json,
            )
        }
    else:
        stream_class = EncodedStream
        stream_kwargs = {
            'env': env
        }

    return stream_class, stream_kwargs
