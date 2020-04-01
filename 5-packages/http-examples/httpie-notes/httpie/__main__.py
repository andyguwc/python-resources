#!/usr/bin/env python
"""The main entry point. Invoke as `http' or `python -m httpie'.

"""
import sys


def main():
    try:
        from .core import main
        exit_status = main()
    except KeyboardInterrupt:
        from httpie.status import ExitStatus
        exit_status = ExitStatus.ERROR_CTRL_C

    # this is refering to the ExitStatus, which is a class essentially mapping error value to error code 
    sys.exit(exit_status.value)


if __name__ == '__main__':
    main()
