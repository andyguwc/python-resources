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





