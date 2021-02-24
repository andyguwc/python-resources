##################################################
# Signals
##################################################


# https://pymotw.com/3/signal/index.html

# Signals are an operating system feature that provide a means of notifying a program of an event, and having it handled asynchronously. They can be generated by the system itself, or sent from one process to another. 

# As with other forms of event-based programming, signals are received by establishing a callback function, called a signal handler, that is invoked when the signal occurs.

import signal
import os
import time

def receive_signal(signum, stack):
    print('Received:', signum)

signal.signal(signal.SIGUSR1, receive_signal)
signal.signal(signal.SIGUSR2, receive_signal)

print('My PID is:', os.getpid())

while True:
    print('waiting')
    time.sleep(3)

# Retrieving registered handlers

import signal
def alarm_reveied(n, stack):
    retun 

signal.signal(signal.SIGALRM, alarm_received)

signals_to_names = {
    getattr(signal, n): n
    for n in dir(signal)
    if n.startswith('SIG') and '_' not in n
}

for s, name in sorted(signals_to_names.items()):
    handler = signal.getsignal(s)
    if handler is signal.SIG_DFL:
        handler = 'SIG_DFL'
    elif handler is signal.SIG_IGN:
        handler = 'SIG_IGN'
    print('{:<10} ({:2d}):'.format(name, s), handler)

# ignore signals
# register SIG_IGN as the handler
import signal
import os
import time

def do_exit(sig, stack):
    raise SystemExit('Exiting')

signal.signal(signal.SIGINT, signal.SIG_IGN)
signal.signal(signal.SIGUSRL, do_exit)

print('My PID:', os.getpid())

signal.pause()



# Signals and threads
# the main thread of a process will receive signals
import signal
import threading
import os
import time

def signal_handler(num, stack):
    print('Received signal {} in {}'.format(
        num, threading.currentThread().name))

signal.signal(signal.SIGUSR1, signal_handler)


def wait_for_signal():
    print('Waiting for signal in',
          threading.currentThread().name)
    signal.pause()
    print('Done waiting')


