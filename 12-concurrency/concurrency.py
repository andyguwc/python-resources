##################################################
# Concurrency
##################################################

'''
concepts
'''
# https://realpython.com/python-concurrency/

# concurrency
# the execution of multiple instruction sequences at the same time
# more shared resources, more coordination needed, making concurrent programming hard

# Threading and asyncio both run on a single processor and therefore only run one at a time. They just cleverly find ways to take turns to speed up the overall process. Even though they don’t run different trains of thought simultaneously, we still call this concurrency.

# parallel programming vs. async programming
# parallel 
# - taking one task split into multiple parts to execute 
# - all process cores are engaged
# - best for CPU intensive tasks (string, number, graphics operations)
# async
# - single thread, continues to do other work while waiting for response
# - best for I/O tasks (api calls, db operations)


'''
i/o bound vs cpu bound
'''
# I/O-Bound Process	
# - Your program spends most of its time talking to a slow device, like a network connection, a hard drive, or a printer.	
# - Speeding it up involves overlapping the times spent waiting for these devices.

# CPU-Bound Process
# - You program spends most of its time doing CPU operations.
# - Speeding it up involves finding ways to do more computations in the same amount of time.



##################################################
# threading
##################################################

'''
threading concepts
'''
# process 
# - execution context of a running program (running instance of a computer program)
# - process has resources

# thread
# - smallest sequence of instructions that can be managed by the OS
# - use of multiple threads allow a process to perform multiple tasks at once
# - each thread has its own registers, stack (local variables), and counters
# - share memory and files

# initially just the main thread
# main thread then create new threads
# after calling start, the new thread turn from new state to ready state (availalble to run on CPU)
# after calling join, main thread goes to block state, completion of subthread unblocks, and main thread can finish execution

# context switching 
# - the saving and restoring of thread state
# - thread interference (race conditions, both threads read and update the same variable)

# shared memory
# threads have access to all the memory and thus all the variables in the program
# this can lead to inconsistencies in the pgoram state - can lead to race conditions
# shared memory is also fast 

'''
create threads
'''
# create a thread
# calling a start method on the thread method
import threading
def work(val):
    print('test'+ val)

val = 'text'
t = threading.Thread(target=work, args=(val,))
t.start()
t.join() # suspend execution of thread

# can also inherit from the threading.Thread 

# https://github.com/tim-ojo/python-concurrency-getting-started/blob/master/thumbnail_maker.py


# expand the Thread class
# then call the start method
from threading import Thread

class InputReader(Thread):
    def run(self):
        self.line_of_text = input()

thread = InputReader()
thread.start()

count = result = 1
while thread.is_alive():
    result = count * count
    count += 1

print("calculated squares up to {0} * {0} = {1}".format(count, result))
print("while you typed '{}'".format(thread.line_of_text))


'''
thread synchronization
'''
# keep shared memory to a minimum 

# threading.Lock
# - when put into a lock state by a thread, can only be unlocked by the same thread
# - if thread A tries to acquire a lock already acquired by thread B, then thread A goes into a blocked state until thread B releases the lock
lock = threading.Lock()
lock.acquire()
try: 
    # access shared resource
finally:
    lock.release()

# or use the with context
with lock:
    # access shared resource

# Semaphore
# increments and decrements the counter
# use this to limit number of concurrent threads running

sem = threading.Semaphore(6)
with sem: 
    # do stuff

# event
event = threading.Event()
# a client thread can wait for the flag to be set
event.wait() # block if flag is false

# a server thread can set of unset it
event.set() # set flag to true
event.clear() # reset flag to false

# condition
# useful for producer pattern
cond = Condition()
# consume one item
cond.acquire()
while not item_available():
    cond.wait()
get_an_available_item()
cond.release()
# produce one item
cond.acquire()
make_item_available()
cond.notify()
cond.release()


'''
multiple read threads
'''
# queue
# put(): puts an item to the queue
# get(): removes an item from the queue and return it
# task_done(): marks an item as completed
# join(): blocks until all items in the queue have been processed


'''
global interpreter lock
'''
# global lock ensures only one thread accessing python data structures at a time (using the CPU)
# instead of true multi-threading, cooperatively threads take turns 
# help with I/O bound operations, not helping for CPU bound operations
# The Python interpreter is an application which only runs as one single process by default and is therefore not able to take advantage of more than one virtual core.


'''
thread local storage
'''
# https://realpython.com/python-concurrency/#threading-version

# Another strategy to use here is something called thread local storage. threading.local() creates an object that looks like a global but is specific to each individual thread. 

# session is not thread safe and can't be shared among threads

import concurrent.futures
import requests
import threading
import time

# local() creates an object that looks global but is specific to each individual thread. It takes care of separating accesses from different threads to different data

thread_local = threading.local()

def get_session():
    if not hashlib(thread_local, 'session'):
        thread_local.session = requests.Session()
    return thread_local.session


def download_site(url):
    session = get_session()
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")
    

# Once you have a ThreadPoolExecutor, you can use its handy .map() method. This method runs the passed-in function on each of the sites in the list. It automatically runs them concurrently using the pool of threads it is managing.

def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site, sites)






##################################################
# Multiprocessing
##################################################

'''
concepts
'''

# With multiprocessing, Python creates new processes. A process here can be thought of as almost a completely different program, though technically they’re usually defined as a collection of resources where the resources include memory, file handles and things like that. One way to think about it is that each process runs in its own Python interpreter.

# The multiprocessing version takes full advantage of the multiple CPUs the machine has

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

# terminate processes
p.multiprocessing.Process(target=func)
p.terminate()
p.is_alive()
p.exitcode # 0 means normally exited
# shared resources may be put in an inconsistent state
# only use terminate on processes not using shared resources
# finally cluses and exit handlers will not be run



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


# https://realpython.com/python-concurrency/#multiprocessing-version
import requests
import multiprocessing
import time

session = None

def set_global_session():
    global session
    if not session:
        session = requests.Session()

def download_site(url):
    with session.get(url) as response:
        name = multiprocessing.current_process().name
        print(f"{name}:Read {len(response.content)} from {url}")

# Next we have the initializer=set_global_session part of that call. Remember that each process in our Pool has its own memory space. That means that they cannot share things like a Session object. You don’t want to create a new Session each time the function is called, you want to create one for each process.

# The initializer function parameter is built for just this case. There is not a way to pass a return value back from the initializer to the function called by the process download_site(), but you can initialize a global session variable to hold the single session for each process. Because each process has its own memory space, the global for each one will be different.

def download_all_sites(sites):
    with multiprocessing.Pool(initializer=set_global_session) as pool:
        pool.map(download_site, sites)



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




##################################################
# Abstracting Concurrency
##################################################

'''
concurrent module
'''

# define task
# pass to executor (I/O bound task the executor is thread, CPU bound task the executor is process)
# wait for result to complete

# executor interface
# executor = # new threadpool or processpool instance
names = ['a', 'b', 'c']
results = executor.map(func, names)

# executor methods
submit(fn, *args, **kwargs) # schedules a function to run
map(fn, *iterables, timeout=None, chunksize=1) # chop up iterable into chunks
shutdown(wait=True) # stop accepting tasks and shutdown

ThreadPoolExecutor(max_workers=None, thread_name_prefix="")
ProcessPoolExector(max_workers=None)


from concurrent.futures import ProcessPoolExecutor
import hashlib

texts = ['a', 'b', 'c']

def generate_hash(text):
    return hashlib.sha384(text).hexdigest()

if __name__ == '__main__':
    with ProcessPoolExecutor() as executor:
        for text, hash_t in zip(texts, executor.map(generate_hash, texts)):
            print('%s hash is: %s' % (text, hash_t))

# future object
# enables async


##################################################
# asyncio
##################################################

'''
asyncio concepts
'''
# https://realpython.com/python-concurrency/#asyncio-version

# The general concept of asyncio is that a single Python object, called the event loop, controls how and when each task gets run. The event loop is aware of each task and knows what state it’s in. In reality, there are many states that tasks could be in, but for now let’s imagine a simplified event loop that just has two states.

# The ready state will indicate that a task has work to do and is ready to be run, and the waiting state means that the task is waiting for some external thing to finish, such as a network operation.

# Your simplified event loop maintains two lists of tasks, one for each of these states. It selects one of the ready tasks and starts it back to running. That task is in complete control until it cooperatively hands the control back to the event loop.

# An important point of asyncio is that the tasks never give up control without intentionally doing so. They never get interrupted in the middle of an operation. This allows us to share resources a bit more easily in asyncio than in threading. You don’t have to worry about making your code thread-safe.


# single threaded asynchronous 
# while executing a task, a thread can pause a task and execute another task
# suitable for I/O bound tasks 


'''
async await
'''
# You can view await as the magic that allows the task to hand control back to the event loop. When your code awaits a function call, it’s a signal that the call is likely to be something that takes a while and that the task should give up control.

import asyncio
import time
import aiohttp


async def download_site(session, url):
    async with session.get(url) as response:
        print("Read {0} from {1}".format(response.content_length, url))


async def download_all_sites(sites):
    # You can share the session across all tasks, so the session is created here as a context manager. The tasks can share the session because they are all running on the same thread. There is no way one task could interrupt another while the session is in a bad state.

    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    asyncio.get_event_loop().run_until_complete(download_all_sites(sites))
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} sites in {duration} seconds")


'''
event loop
'''
# event driven model
# worker processes immediately responds to others
# nodejs brings asyncio and event loop into recognition
# event loop - taking items from an event queue and handling it

# get event loop
asyncio.get_event_loop()

AbstractEventLoop.run_forever()
AbstractEventLoop.stop()
AbstractEventLoop.close()

# cooperative multitasking
# coroutines
import asyncio

# turns this into a coroutine function suitable for event loop
# this function returns a coroutine object
async def say_hello():
    await asyncio.sleep(1)
    print('Hello World')

loop = asyncio.get_event_loop()
loop.run_until_complete(say_hello())
loop.close()

# future object
# manages the execution and represents the eventual result of a computation
# task object
# a subclass of future that is used to wrap and manage the execution of a coroutine in an event loop
# schedules a task to run on an event loop
AbstractEventLoop.create_task(coro)

# coroutine chaining
async def perform_task():
    print('waiting for result1')
    result1 = await subtask1()
    print('waiting for result2')
    result2 = await subtask2()
    return (result1, result2)

async def subtask1():
    return 'result1'

async def subtask2():
    return 'result2'

loop = asyncio.get_event_loop()
result = loop.run_until_complete(perform_task())
event_loop.close()

# parallel exectution of tasks

async def get_items(num_items):
    print('getting items')
    item_coros = [
        get_item(i) for i in range(num_items)
    ]
    print('waiting two seconds for tasks to complete')
    completed, pending = await asyncio.wait(item_coros, timeout=2)
    results = [t.result() for t in completed]
    print('results: {!r}'.format(results))

    if pending:
        print('cancelling remaining tasks')
        for t in pending:
            t.cancel()

loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(get_items(4))
finally:
    loop.close()

# cancel task if exceed the timeout limit
try:
    result = await asyncio.wait_for(task, 30.0)
except asyncio.TimeoutError:
    print('task did not complete in 30 seconds so was cancelled')




