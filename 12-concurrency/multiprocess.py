######################################
# Multiprocessing Basics
######################################

# https://pymotw.com/3/multiprocessing/index.html


'''
concepts
'''
# process - a running instance of a computer program
# processes do not share memories unless explicitly asked

# multiprocessing vs. multithreading
# - multiprocessing has less need for synchronization (since processes don't share memory)
# - processes can be paused and terminated 
# - an error in a process can't bring down others 
# - but has higher memory and expensive context switches 
# - use multiprocessing for CPU bound operations and multithreading for I/O bound operations


'''
multiprocessing
'''
# multiprocessing module
# - leverage subprocessors 
# - similar interface to the threading module

# items passes to process has to be pickable (converted to bytes)
# - basic types, collections, class with pickalable attributes

# In the case of multiprocessing, the primary drawback is that sharing data between
# processes is very costly. All communication between processes,
# whether by queues, pipes, or a more implicit mechanism requires pickling the objects.

# Excessive pickling quickly dominates processing time. Multiprocessing works best
# when relatively small objects are passed between processes and a tremendous amount
# of work needs to be done on each one.

import multiprocessing

def work(val):
    print('test'+val)

if __name__ == '__main__':
    val = 'text'
    t = multiprocessing.Process(target=work, args=(val,))
    t.start()
    t.join()

# daemon process
# a child process that does not prevent its parent process from exiting
# by default, the main program will not exit until all of the children have exited

# terminate processes
p.multiprocessing.Process(target=func)
p.terminate()
p.join() # It is important to join() the process after terminating it in order to give the process management code time to update the status of the object to reflect the termination.
p.is_alive()
p.exitcode # 0 means normally exited
# shared resources may be put in an inconsistent state
# only use terminate on processes not using shared resources
# finally cluses and exit handlers will not be run


# arguments
# Unlike with threading, in order to pass arguments to a multiprocessing Process the arguments must be able to be serialized using pickle

def worker(num):
    print('Worker:', num)

jobs = []
for i in range(5):
    p = multiprocessing.Process(target=worker, args=(i,))
    jobs.append(p)
    p.start()


# current process
multiprocessing.current_process().name



'''
process pool
'''

# - Only cpu_count() processes can run simultaneously
# - Each process consumes resources with a full copy of the Python interpreter
# - Communication between processes is expensive
# - Creating processes takes a nonzero amount of time

# Benefits
# - Hide the process of passing data between processes
# - Abstract away the overhead of figuring out what code is executing in the main process vs. subprocess

# specify number of working processes
# if none, default to number of CPU cores available to the machine
# no need for pickling of args

# define a function to be executed with iterable as args
# apply to the pool

import multiprocessing 

def do_work(data):
    return data**2

def start_process():
    print('Starting', multiprocesing.current_process().name)

if __name__ == '__main__':
    pool_size = multiprocessing.cpu_count()*2
    pool = multiprocessing.Pool(processes=pool_size, initializer=start_process)
    inputs = list(range(10))
    outputs = pool.map(do_work, inputs)
    print(outputs)

    pool.close() # no more tasks
    pool.join() # wait for worker processes to exit

'''
map async
'''
# when the call needs result of map operation
# with async, result is returned immediately and only be fetched when calling result.get()
# pool has apply and apply_async
# the result variable is a promise to return values by calling get(). Also has methods like ready() and wait()

from multiprocessing import Pool
import time

def multiply(x, y):
    return x*y

if __name__ == '__main__':
    pool = Pool(processes=4)
    result = pool.apply_async(multi, (7,7)) # evaluate asyncly
    print(result.get())


'''
inter-process communication
'''
# if want to exchange data, use os-enabled communication channels

# multiprocessing.Pipe
# pipe is bidirectional by default
# no locking, or consistency guarantees

# multiprocessing.Queue
# multiproducer, multiconsumer queues


'''
shared state
'''
# shared memory with multiprocessing.Value

# one for incoming queries and one to send outgoing results
def search(paths, query_q, results_q):
    lines = []
    for path in paths:
        lines.extend(l.strip() for l in path.open())
    query = query_q.get()
    while query:
        results_q.put([l for l in lines if query in l])
        query = query_q.get()

from multiprocessing import Process, Queue, cpu_count
from path import path
cpus = cpu_count()

pathnames = [f for f in path('.').listdir() if f.isfile()]
paths = [pathnames[i::cpus] for i in range(cpus)]
query_queues = [Queue() for p in range(cpus)]
results_queue = Queue()


'''
subclass process
'''

# Although the simplest way to start a job in a separate process is to use Process and pass a target function, it is also possible to use a custom subclass.

import multiprocessing

class Worker(multiprocessing.Process):

    def run(self):
        print('In {}'.format(self.name))
        return 

jobs = []
for i in range(5):
    p = Worker()
    jobs.append(p)
    p.start()
for j in jobs:
    j.join()





######################################
# Multiprocessing Examples
######################################


'''
run a task in a separate subprocess
'''

# https://github.com/mara/mara-pipelines/blob/ae17c34e7759915b5e37799c486c4c03443aedae/mara_pipelines/execution.py#L397