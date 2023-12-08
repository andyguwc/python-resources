##################################################
# Data Structures
##################################################

##################################################
# Basic Data Types
##################################################

'''
Numeric
'''

# Numeric 
int # unlimited precision signed integer
float # double precision 64 bit float - 1 sign, 11 exponent, 52 fraction
sys.float_info # more info about float 
# for large numbers - float can lose precision 
float(2*53+1) # outputs the same as float(2*53)

# fraction can also be misrepresented 

# decimal
# Decimal type in decimal module 
import decimal
decimal.getcontext() # decimal configured with 28 places of decimal precisiion 
# always quote literal values to avoid intermediate inprecise base 2 
Decimal('0.8') - Decimal('0.7') # Decimal('0.1)
Decimal(0.8) - Decimal(0.7) # Decimal('0.1000000000000000888178419700')

# decimal precision is propagated 
Decimal(3)
Decimal(2.0)
# Fraction for representing fraction numbers 
# can be constructed from string and decimals
Fraction(2,3)

abs() # distance from zero
round() # aviid bias, round towards even numbers
round(1.5) # 2
round(2.5) # 2
round(Decimal('3.25', 1)) # Decimal('3.2')
# round can show suprising behavior with float which can't be represented as binary numbers


##################################################
# Datetime Module
##################################################
'''
Datetime
'''

# datetime module 

# date
import datetime
datetime.date(2014,1,6)
datetime.date(year=2014, month=1, day=6)
datetime.datetime.now() # local time from the machine
datetime.datetime.utcnow() # utc time 

d = datetime.date.today()
d.month
d.day 
d.isoformat()

# transform from epoch time 
datetime.date.fromtimestamp(10000000)

# attributes
d = datetime.date.today() # current date
d.year
d.month
d.day
d.weekday()
d.isoweekday()
d.isoformat()

# strftime()
# string format time
# default string representation uses the ISO format YYYY-MM-DDTHH:MM:SS.mmmmmm
"the date is {:%A %d %B %Y}".format(d) # day, date, month, year

format = "%a %b %d %H:%M:%S %Y"
today = datetime.datetime.today()
s = today.strftime(format)

# time
datetime.time(hour=23, minute=59, second=59, microsecond=9999)
d = datetime.date.today()
t = datetime.time(8,15)
datetime.datetime.combine(d,t)

# create datetime from time 
import time
import datetime
t = time.time()
print('fromtimestamp(t):', datetime.date.fromtimestamp(t))

# timedelta
# duration - represent differences between timestamps
a = datetime.datetime(year=2004, month=1, day=8, hour=12, minute=22)
b = datetime.datetime(year=2010, month=2, day=6, hour=10, minute=20)
d = a - b # outputs datetime.timedelta 
d.total_seconds() # output number of seconds
datetime.date.today() + datetime.timedelta(weeks=3) # in three weeks time
datetime.timedelta(seconds=1)
datetime.timedelta(days=1)

# timedelta constructor
# instances store only days, seconds, microseconds
# while constructor accepsts almost everything from microseconds to weeks 


# timezone (optional)
# tzinfo object
datetime.timezone 
cet = datetime.timezone(datetime.timedelta(hours=1), "CET") # define a timezone
departure = datetime.datetime(year=2014, month=1, day=7, hour=11, minute=30, tzinfo=cet)
arrival = datetie.datetime(year=2014, month=1, day=8, hour=10, minute=30, tzinfo=datetime.timezone.utc)
str(arrival - departure) 


from datetime import datetime, timezone
now = datetime(2014, 8, 10, 18, 18, 30)

# convert utc to local time 
now_utc = now.replace(tzinfo=timezone.utc) # utc time 
now_local = now_utc.astimezone() # local time
print(now_local)

# convert local time to utc 
time_format = '%Y-%m-%d %H:%M:%S'
time_str = '2014-08-10 11:18:30'
now = datetime.strptime(time_str, time_format)
time_tuple = now.timetuple()
utc_now = mktime(time_tuple)
print(utc_now)

# pytz for converting between time zones 
# first convert Eastern Time time to UTC datetime
arrival_nyc = '2014-05-01 23:33:24'
nyc_dt_naive = datetime.strptime(arrival_nyc, time_format)
eastern = pytz.timezone('US/Eastern')
nyc_dt = eastern.localize(nyc_dt_naive)
utc_dt = pytz.utc.normalize(nyc_dt.astimezone(pytz.utc))
print(utc_dt)

# once with UTC datetime, can covnert to Pacific Time 
pacific = pytz.timezone('US/Pacific')
sf_dt = pacific.normalize(utc_dt.astimezone(pacific))
print(sf_dt)


##################################################
# List
##################################################

'''
List
'''
# list is not ideal for queues
# inserting and deleting an element at the beginning requires shifting 
# the other elemnts by one, requiring O(n) time 


# Lists
alist = [10,20,30,40]
alist = ["a","b","c"]

# Lists are mutable 
alist = ["a","b","c"]
alist[0] = "pear"

#  Element Deletion 
del alist[1]
del alist[1:5]

# objects and references 
# We can test whether two names refer to the same object using the is operator. The is operator will return true if the two references are to the same object. In other words, the references are the same. Try our example from above.
# for immutable strings, python optimizes resources by by making two names that refer to the same string value refer to the same object
a = "banana"
b = "banana"
print(a is b)

# This is not the case with lists, which never share an id just because they have the same contents.
a = [81,82,83]
b = [81,82,83]

# a and b have equivalent values but do not refer to the same object. 
# Because their contents are equivalent, a==b evaluates to True; because they are not the same object, a is b evaluates to False.
print(a is b) # evaluates to false
print(a == b) # evaluates to true

# append
mylist = []
mylist.append(5)
mylist.insert(1,12)
mylist.sort()
lastitem = mylist.pop()

# slicing 
# [start:stop:step]
s = 'bicycle'
s[::3] # 'bye'
s[::-1] # 'elcycib'
s[::-2] # 'eccb'


'''
Unpacking
'''
# Unpacking actually works with any object that happens to be iterable, not just tuples or
# lists. This includes strings, files, iterators, and generators.
data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
name, shares, price, date = data
# throw away variable names 
_, shares, price, _ = data


# unpacking elements from iterables of arbitrary length 
record = ['name', 'email', 'phone1', 'phone2']
name, email, *phone_numbers = user_record 

# string unpacking
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')

# append vs. extend
# Append: Adds its argument as a single element to the end of a list. The length of the list increases by one.
my_list = ['geeks', 'for'] 
my_list.append('geeks') 
print my_list 

# extend(): Iterates over its argument and adding each element to the list and extending the list. The length of the list increases by number of elements in it’s argument.
my_list = ['geeks', 'for'] 
another_list = [6, 0, 4, 1] 
my_list.extend(another_list) 


'''
Filtering
'''
# best to use list comprehension 

# filter creates an iterator. To make sure using a list of results use the list()
values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
ivals = list(filter(is_int, values))
print(ivals)


'''
Enumerate
'''
# enumerate provides concise syntax for looping over an iterator and getting the
# index of each item from the iterator as you go.

# iterating over the index value pairs 
my_list = ['a','b','c']
for idx, val in enumerate(my_list):
    print(idx, val)

# use enumerate instead of range(len(astr))
# clumsy implementation
for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print('%d: %s' % (i+1, flavor))
# enumerate implementation 
for i, flavor in enumerate(flavor_list):
    print('%d: %s' % (i+1, flavor))


'''
Zip & Chain
'''
# iterating over multiple sequences simultaneously
# use zip whenever you need to pair data together 
# In Python 3, zip is a lazy generator that produces tuples

xpts = [1,2,3]
ypts = [3,4,5]
for x,y in zip(xpts, ypts):
    print(x, y)

for name, count in zip(names, letters):
    if count > max_letters:
        longest_name = name
        max_letters = count

# use chain for iterating on items in separate containers
from itertools import chain 
a = [1,2,3]
b = ['x','y','z']
for x in chain(a, b):
    print(x)


##################################################
# Sorting
##################################################

'''
Sort and Sorted 
'''

# list.sort and the sorted built in function 
# list.sort sorts a list in place without making a copy
# sorted creates a new list and returns it 

# takes two optional parameters
# reverse (if True the items are returned in descending order)
# key (a one argument function that will be applied to each item to produce its sorting key, key = len will sort by length)
fruits = ['grape', 'raspberry', 'apple', 'banana']
sorted(fruits)
sorted(fruits, reverse=True) # reverses alphabetical ordering 
sorted(fruits, key = len) # sorted by length 

L1 = [1, 7, 4, -2, 3]
L1.sort() # the list itself was modified by this 

L2 = ["Cherry", "Apple", "Blueberry"]
L3 = sorted(L2)
print(L3) 

L1 = [1, 7, 4, -2, 3]
def absolute(x):
    if x >= 0:
        return x
    else:
        return -x

L2 = sorted(L1, key=absolute) # pass in a function to sort by 
print(L2)

# sorting a dictionary 
# lambda expression lambda k: d[k]

# now loop through the sorted keys
d = {'E': 2, 'F': 1, 'B': 2, 'A': 2, 'D': 4, 'I': 2, 'C': 1}

def printout(d):
    for k in sorted(d, key=lambda k: d[k], reverse=True):
      print("{} appears {} times".format(k, d[k]))
printout(d)

# sort by length then alphabetically
fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear']
new_order = sorted(fruits, key=lambda fruit_name:(len(fruit_name), fruit_name))
for fruit in new_order:
    print(fruit)

# if the property is too complex, then define a separate function instead of lambda function
def s_cities_count(city_list):
    ct = 0
    for city in city_list:
        if city[0] == "S":
            ct += 1
    return ct

states = {"Minnesota": ["St. Paul", "Minneapolis", "Saint Cloud", "Stillwater"],
          "Michigan": ["Ann Arbor", "Traverse City", "Lansing", "Kalamazoo"],
          "Washington": ["Seattle", "Tacoma", "Olympia", "Vancouver"]}

print(sorted(states, key=lambda state: s_cities_count(states[state])))



'''
bisect
'''
# https://pymotw.com/3/bisect/index.html

# bisect and insort use the binary search algorithm to find and insert items in any sorted sequence
# bisect(haystack, meedle) to locate the position where needle can be inserted 
# maintaining haystack in ascending order. All items appearing up to that position are less than or equal to needle

# bisect is actually an alias for bisect_right, and there is a sister function called
# bisect_left. Their difference is apparent only when the needle compares equal to an
# item in the list: bisect_right returns an insertion point after the existing item, and
# bisect_left returns the position of the existing item, so insertion would occur before it


origlist = [45,32,88]

origlist.append("cat") # adds a new item to the end of a list, original list modified
origlist = origlist + ["dog"] # with concatenation, a new list is created 
print(origlist)

# bisect.insort 
# insort(seq, item) inserts item into seq so as to keep seq in ascending order 

import bisect 
import random 
SIZE = 7 
random.seed(123)
my_list= []
for i in range(SIZE):
    new_item = random.randrange(SIZE*2)
    bisect.insort(my_list, new_item)
    print()

##################################################
# Queues
##################################################

# The queue module provides a first-in, first-out (FIFO) data structure suitable for multi-threaded programming. It can be used to pass messages or other data between producer and consumer threads safely. Locking is handled for the caller, so many threads can work with the same Queue instance safely and easily. The size of a Queue (the number of elements it contains) may be restricted to throttle memory usage or processing.

'''
heapq
'''
# https://pymotw.com/3/heapq/index.html

# useful data structure for maintaining priority queue
# heapq module for finding nlargest or nsmallest 
# priority queue manages a set of records with totally-ordered keys 
# retries the highest-priority element 

import heapq 

nums = [1,2,3,-4]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

a = []
heappush(a, 1)
heappush(a, 3)
heappop(a)

q = [] 
heapq.heappush(q, (2, 'a'))
heapq.heappush(q, (1, 'b'))
heapq.heappush(q, (3, 'c'))
while q: 
    next_item = heapq.heappop(q)
    print(next_item)
# Result:
# (1, 'eat')
# (2, 'code')
# (3, 'sleep')

# Accessing the 0 index of the heap will always return the smallest item.

# heap[0] is slways the smallest item. Subsequent items can be found using heapq.heappop() method 
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heap = list(nums)
heap.heapify(heap)
# [-4, 2, 1, 23, 7, 2, 18, 23, 42, 37, 8]

# for more complicated data structures 
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])


'''
PriorityQueue
'''
# Sometimes the processing order of the items in a queue needs to be based on characteristics of those items, rather than just the order they are created or added to the queue.

# https://pymotw.com/3/queue/index.html

# priorityqueue uses heapq internally and has the same time and space complexities
# PriorityQueue is synchronizedand and provides locking semantics to support multiple concurrent producers and consumers.



from queue import PriorityQueue

q = PriorityQueue()
q.put((2, 'a'))
q.put((1, 'b'))
q.put((3, 'c'))

while not q.empty():
    next_item = q.get()
    print(next_item)

# Result:
# (1, 'eat')
# (2, 'code')
# (3, 'sleep')

import functools
import queue
import threading

# define a class with total ordering implemented
@functools.total_ordering
class Job:
    def __init__(self, priority, description:
        self.priority = priority
        self.description = description

    def __eq__(self, other):
        try:
            return self.priority = other.priority
        except AttributeError:
            return NotImplemented
        
    def __lt__(self, other):
        try:
            return self.priority < other.priority
        except AttributeError:
            return NotImplemented

q = queue.PriorityQueue()
q.put(Job(3, 'Mid Job'))
q.put(Job(10, 'Low Job'))
q.put(Job(1, 'High Job'))

# multiple threads consuming the jobs
# processed based on the priority of items in the queue at the time get() was called
def process_job(q):
    while True:
        next_job = q.get()
        print('Processing job:', next_job.description)
        q.task_done()

workers = [
    threading.Thread(target=process_job, args=(q,)),
    threading.Thread(target=process_job, args=(q,)),
]
for w in workers:
    w.setDaemon(True)
    w.start()

q.join()


'''
using queue for thread management
'''
# https://pymotw.com/3/queue/index.html

# The program reads one or more RSS feeds, queues up the enclosures for the five most recent episodes from each feed to be downloaded, and processes several downloads in parallel using threads

from queue import Queue
import threading
import time
import urllib
from urllib.parse import urlparse

import feedparser

# Set up global variables
num_fetch_threads = 2
enclosure_queue = Queue()

feed_urls = [
    'http://talkpython.fm/episodes/rss',
]

def mesage(s):
    print('{}: {}'.format(threading.current_thread().name, s))

# download_enclosures() runs in the worker thread and processes the downloads using urllib

def download_enclosures(q):
    """This is the worker thread function.
    It processes items in the queue one after
    another.  These daemon threads go into an
    infinite loop, and exit only when
    the main thread ends.
    """
    while True:
        message('look for the next enclosure')
        url = q.get()
        filename = url.rpartition('/')[-1]
        message('downloading {}'.format(filename))
        response = urllib.request.urlopen(url)
        data = response.read()
        # Save the downloaded file to the current directory
        message('writing to {}'.format(filename))
        with open(filename, 'wb') as outfile:
            outfile.write(data)
        q.task_done()
    
# Once the target function for the threads is defined, the worker threads can be started. When download_enclosures() processes the statement url = q.get(), it blocks and waits until the queue has something to return. That means it is safe to start the threads before there is anything in the queue.

# Set up some threads to fetch the enclosures
for i in range(num_fetch_threads):
    worker = threading.Thread(
        target=download_enclosures,
        args=(enclosure_queue,),
        name='worker-{}'.format(i)
    )
    worker.setDaemon(True)
    worker.start()

# The next step is to retrieve the feed contents using the feedparser module and enqueue the URLs of the enclosures. As soon as the first URL is added to the queue, one of the worker threads picks it up and starts downloading it. The loop continues to add items until the feed is exhausted, and the worker threads take turns dequeuing URLs to download them.

# Downloads the feed(s) and put the enclosure URLs into the queue
for url in feed_urls:
    response = feedparser.parse(url, agent='fetch_podcasts.py')
    for entry in response['entries'][:5]:
        for enclosure in entry.get('enclosures', []):
            parsed_url = urlparse(enclosure['url'])
            message('queuing {}'.format(
                parsed_url.path.rpartition('/')[-1]))
            enclosure_queue.put(enclosure['url'])

# Now wait for the queue to be empty, indicating that we have
# processed all of the downloads.
message('*** main thread waiting')
enclosure_queue.join()
message('*** done')



##################################################
# Array
##################################################

# efficiency 
# array is more efficient than lists because array does not hold full fledged float objects but packed bytes presenting machine values 
# python array is as lean as C array 

from array import array 
from random import random 
floats = array('d', (random() for i in range(10**7))) # an array of double precision floats typecode 'd'
floats[-1] # the last item in the array 


##################################################
# Dequeue
##################################################

# A double-ended queue, or deque, supports adding and removing elements from either end of the queue. The more commonly used stacks and queues are degenerate forms of deques, where the inputs and outputs are restricted to a single end.

# The class collections.deque is a thread-safe double-ended queue designed for fast inserting and removing from both ends. Provides constant time operations for inserting or removing items from beginning or end

# The .append, and .pop makes a list usable as a stack or queue (using .append and .pop(0) to get LIFO behavior)
# But inserting and removing from left of list is costly 


from collections import deque
dq = deque(range(10), maxlen=10) # optional maxlen set the maximum number of items allowed 
dq.rotate(3) # takes items from the right end and prepends them to the left 

dq.append(e) # push the element onto the queue
dq.appendleft(4) # append to the beginning 
dq[0] # retrieve but not remove the element at the front
dq.popleft() # remove and return element at the front of the queue
dq.pop() # pops on the right 


# A deque can be populated from either end, termed “left” and “right” in the Python implementation.
import collections

# Add to the right
d1 = collections.deque()
d1.extend('abcdefg')
print('extend    :', d1)
d1.append('h')
print('append    :', d1)

# Add to the left
d2 = collections.deque()
d2.extendleft(range(6))
print('extendleft:', d2)
d2.appendleft(6)
print('appendleft:', d2)

# extend    : deque(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
# append    : deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
# extendleft: deque([5, 4, 3, 2, 1, 0])
# appendleft: deque([6, 5, 4, 3, 2, 1, 0])


# keeping a limited history using deque
# example yielding matching line and previous n lines while found
from collections import deque 

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines 
        previous_lines.append(line)

# Example use on a file 
if __name__ == '___main__':
    with open('somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)

# Define a class to inherit deque

from collections import deque
class Deck(deque):
    def __init__(self, size=1):
        super().__init__()
        for d in range(size):
            cards = [card(r,s) for r in range(10) for s in Suits] 
            super().extend(cards)
        random.shuffle(self)

from collections import dequeue 
s = dequeue()
s.append('a')
s.append('b')



'''
numpy
'''
import numpy 
a = numpy.arange(12)
a # array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
type(a) # <class 'numpy.ndarray'>
a.shape = 3,4
array([[ 0, 1, 2, 3],
       [ 4, 5, 6, 7],
       [ 8, 9, 10, 11]])


##################################################
# Sets
##################################################

# basic use case is to remove duplication 
l = ['spam', 'spam', 'eggs', 'spam']
list(set(l))

# set operations
a | b the union 
a & b the intersection
a - b the difference 
# another application of set operations is to count needles in haystack 
found = len(needles & haystack)
from unicodedata import name 
{chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i),'')}

# set comprehension 

from unicodedata import name 
{chr(i) for i in range(32,256) if 'SIGN' in name(chr(i),'')}


# hash tables in dictionaries 
# In standard data structure texts, the cells in a hash table are often called “buckets.” In a dict hash table,
# there is a bucket for each item, and it contains two fields: a reference to the key and a
# reference to the value of the item.

# hash table algorithm
# To fetch the value at my_dict[search_key], Python calls hash(search_key) to obtain
# the hash value of search_key and uses the least significant bits of that number as an
# offset to look up a bucket in the hash table (the number of bits used depends on the
# current size of the table). If the found bucket is empty, KeyError is raised. Otherwise,
# the found bucket has an item—a found_key:found_value pair—and then Python
# checks whether search_key == found_key. If they match, that was the item sought:
# found_value is returned.

# However, if search_key and found_key do not match, this is a hash collision. This happens
# because a hash function maps arbitrary objects to a small number of bits, and—in
# addition—the hash table is indexed with a subset of those bits. In order to resolve the
# collision, the algorithm then takes different bits in the hash, massages them in a particular
# way, and uses the result as an offset to look up a different bucket.



'''
Practical Implications of How Set Works
'''

# The set and frozenset types are also implemented with a hash table, except that each
# bucket holds only a reference to the element (as if it were a key in a dict, but without
# a value to go with it).

# - Set elements must be hashable objects.
# - Sets have a significant memory overhead.
# - Membership testing is very efficient.
# - Element ordering depends on insertion order.
# - Adding elements to a set may change the order of other elements.

'''
frozenset
'''
# frozenset implements an immutable version of set that cannot be changed after it has been constructed 
# froezensets are static and hashable 

vowel = frozenset({'a', 'b', 'c'})
vowels.add('p')

# Frozensets are hashable and can
# be used as dictionary keys:
# >>> d = { frozenset({1, 2, 3}): 'hello' }
# >>> d[frozenset({1, 2, 3})]




##################################################
# Bit Operations
##################################################

0b111000 #56

bin(66)

bin(0b111000 ^ 0b111000)

# operators
& # and
| # or
^ # exclusive-or
~ # not
<< # left shift
>> # right shift


##################################################
# Enum
##################################################

# https://pymotw.com/3/enum/index.html
# A new enumeration is defined using the class syntax by subclassing Enum and adding class attributes describing the values.

import enum

class BugStatus(enum.Enum):

    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1

print('\nMember name: {}'.format(BugStatus.wont_fix.name))
print('Member value: {}'.format(BugStatus.wont_fix.value))

# iterating over the num class 

for status in BugStatus:
    print('{:15} = {}'.format(status.name, status.value))


# create mapping programatically
import enum

BugStatus = enum.Enum(
    value='BugStatus',
    names=[
        ('new', 7),
        ('incomplete', 6),
        ('invalid', 5),
        ('wont_fix', 4),
        ('in_progress', 3),
        ('fix_committed', 2),
        ('fix_released', 1),
    ],
)

print('All members:')
for status in BugStatus:
    print('{:15} = {}'.format(status.name, status.value))

