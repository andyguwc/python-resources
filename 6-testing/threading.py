

# Threading
# Python’s threading library allows you to create multiple threads. Because of the GIL
# (at least in CPython), there will only be one Python process running per Python
# interpreter, meaning there will only be a performance gain when at least one thread is
# blocking (e.g., on I/O). The other option for I/O is to use event handling. For that, see
# the paragraphs on asyncio in “Performance networking tools in Python’s Standard
# Library” on page 247.
# What happens in Python when you have multiple threads is the kernel notices that
# one thread is blocking on I/O, and it switches to allow the next thread to use the processor
# until it blocks or is finished. All of this happens automatically when you start
# your threads.


# Multiprocessing
# The multiprocessing module in Python’s Standard Library provides a way to bypass
# the GIL—by launching additional Python interpreters.


# Subprocess
# The subprocess library was introduced into the Standard Library in Python 2.4 and
# defined in PEP 324. It launches a system call (like unzip or curl) as if called from the
# command line (by default, without calling the system shell), with the developer
# selecting what to do with the subprocess’s input and output pipes.

