##################################################
# Subprocess
##################################################

# https://pymotw.com/3/subprocess/index.html

# The subprocess module supports three APIs for working with processes. 
# - The run() function, added in Python 3.5, is a high-level API for running a process and optionally collecting its output. 
# - The functions call(), check_call(), and check_output() are the former high-level API, carried over from Python 2. They are still supported and widely used in existing programs. 
# - The class Popen is a low-level API used to build the other APIs and useful for more complex process interactions. The constructor for Popen takes arguments to set up the new process so the parent can communicate with it via pipes.

# The subprocess module is intended to replace functions such as os.system(), os.spawnv(), the variations of popen() in the os and popen2 modules

import subprocess

# Using run() without passing check=True is equivalent to using call(), which only returned the exit code from the process.
completed = subprocess.run(['ls', '-l'])
print('returncode:', completed.returncode)

# Setting the shell argument to a true value causes subprocess to spawn an intermediate shell process which then runs the command.
completed = subprocess.run('echo $HOME', shell=True)
print('returncode:', completed.returncode)

# error handling
# The returncode attribute of the CompletedProcess is the exit code of the program. The caller is responsible for interpreting it to detect errors. If the check argument to run() is True, the exit code is checked and if it indicates an error happened then a CalledProcessError exception is raised.

# Passing check=True to run() makes it equivalent to using check_call().
try:
    subprocess.run(['false'], check=True)
except subprocess.CalledProcessError as err:
    print('Error:', err)

# Capture output
# Passing check=True and setting stdout to PIPE is equivalent to using check_output().
completed = subprocess.run(
    ['ls', '-l'],
    stdout=subprocess.PIPE,
)
print('returncode:', completed.returncode)
print('Have {} bytes in stdout:\n{}'.format(
    len(completed.stdout),
    completed.stdout.decode('utf-8'))
)

# Capture output and error
completed = subprocess.run(
    'echo to stdout; echo to stderr 1>&2; exit 1',
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

'''
Popen - working with process directly
'''

# To check if a child process has terminated, call subprocess.Popen.poll() with subprocess.Popen as the child process. If a None value is returned it indicates that the process hasn’t terminated yet.

a_child_process = subprocess.Popen(args=["echo", "0"], stdout=subprocess.PIPE)
a_child_process.terminate()
print(a_child_process.poll())



# One-way Communication With a Process
# To run a process and read all of its output, set the stdout value to PIPE and call communicate().

# subprocess_popen_read.py
import subprocess

print('read:')
proc = subprocess.Popen(
    ['echo', '"to stdout"'],
    stdout=subprocess.PIPE,
)
stdout_value = proc.communicate()[0].decode('utf-8')
print('stdout:', repr(stdout_value))


# To set up a pipe to allow the calling program to write data to it, set stdin to PIPE.

# subprocess_popen_write.py
import subprocess

print('write:')
proc = subprocess.Popen(
    ['cat', '-'],
    stdin=subprocess.PIPE,
)
proc.communicate('stdin: to stdin\n'.encode('utf-8'))


# Popen.communicate
# https://docs.python.org/3/library/subprocess.html#subprocess.Popen.communicate

# communicate() returns a tuple (stdout_data, stderr_data). The data will be strings if streams were opened in text mode; otherwise, bytes.

# Note that if you want to send data to the process’s stdin, you need to create the Popen object with stdin=PIPE. Similarly, to get anything other than None in the result tuple, you need to give stdout=PIPE and/or stderr=PIPE too.

# If the process does not terminate after timeout seconds, a TimeoutExpired exception will be raised. Catching this exception and retrying communication will not lose any output.

# The child process is not killed if the timeout expires, so in order to cleanup properly a well-behaved application should kill the child process and finish communication:

proc = subprocess.Popen(...)
try:
    outs, errs = proc.communicate(timeout=15)
except TimeoutExpired:
    proc.kill()
    outs, errs = proc.communicate()


'''
Popen vs. Call
'''


# subprocess.Popen is more general than subprocess.call.

# Popen doesn't block, allowing you to interact with the process while it's running, or continue with other things in your Python program. The call to Popen returns a Popen object.

# call does block. While it supports all the same arguments as the Popen constructor, so you can still set the process' output, environmental variables, etc., your script waits for the program to complete, and call returns a code representing the process' exit status.

# returncode = call(*args, **kwargs) 
# is basically the same as calling

# returncode = Popen(*args, **kwargs).wait()
# call is just a convenience function. It's implementation in CPython is in subprocess.py:

def call(*popenargs, timeout=None, **kwargs):
    """Run command with arguments.  Wait for command to complete or
    timeout, then return the returncode attribute.

    The arguments are the same as for the Popen constructor.  Example:

    retcode = call(["ls", "-l"])
    """
    with Popen(*popenargs, **kwargs) as p:
        try:
            return p.wait(timeout=timeout)
        except:
            p.kill()
            p.wait()
            raise
# As you can see, it's a thin wrapper around Popen.


'''
Popen vs. Run
'''

# subprocess.run was added in Python 3.5 as a simplification over subprocess.Popen when you just want to execute a command and wait until it finishes, but you don't want to do anything else meanwhile. For other cases, you still need to use subprocess.Popen.

# The main difference is that subprocess.run executes a command and waits for it to finish, while with subprocess.Popen you can continue doing your stuff while the process finishes and then just repeatedly call subprocess.communicate yourself to pass and receive data to your process.

# Note that, what subprocess.run is actually doing is invoking for you the Popen and communicate, so you don't need to make a loop to pass/receive data nor wait for the process to finish.

# Using run() without passing check=True is equivalent to using call(), which only returned the exit code from the process.


'''
shell
'''

>>> import subprocess
>>> subprocess.call('echo $HOME')
Traceback (most recent call last):
...
OSError: [Errno 2] No such file or directory
>>>
>>> subprocess.call('echo $HOME', shell=True)
/user/someuser
# Setting the shell argument to a true value causes subprocess to spawn an intermediate shell process, and tell it to run the command. In other words, using an intermediate shell means that variables, glob patterns, and other special shell features in the command string are processed before the command is run. Here, in the example, $HOME was processed before the echo command. Actually, this is the case of command with shell expansion while the command ls -l considered as a simple command.

# Invoking the shell invokes a program of the user's choosing and is platform-dependent. Generally speaking, avoid invocations via the shell.

