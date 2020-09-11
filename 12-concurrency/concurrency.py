##################################################
# Concurrency
##################################################

'''
concepts
'''
# concurrency
# the execution of multiple instruction sequences at the same time
# more shared resources, more coordination needed, making concurrent programming hard

# parallel programming vs. async programming
# parallel 
# - taking one task split into multiple parts to execute 
# - all process cores are engaged
# - best for CPU intensive tasks (string, number, graphics operations)
# async
# - single thread, continues to do other work while waiting for response
# - best for I/O tasks (api calls, db operations)


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
# global lock ensures only one thread accessing python data structures at a time
# instead of true multi-threading, cooperatively threads take turns 
# help with I/O bound operations, not helping for CPU bound operations
# The Python interpreter is an application which only runs as one single process by default and is therefore not able to take advantage of more than one virtual core.


##################################################
# Multiprocessing
##################################################

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

# single threaded asynchronous 
# while executing a task, a thread can pause a task and execute another task
# suitable for I/O bound tasks 

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
# this function returns a corouting object
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




