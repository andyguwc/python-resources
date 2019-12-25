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

# for large numbers - float can lose precision 
float(2*53+1) # outputs the same as float(2*53)

# fraction can also be misrepresented 

# decimal
# Decimal type in decimal module 
import decimal
decimal.getcontext() # decimal configured with 28 places of decimal precisiion 
# always quote literal values to avoid intermediate inprecise base 2 

# decimal precision is propagated 
Decimal(3)
Decimal(2.0)
# Fraction for representing fraction numbers 
Fraction(2,3)

abs() # distance from zero
round() # aviid bias, round to event numbers
round(1.5) # 2
round(2.5) # 2


'''
Datetime
'''

# datetime module 
# includes date and time 
import datetime
datetime.date(2014,1,6)
datetime.date(year=2014,month=1, day=6)
datetime.date.today()

"the date is {:%A %d %B %Y}".format(d) # day, date, month, year

datetime.time(hour=23, minute=59, second=59, microsecond=9999)
d = datetime.date.today()
t = datetime.time(8,15)
datetime.datetime.combine(d,t)

# timedelta
a = datetime.datetime(year=2004, month=1, day=8, hour=12, minute=22)
b = datetime.datetime(year=2010, month=2, day=6, hour=10, minute=20)
a - b # outputs datetime.timedelta 

datetime.timezone 

##################################################
# List
##################################################

'''
List
'''

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
# Strings and Text
##################################################


'''
String Operations
'''
# Count and Index
a = "I have had an apple on my desk before!"
print(a.count("e"))

z = ['atoms', 4, 'neutron', 6, 'proton', 4, 'electron', 4, 'electron', 'atoms']
print(z.count("4"))

# split
song = "this is a song"
wds = song.split()
print(wds)

# join
wds = ["red", "blue", "green"]
glue = ';'
s = glue.join(wds)
print(s)

ss = "Hello, World"
els = ss.count("l")

# ascii
# serialize data as ascii

# ord() converts a character to an integer unicode 
# chr() converts an integer unicode into a single character string

'''
Regular Expressions (re)

'''
# matching patterns 

# regular expressions
import re
search_string = "hello world"
pattern = "hello world"
match = re.match(pattern, search_string)
if match:
	print("regex matches")

import re
pattern = sys.argv[1]
search_string = sys.argv[2]
match = re.match(pattern, search_string)
if match:
	template = "'{}' matches pattern '{}'"
else:
	template = "'{}' does not match pattern '{}'"
print(template.format(search_string, pattern))

. # any character as long as not empty
[] # a set of characters as long as matches one of them
'hello world' matches pattern 'hel[lp]o world'

'hello 2 world' matches pattern 'hello [a-zA-Z0-9] world'

# \. matches . escaping 

'helllllo' matches pattern 'hel*o' # can be zero or more times 

'abcabcabc' matches pattern '(abc){3}'

'abccc' matches pattern 'abc{3}'

# Make repeated regular expressions efficient 


# specify multiple patterns for the separator 
# use the re.split() method 
line = 'asdf fjdk; afed, fjek,asdf, foo'

import re
re.split(r'[;,\s]\s*', line)

# matching test 
str.startswith()
str.endswith()
filename = 'spam.txt'
filename.endswith('.txt')

# Normally, fnmatch() matches patterns using the same case-sensitivity rules as the system’s underlying filesystem
import os 
filenames = os.listdir('.')
filenames
[name for name in filenames if name.endswith(('.c','.h'))]
[name for name in names if fnmatch(name, 'Dat*.csv')]

# replacing text 
text = 'yeah, but not, yeah'
text.replace('yeah', 'yep')

# for more complicated patterns, use the sub() function
# The first argument to sub() is the pattern to match and the second argument is the replacement pattern. 
# Backslashed digits such as \3 refer to capture group numbers in the pattern.
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
import re
re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)

# strip chracters from strings 
s = ' hello world \n'
s.strip()
# >>> t = '-----hello====='
# >>> t.lstrip('-')
# 'hello====='
# >>> t.strip('-=')
# 'hello'

text = 'Hello World'
format(text, '=>20s')
# '=========Hello World'
format(text, '*^20s')
# '****Hello World*****'

# combining and concatenating string 
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
' '.join(parts)

a = 'Is Chicago'
b = 'Not Chicago?'
print('{} {}'.format(a,b))  
# Is Chicago Not Chicago?

','.join(str(d) for d in data)
print(a, b, c, sep=':')


'''
format (interpolating values in strings)
'''
# format
s = '{name} has {n} messages'
s.format(name='Hello', n=37)

name = 'Guido'
n = 37
'%(name) has %(n) messages.' % vars()

# container lookup 
# we can access complex objects (indexes, variables of arrays, lists, etc.) from the format string
emails = ("a@example.com", "b@example.com")
message = {
    'subject': "You Have Mail!",
    'message': "Here's some mail for you!"
}
template = """
From: <{0[0]}>
To: <{0[1]}>
Subject: {message[subject]}
{message[message]}"""
print(template.format(emails, message=message))
# so 0[0] maps to emails[0], in the emails tuple

# object lookup
# We can pass arbitrary objects as parameters, and use the dot notation to look up attributes on those objects.
class EMail:
    def __init__(self, from_addr, to_addr, subject, message):
        self.from_addr = from_addr
        self.to_addr = to_addr
        self.subject = subject
        self.message = message
email = EMail("a@example.com", "b@example.com",
"You Have Mail!",
"Here's some mail for you!")

template = """
From: <{0.from_addr}>
To: <{0.to_addr}>
Subject: {0.subject}
{0.message}"""
print(template.format(email))

'{:10s} {:10d} {:10.2f}'.format('ACME', 100, 490.1).encode('ascii')

x = 1.23456
format(x, '0.2f')
format(x, '0.3f')
'value is {:0.3f}'.format(x)


print("Sub: ${0:0.2f} Tax: ${1:0.2f} Total: ${total:0.2f}".format(subtotal, tax, total=total))



'''
byte strings
'''
# byte strings support most of the operations for regular strings 
data = b'Hello World'
data[0:5]
data.startwith(b'Hello')

data = b'FOO:BAR,SPAM'
re.split(b'[:,]',data) # pattern as bytes





'''
datetime
'''
from datetime improt timedelta 
a = timedelta(days=2, hours=6)


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


'''
heapq
'''
# useful data structure for maintaining priority queue
# heapq module for finding nlargest or nsmallest 

import heapq 

nums = [1,2,3,-4]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

a = []
heappush(a, 1)
heappush(a, 3)
heappop(a)

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
# The .append, and .pop makes a lit usable as a stack or queue (using .append and .pop(0) to get LIFO behavior)
# But inserting and removing from left of list is costly 

# The class collections.deque is a thread-safe double-ended queue designed for fast
# inserting and removing from both ends. Provides constant time operations for inserting or removing items from beginning or end

from collections import deque
dq = deque(range(10), maxlen=10) # optional maxlen set the maximum number of items allowed 
dq.rotate(3) # takes items from the right end and prepends them to the left 

dq.append(e) # push the element onto the queue
dq.appendleft(4) # append to the beginning 
dq[0] # retrieve but not remove the element at the front
dq.popleft() # remove and return element at the front of the queue
dq.pop() # pops on the right 
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
# Tuple
##################################################

'''
Tuple
'''
# use tuple as data records 


# In ptyhon automatically packed into a tuple
julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")

# Slice Operator
singers = "Peter, Paul, and Mary"
print(singers[0:5])
print(singers[7:11])
fruit = "banana"
print(fruit[:3])

# Concatenation and Repitition
fruit = ["a", "b", "c"]
print([1,2]+[3,4])
print([0]*4)

# tuple assignment 
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)


# tuple unpacking
authors = [('a1','a2'),('b1','b2')]
for first_name, last_name in authors:
    print("first name:", first_name, "last name:", last_name)


# unpacking tuple as arguments
def add(x, y):
    return x + y
z = (5,4)
print(add(*z))

# using * to grab excess items
a,b, *rest = range(5) # rest will be assigned [2,3,4]

'''
named tuple
'''

# collections.namedtuple function is a factory that produces subclasses of tuple enhanced with field names and a class name 
from collections import namedtuple

Card = collections.namedtuple('Card', ['rank', 'suit'])

# Two parameters are required to create a named tuple: 
# - a class name and 
# - a list of field names, which can be given as an iterable of strings or as a single spacedelimited string.

# namedtuple is helpful for cases we need to name a fixed set of attributes
City = namedtuple('City', 'name country population coordinates')

BlackjackCard = namedtuple('BlackjackCard', 'rank, suit, hard, soft')
# subclass a namedtuple class 
class AceCard(BlackjackCard):
    __slots__ = ()
    # making __slots__() empty ensures that the subclass has no __dict__ and we can't add any new attributes

    # override the __new__() so we can construct instances with only two values 
    def __new__(self, rank, suit):
        return super().__new__(AceCard, 'A', suit, 1, 11)
    

# Data must be passed as positional arguments to the constructor (in contrast, the
# tuple constructor takes a single iterable).
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))

# can access fields by name or position
tokyo.population
tokyo[1]


from collections import namedtuple
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
def compute_cost(records):
    total = 0.0
    for rec in records: 
        s = Stock(*rec)
        total += s.shares * s.price
    return total 

# note on using dict, namedtuple or class for book-keeping 
# Use namedtuple for lightweight, immutable data containers before you need the
# flexibility of a full class.
# Move your bookkeeping code to use multiple helper classes when your internal state
# dictionaries get complicated






##################################################
# Dictionaries 
##################################################

'''
Hashable
'''

# All mapping types in the standard library use the basic dict in their implementation,
# so they share the limitation that the keys must be hashable (the values need not be
# hashable, only the keys).

# An object is hashable if it has a hash value which never changes during its lifetime (it
# needs a __hash__() method), and can be compared to other objects (it needs an
# __eq__() method). Hashable objects which compare equal must have the same hash
# value.

# User-defined types are hashable by default because their hash value is their id() and
# they all compare not equal. If an object implements a custom __eq__ that takes into
# account its internal state, it may be hashable only if all its attributes are immutable.


'''
Dictionary
'''
# building dictionaries 
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
a == b == c == d == e # True

b = {'one':1, 'two':2, 'three':3}


d.get(ke, default) # is an alternative to d[k] whenever a default value is more convenient than handling KeyError

# dict comprehensions
# build a dict instance by producing key:value pair from any iterable 
DIAL_CODES = [
    (81, 'Japan'),
    (7, 'Russia'),
    (55, 'Brazil'),
]

country_code = {country:code for code, country in DIAL_CODES}

{code:country.upper() for country, code in country_code.items()}

# empty dictionary is denoted {}
eng2sp = {}
eng2sp['one'] = 'uno'
eng2sp['two'] = 'dos'
eng2sp['three'] = 'tres'

# dictionary methods
# keys
# values
# items

# find keys in common 
a.keys() & b.keys()
# find (key, value) pairs in common 
a.items() & b.items()

# alter or filter dictionary contents
# make a new dictionary with certain keys removed 
c = {key:a[key] for key in a.keys() - {'z', 'w'}}

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
for akey in inventory.keys():
    print("Got key", akey, "which maps to value", inventory[akey])

ks = list(inventory.keys())
print(ks)

# copy and alias (given dictionary is mutable)
opposites = {'up':'down','right':'wrong'}
alias = opposites
print(alias is opposites) # return True, both point to the same 
alias['right'] = 'left'
print(opposites['right'])

# if you want to modify a dictionary and keep a copy of the original, use the dictionary copy method
acopy = opposites.copy()
acopy['right'] = 'left'

# accumulating multiple results in a dictionary
f = open('')


# accumulator pattern for dictionary
f = open('scarlet.txt', 'r')
txt = f.read()
letter_counts = {}
for c in txt:
    if c not in letter_counts:
        letter_counts[c] = 0
    letter_counts[c] +=1
for c in letter_counts.keys():
    print(c+": "+str(letter_counts[c])+" occurrences")


'''
Calculating with Dictionaries
'''
# to perform useful calculations on dictionary contents, you can invert the keys and values of the dictionary using zip()
prices = {
    'ACME': 45.23,
    'FB': 10.75
}
min_price = min(zip(prices.values(), prices.keys()))

# regular solution
min(prices, key=lambda k: prices[k]) # Returns 'FB'
min_value = prices[min(prices, key=lambda k: prices[k])]


'''
Missing Keys & Default Keys
'''
# The end result of this line
# my_dict.setdefault(key, []).append(new_value)

# is the same as running
for key, value in pairs: 
    if key not in my_dict:
        my_dict[key] = []
        my_dict[key].append(new_value)

# Using defaultdict leads to cleaner code 
d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)


'''
defaultdict
'''
# automatically initializes the first value so you can add items 

# if 'new-key' is not in dd, the expression dd['new-key'] does the following steps:
# 1. Calls list() to create a new list.
# 2. Inserts the list into dd using 'new-key' as key.
# 3. Returns a reference to that list.
d = defaultdict(list)
d['a'].append(1)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)

# counter
stats = defaultdict(int)
stats['my_counter'] +=1 


# The __missing__ Method
# Underlying the way mappings deal with missing keys is the aptly named __missing__
# method. This method is not defined in the base dict class, but dict is aware of it: if you
# subclass dict and provide a __missing__ method, the standard dict.__getitem__ will
# call it whenever a key is not found, instead of raising KeyError.

'''
OrderedDict
'''
# OrderedDict preserves the original insertion order of data when iterating 
# An OrderedDict can be particularly useful when you want to build a mapping that you
# may want to later serialize or encode into a different format. For example, if you want
# to precisely control the order of fields appearing in a JSON encoding, first building the
# data in an OrderedDict will do the trick

from collections import OrderedDict
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2

import json 
json.dumps(d)

# An OrderedDict internally maintains a doubly linked list that orders the keys according
# to insertion order. When a new item is first inserted, it is placed at the end of this list.
# Subsequent reassignment of an existing key doesn’t change the order




'''
sorting dictionary 
'''
# sort entries according to dictionary values 
# use itemgetter function

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))

from operator import itemgetter
l = [('h', 4), ('n', 6), ('o', 5), ('p', 1), ('t', 3), ('y', 2)]
l.sort(key=itemgetter(1))


# or use the lambda expression 
rows_by_fname = sorted(rows, key=lambda r: r['fname'])

print(rows_by_fname)
print(rows_by_uid)


'''
Dictionary List Comprehension
'''
# make a dictionary that is subset of another using list comprehension
p1 = {key:value for key, value in prices.items() if value > 100}
p1 = dict((key, value) for key, value in prices.items() if value > 200)



'''
Practical Implications of How Dict Works
'''
# keys must be hashable objects 
# An object is hashable if:
#  - support hash() function that returns the same value over the lifetime of the object
#  - support equality via an eq() method 
#  - if a == b then hash(a) == hash(b)


# dicts have significant memory overhead
# Because a dict uses a hash table internally, and hash tables must be sparse to work, they
# are not space efficient. For example, if you are handling a large quantity of records, it
# makes sense to store them in a list of tuples or named tuples instead of using a list of
# dictionaries in JSON style, with one dict per record. Replacing dicts with tuples reduces
# the memory usage in two ways: by removing the overhead of one hash table per record
# and by not storing the field names again with each record.


# Key search is very fast
# The dict implementation is an example of trading space for time: dictionaries have
# significant memory overhead, but they provide fast access regardless of the size of the
# dictionary—as long as it fits in memory. As Table 3-5 shows, when we increased the size
# of a dict from 1,000 to 10,000,000 elements, the time to search grew by a factor of 2.8,
# from 0.000163s to 0.000456s. The latter figure means we could search more than 2
# million keys per second in a dict with 10 million items.

'''
counters
'''
# determine the most frequently occurring items in the sequence 
words = ['look', 'into', 'this', 'look']


from collections import Counter
word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)

# update counters
word_counts.update(morewords)

# combine counts
c = a+b

'''
update
'''
a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }
merged = dict(b)
merged.update(a)

ct = collections.Counter('abracadabra')
ct # Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
ct.update('aaaaazzz')
ct # Counter({'a': 10, 'z': 3, 'b': 2, 'r': 2, 'c': 1, 'd': 1})



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



##################################################
# Datetime Module
##################################################

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


