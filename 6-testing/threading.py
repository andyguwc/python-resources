################################################
# threading library
################################################

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


'''
thread basics
'''
# https://realpython.com/intro-to-python-threading/
# https://pymotw.com/3/threading/index.html


# For most Python 3 implementations the different threads do not actually execute at the same time: they merely appear to.

# Getting multiple tasks running simultaneously requires a non-standard implementation of Python, writing some of your code in a different language, or using multiprocessing which comes with some extra overhead.

# Because of the way CPython implementation of Python works, threading may not speed up all tasks. This is due to interactions with the GIL that essentially limit one Python thread to run at a time.

# Tasks that spend much of their time waiting for external events are generally good candidates for threading. Problems that require heavy CPU computation and spend little time waiting for external events might not run faster at all.

# pass a function and a list containing the arguments to the function
def thread_function(name):
    time.sleep(1)
    print(name)

x = threading.Thread(target=thread_function, args=(1,))
x.start()

# wait for thread to finish, 
# the main thread pauses and wait for thread x to complete running
# doesn't matter if it is a thread of daemon thread
x.join()

# join with timeout
# By default, join() blocks indefinitely. It is also possible to pass a float value representing the number of seconds to wait for the thread to become inactive. If the thread does not complete within the timeout period, join() returns anyway.
x.join(0.1)


'''
daemon threads
'''
# Python threading has a more specific meaning for daemon. A daemon thread will shut down immediately when the program exits. One way to think about these definitions is to consider the daemon thread a thread that runs in the background without worrying about shutting it down.

# If a program is running Threads that are not daemons, then the program will wait for those threads to complete before it terminates. Threads that are daemons, however, are just killed wherever they are when the program is exiting.

# If you look at the source for Python threading, you’ll see that threading._shutdown() walks through all of the running threads and calls .join() on every one that does not have the daemon flag set.


x = threading.Thread(target=thread_function, args=(1,), daemon=True)
x.start()


threads = list()
for index in range(3):
    x = threading.Thread(target=thread_function, args=(index,))
    threads.append(x)
    x.start()

for index, thread in enumerate(threads):
    thread.join()


'''
current thread
'''
# this prints out the current thread's name
threading.current_thread().getName()
t = threading.Thread(name='my_service', target=my_service)

# logging module for threadName

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] (%(threadName)-10s) %(message)s'
)

'''
customized threading.Thread
'''

class Crawler(threading.Thread):
    def __init__(self):
        super().__init__()
        self.done = False
    
    def isDone(self):
        return self.done

    def run(self):
        time.sleep(5)
        self.done = True
        raise Exception('Something bad happened!')

t = Crawler()
t.start()



################################################
# ThreadPoolExecutor
################################################

'''
threadpool basics
'''

# https://pymotw.com/3/concurrent.futures/index.html

# The code creates a ThreadPoolExecutor as a context manager, telling it how many worker threads it wants in the pool. It then uses .map() to step through an iterable of things, in your case range(3), passing each one to a thread in the pool.

# The end of the with block causes the ThreadPoolExecutor to do a .join() on each of the threads in the pool. It is strongly recommended that you use ThreadPoolExecutor as a context manager when you can so that you never forget to .join() the threads.

# context manager
# executors work as context managers, running tasks concurrently and waiting for them all to complete. When the context manager exits, the shutdown() method of the executor is called.

from concurrent.futures import ThreadPoolExecutor

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(thread_function, range(3))


from concurrent import futures
import threading
import time 

def task(n):
    print('{}: sleeping {}'.format(
        threading.current_thread().name,
        n)
    )
    return n / 10

ex = futures.ThreadPoolExecutor(max_workers=2)
results = ex.map(task, range(5, 0, -1))
print(list(results))




'''
schedule individual tasks
'''

# use the future instance returned to wait for the task's results

from concurrent import futures
import threading
import time

def task(n):
    print('{}: sleeping {}'.format(
        threading.current_thread().name,
        n
    ))
    time.sleep(n / 10)
    return n / 10

ex = futures.ThreadPoolExecutor(max_workers=2)
print('main: starting')
f = ex.submit(task, 5)
print('main: future: {}'.format(f))
print('main: waiting for results')
result = f.result()

print('main: result: {}'.format(result))
print('main: future after result: {}'.format(f))


class FakeDatabase:
    def __init__(self):
        self.value = 0

    def update(self, name):
        logging.info("Thread %s: starting update", name)
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy
        logging.info("Thread %s: finishing update", name)


database = FakeDatabase()

with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    for index in range(2):
        executor.submit(database.update, index)
logging.info("Testing update. Ending value is %d.", database.value)


'''
wait for tasks in random order
'''

# Invoking the result() method of a Future blocks until the task completes (either by returning a value or raising an exception), or is canceled. The results of multiple tasks can be accessed in the order the tasks were scheduled using map(). If it does not matter what order the results should be processed, use as_completed() to process them as each task finishes.

from concurrent import futures
import random
import time

def task(n):
    time.sleep(random.random())
    return (n, n / 10)

ex = futures.ThreadPoolExecutor(max_workers=5)
print('main: starting')

wait_for = [
    ex.submit(task, i)
    for i in range(5, 0, -1)
]

for f in futures.as_completed(wait_for):
    print('main: result: {}'.format(f.result()))




'''
callbacks
'''
# take some action when a task completed, without explicitly waiting for the result, use
# add_done_callback() to specify a new function to call when the Future is done

from concurrent import futures
import time

def task(n):
    time.sleep(0.5)
    return n / 5


def task(n):
    return n / 10


def done(fn):
    if fn.cancelled():
        print('{}: canceled'.format(fn.arg))
    elif fn.done():
        error = fn.exception()
        if error:
            print('{}: error returned: {}'.format(fn.arg, error))
        else:
            result = fn.result()
            print('{}: value returned: {}'.format(fn.arg, result))


if __name__ == '__main__':
    ex = futures.ThreadPoolExecutor(max_workers=2)
    print('main: starting')
    f = ex.submit(task, 5)
    f.arg = 5
    f.add_done_callback(done)
    result = f.result()




################################################
# Lock
################################################


'''
lock and race conditions
'''
# There are two things to keep in mind when thinking about race conditions:
# Even an operation like x += 1 takes the processor many steps. Each of these steps is a separate instruction to the processor.
# The operating system can swap which thread is running at any time. A thread can be swapped out after any of these small instructions. This means that a thread can be put to sleep to let another thread run in the middle of a Python statement.

def inc(x):
    x += 1

import dis
dis.dis(inc)


# Acquire lock
# To find out whether another thread has acquired the lock without holding up the current thread, pass False for the blocking argument to acquire()

# In this case, the second call to acquire() is given a zero timeout to prevent it from blocking because the lock has been obtained by the first call.

lock = threading.Lock()

print('First try :', lock.acquire())
print('Second try:', lock.acquire(0))


# local context management
def worker_with(lock):
    with lock:
        logging.debug('Lock acquired directly')

def worker_no_with(lock):
    lock.acquire()
    try:
        logging.debug('Lock acquired directly')
    finally:
        lock.release()
    
logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

lock = threading.Lock()
w = threading.Thread(target=worker_with, args=(lock,))
nw = threading.Thread(target=worker_no_with, args=(lock,))

w.start()
nw.start()


'''
controlling access to resources
'''
# https://pymotw.com/3/threading/index.html#controlling-access-to-resources
# In addition to synchronizing the operations of threads, it is also important to be able to control access to shared resources to prevent corruption or missed data. Python’s built-in data structures (lists, dictionaries, etc.) are thread-safe as a side-effect of having atomic byte-codes for manipulating them (the global interpreter lock used to protect Python’s internal data structures is not released in the middle of an update). Other data structures implemented in Python, or simpler types like integers and floats, do not have that protection. To guard against simultaneous access to an object, use a Lock object.

import logging
import random
import threading
import time


class Counter:
    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.value = start

    def increment(self):
        logging.debug('Waiting for lock')
        self.lock.acquire()
        try:
            logging.debug('Acquired lock')
            self.value = self.value + 1
        finally:
            self.lock.release()

def worker(c):
    for i in range(2):
        pause = random.random()
        logging.debug('Sleeping %0.02f', pause)
        time.sleep(pause)
        c.increment()
    logging.debug('Done')

counter = Counter()
for i in range(2):
    t = threading.Thread(target=worker, args=(counter,))
    t.start()

logging.debug('Waiting for worker threads')
main_thread = threading.main_thread()
for t in threading.enumerate():
    if t is not main_thread:
        t.join()
logging.debug('Counter: %d', counter.value)


# Avoid race conditions with Lock
# https://realpython.com/intro-to-python-threading/#basic-synchronization-using-lock

class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()
    
    def locked_update(self, name):
        logging.info("Thread %s: starting update", name)
        logging.debug("Thread %s about to lock", name)
        with self._lock:
            logging.debug("Thread %s has lock", name)
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy
            logging.debug("Thread %s about to release lock", name)
        logging.debug("Thread %s after release", name)
        logging.info("Thread %s: finishing update", name)

'''
RLock
'''
# Use RLock to avoid deadlock caused by calling lock acquire multiple times
# Python threading has a second object, called RLock, that is designed for just this situation. It allows a thread to .acquire() an RLock multiple times before it calls .release(). That thread is still required to call .release() the same number of times it called .acquire(), but it should be doing that anyway.

# In a situation where separate code from the same thread needs to “re-acquire” the lock, use an RLock instead.
import threading

lock = threading.RLock()

print('First try :', lock.acquire())
print('Second try:', lock.acquire(0))





'''
Limiting concurrent access to resources
'''
# https://pymotw.com/3/threading/index.html#limiting-concurrent-access-to-resources
# using Semaphore to limit number of concurrent runs

# at most two threads are running concurrently
import logging
import random
import threading
import time


class ActivePool:

    def __init__(self):
        super(ActivePool, self).__init__()
        self.active = []
        self.lock = threading.Lock()

    def makeActive(self, name):
        with self.lock:
            self.active.append(name)
            logging.debug('Running: %s', self.active)

    def makeInactive(self, name):
        with self.lock:
            self.active.remove(name)
            logging.debug('Running: %s', self.active)


def worker(s, pool):
    logging.debug('Waiting to join the pool')
    with s:
        name = threading.current_thread().getName()
        pool.makeActive(name)
        time.sleep(0.1)
        pool.makeInactive(name)


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s (%(threadName)-2s) %(message)s',
)

pool = ActivePool()
s = threading.Semaphore(2)
for i in range(4):
    t = threading.Thread(
        target=worker,
        name=str(i),
        args=(s, pool),
    )
    t.start()
        


################################################
# Producer Consumer
################################################

'''
producer consumer using lock
'''

# https://realpython.com/intro-to-python-threading/#producer-consumer-using-lock

# The Pipeline in this version of your code has three members:

# .message stores the message to pass.
# .producer_lock is a threading.Lock object that restricts access to the message by the producer thread.
# .consumer_lock is also a threading.Lock that restricts access to the message by the consumer thread.
# __init__() initializes these three members and then calls .acquire() on the .consumer_lock. This is the state you want to start in. The producer is allowed to add a new message, but the consumer needs to wait until a message is present.

# .get_message() and .set_messages() are nearly opposites. .get_message() calls .acquire() on the consumer_lock. This is the call that will make the consumer wait until a message is ready.

# Once the consumer has acquired the .consumer_lock, it copies out the value in .message and then calls .release() on the .producer_lock. Releasing this lock is what allows the producer to insert the next message into the pipeline.

class Pipeline:
    """
    Class to allow a single element pipeline between producer and consumer.
    """
    def __init__(self):
        self.message = 0
        self.producer_lock = threading.Lock()
        self.consumer_lock = threading.Lock()
        self.consumer_lock.acquire()

    def get_message(self, name):
        self.consumer_lock.acquire()
        message = self.message
        self.producer_lock.release()
        return message

    def set_message(self, message, name):
        self.producer_lock.acquire()
        self.message = message
        self.consumer_lock.release()


format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,
                    datefmt="%H:%M:%S")
# logging.getLogger().setLevel(logging.DEBUG)

pipeline = Pipeline()
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    executor.submit(producer, pipeline)
    executor.submit(consumer, pipeline)


'''
producer consumer using queue
'''

# https://realpython.com/intro-to-python-threading/#producer-consumer-using-queue

# Queue is thread safe

# The threading.Event object allows one thread to signal an event while many other threads can be waiting for that event to happen. The key usage in this code is that the threads that are waiting for the event do not necessarily need to stop what they are doing, they can just check the status of the Event every once in a while.

import logging
import threading
import random
import queue
import time
from concurrent.futures import ThreadPoolExecutor

# Assume set event means terminating signal here 

def producer(queue, event):
    while not event.is_set():
        message = random.randint(1,101)
        logging.info("Producer got message: %s", message)
        queue.put(message)
    logging.info("Producer received event. Exiting")


def consumer(queue, event):
    while not event.is_set() or not queue.empty():
        message = queue.get()
        logging.info(
            "Consumer storing message: %s (size=%d)", message, queue.qsize()
        )
    logging.info("Consumer received event. Exiting")


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    pipeline = queue.Queue(maxsize=10)
    event = threading.Event()
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)

        time.sleep(0.1)
        logging.info("Main: about to set event")
        event.set()


'''
producer consumer using Condition
'''
# https://pymotw.com/3/threading/index.html#synchronizing-threads

# Condition uses a Lock, it can be tied to a shared resource, allowing multiple threads to wait for the resource to be updated.

import threading
import time


def consumer(cond):
    """wait for the condition and use the resource"""
    logging.debug('Starting consumer thread')
    with cond:
        cond.wait()
        logging.debug('Resource is available to consumer')


def producer(cond):
    """set up the resource to be used by the consumer"""
    logging.debug('Starting producer thread')
    with cond:
        logging.debug('Making resource available')
        cond.notifyAll()


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s (%(threadName)-2s) %(message)s',
)

condition = threading.Condition()
c1 = threading.Thread(name='c1', target=consumer,
                      args=(condition,))
c2 = threading.Thread(name='c2', target=consumer,
                      args=(condition,))
p = threading.Thread(name='p', target=producer,
                     args=(condition,))

c1.start()
time.sleep(0.2)
c2.start()
time.sleep(0.2)
p.start()
# The threads use with to acquire the lock associated with the Condition. Using the acquire() and release() methods explicitly also works.

# $ python3 threading_condition.py

# 2016-07-10 10:45:28,170 (c1) Starting consumer thread
# 2016-07-10 10:45:28,376 (c2) Starting consumer thread
# 2016-07-10 10:45:28,581 (p ) Starting producer thread
# 2016-07-10 10:45:28,581 (p ) Making resource available
# 2016-07-10 10:45:28,582 (c1) Resource is available to consumer
# 2016-07-10 10:45:28,582 (c2) Resource is available to consumer


################################################
# Threading Examples
################################################

'''
multi-threaded crawler
'''

import requests
from bs4 import BeautifulSoup
from queue import Queue, Empty
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin, urlparse


class MultiThreadScraper:

    def __init__(self, base_url):
        self.base_url = base_url
        self.root_url = '{}://{}'.format(urlparse(self.base_url).scheme, urlparse(self.base_url).netloc)
        # initialize a thread pool to submit tasks and allow us to use a callback function to collect our results
        self.pool = ThreadPoolExecutor(max_workers=20)
        # cache the list of pages already scraped
        self.scraped_pages = set([])
        # queue which contains URLs to crawl, continue grabbing URLs from queue until it it's empty
        self.to_crawl = Queue()
        self.to_crawl.put(self.base_url)

    def parse_links(self, html):
        # extract all links, and resolve relative URLs, while excluding external links
        soup = BeautifulSoup(html, 'html.parser')
        links = soup.find_all('a', href=True)
        for link in links:
            url = link['href']
            if url.startswith('/') or url.startswith(self.root_url):
                url = urljoin(self.root_url, url)
                if url not in self.scraped_pages:
                    self.to_crawl.put(url)

    def scrape_info(self, html):
        return

    def post_scrape_callback(self, res):
        # callback function which takes the result (a response object) and furthers parsing and scraping
        result = res.result()
        if result and result.status_code == 200:
            self.parse_links(result.text)
            self.scrape_info(result.text)

    def scrape_page(self, url):
        # returns a requests.Response object
        try:
            res = requests.get(url, timeout=(3, 30))
            return res
        except requests.RequestException:
            return

    def run_scraper(self):
        # loop through until the queue of todos is empty
        # for each link, first acknowledge it in the visited cache
        # then submit the scrape_page task with the target link to the pool
        # add callback which parses the info, and saves more links to the todo queue
        while True:
            try:
                target_url = self.to_crawl.get(timeout=60)
                if target_url not in self.scraped_pages:
                    print("Scraping URL: {}".format(target_url))
                    self.scraped_pages.add(target_url)
                    job = self.pool.submit(self.scrape_page, target_url)
                    job.add_done_callback(self.post_scrape_callback)
            except Empty:
                return
            except Exception as e:
                print(e)
                continue

if __name__ == '__main__':
    s = MultiThreadScraper("http://www.example.co.uk")
    s.run_scraper()


# another more naive way to call a crawler in multiple threads
# https://medium.com/analytics-vidhya/multi-threaded-python-web-crawler-for-https-pages-e103f0839b71


'''
using threading for IO bound tasks
'''
# append thread results to a common list
# here the use case is to collect search results by executing search from a different source on each thread
# https://github.com/0xHJK/music-dl/blob/aeca4ca584a6fd11c2b177c5e14afbf029104d92/music_dl/source.py#L54-L63

# the threaded function takes in a list of results as state to add onto

class MusicSource:

    def search_thread(self, source, keyword, ret_songs_list, ret_errors):
        try:
            addon = importlib.import_module(".addons." + source, __package__)
            ret_songs_list += addon.search(keyword)
        except (RequestError, ResponseError, DataError) as e:
            ret_errors.append((source, e))
        except Exception as e:
            # 最后一起输出错误信息免得影响搜索结果列表排版
            err = traceback.format_exc() if config.get("verbose") else str(e)
            ret_errors.append((source, err))
        finally:
            # 放在搜索后输出是为了营造出搜索很快的假象
            click.echo(" %s ..." % colorize(source.upper(), source), nl=False)
    
    def search(self, keyword, sources_list):
        thread_pool = []
        ret_songs_list = []
        ret_errors = []

        click.echo("")
        click.echo(
            _("Searching {keyword} from ...").format(
                keyword=colorize(config.get("keyword"), "highlight")
            ),
            nl=False,
        )

        for source_key in sources_list:
            if not source_key in sources_map:
                raise ParameterError("Invalid music source.")

            t = threading.Thread(
                target=self.search_thread,
                args=(sources_map.get(source_key), keyword, ret_songs_list, ret_errors),
            )
            thread_pool.append(t)
            t.start()
        
        for t in thread_pool:
            t.join()
        
        click.echo("")
        # 输出错误信息
        for err in ret_errors:
            self.logger.debug(_("音乐列表 {error} 获取失败.").format(error=err[0].upper()))
            self.logger.debug(err[1])


'''
Async support 
'''
# Async support using ThreadPoolExecutor
# https://github.com/Diaoul/subliminal/blob/a4113adb745dc5cd2da7254ee14802077237bb15/subliminal/core.py#L241
from concurrent.futures import ThreadPoolExecutor

class AsyncProviderPool(ProviderPool):
    """Subclass of :class:`ProviderPool` with asynchronous support for :meth:`~ProviderPool.list_subtitles`.
    :param int max_workers: maximum number of threads to use. If `None`, :attr:`max_workers` will be set
        to the number of :attr:`~ProviderPool.providers`.
    """

    def __init__(self, max_workers=None, *args, **kwargs):
        super(AsyncProviderPool, self).__init__(self, *args, **kwargs)
        self.max_workers = max_workers or len(self.providers)

    def list_subtitles_provider(self, provider, video, languages):
        return provider, super(AsyncProviderPool, self).list_subtitles_provider(provider, video, languages)
    
    def list_subtitles(self, video, languages):
        subtitles = []

        with ThreadPoolExecutor(self.max_workers) as executor:
            for provider, provider_subtitles in executor.map(self.list_subtitles_provider, self.providers, 
                                                             itertools.repeat(video, len(self.providers)),
                                                             itertools.repeat(languages, len(self.providers))):
                if provider_subtitles is None:
                    logger.info('Discarding provider %s', provider)
                    self.discarded_providers.add(provider)
                    continue

                # add subtitles
                subtitles.extend(provider_subtitles)
            
            return subtitles


'''
define classes with threading methods
'''
# several classes with methods to start and stop threads
# https://github.com/Bitwise-01/Instagram-/blob/288a5e6073a377c43cb4f6cb3c56137bde9862bc/lib/scraper.py#L93-L123

# https://github.com/Bitwise-01/Instagram-/blob/288a5e6073a377c43cb4f6cb3c56137bde9862bc/lib/bruter.py


class Scraper(object):

    def __init__(self):
        self.lock = RLock()
        self.is_alive = True
        self.display = Display()
        self.scraped_proxies = []

        self.links = [
            'https://sslproxies.org',
            'https://free-proxy-list.net',
            'https://free-proxy-list.net/anonymous-proxy.html',
        ]

    def parse_proxy(self, proxy):
        # proxy is from a bs4 object that we'll parse into dictionaries
        proxy = proxy.find_all('td')
        if proxy[4].string != 'transparent' and proxy[5].string != 'transparent':
            return {
                'ip': proxy[0].string,
                'port': proxy[1].string,
                'country': proxy[3].string
            }
    
    def scrape_proxy(self, link):
        # parse all proxies from a link and add results to memory
        proxies = []

        try: 
            proxies = bs(get(link, timeout=fetch_time).text,
                         'html.parser').find('tbody').find_all('tr')
        except:
            pass
        
        if not proxies:
            with self.lock:
                if self.is_alive and debug:
                    self.display.warning(
                        'Failed to grab proxies from {}'.format(link))

        for proxy in proxies:
            with self.lock:
                _proxy = self.parse_proxy(proxy)
                if _proxy:
                    self.scraped_proxies.append(_proxy)

    @property
    def proxies(self):
        proxy_list = ProxyList()

        threads = []
        threads = [Thread(target=self.scrape_proxies, args=[link])
                   for link in self.links]
        index = 0
        while index < len(threads) and self.is_alive:
            thread = threads[index]

            try:
                thread.daemon = True
                thread.start()
                index += 1
            except:
                sleep(0.5)
        
        # this is similar to thread.join() but it also makes sure to check if self.is_alive
        while self.is_alive and len(threads):
            for thread in [thread for thread in threads if not thread.is_alive()]:
                threads.pop(threads.index(thread))
            sleep(0.5)

        if self.is_alive:
            for proxy in self.scraped_proxies:

                if not proxy in proxy_list:
                    proxy_list.append(Proxy(proxy))
        
        return [proxy_list.list.pop(randint(0, len(proxy_list.list)-1)) for _ in range(len(proxy_list.list))]


'''
custom Thread object
'''
# look for problem data in aws logs
# https://github.com/eth0izzle/bucket-stream/blob/5da68b39bcf496415c86c772d537156bb182b8b5/bucket-stream.py#L310-L312



'''
threaded scraper
'''

# https://github.com/xianhu/PSpider/blob/bc14a5145c9a1fee6b7a0398733730624cd7f5a7/spider/concurrent/threads_pool.py



'''
download via threading
'''
# https://github.com/YongHaoWu/NeteaseCloudMusicFlac/blob/61a437e94787b311ae3bb4300430a4fb618e625c/main.py#L169-L195

# download music via ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=10) as executor:
    counter = collections.Counter()
    song_ids = executor.map(get_songid, song_list)
    song_infos = executor.map(get_song_info, song_ids)
    res = [i for i in song_infos if i['data'] == True]
    logger.info("获取歌曲信息完成，开始下载。")
    session = requests.session()
    d = tqdm.tqdm(total=len(res))
    download = partial(download_song, session=session, mp3_option=mp3_option,
                        download_folder=download_folder, display=d, counter=counter)
    executor.map(download, res)