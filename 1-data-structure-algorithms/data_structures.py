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
rount(2.5) # 2

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
# inserting and removing from both ends.

from collections import deque
dq = deque(range(10), maxlen=10) # optional maxlen set the maximum number if items allowed 
dq.rotate(3) # takes items from the right end and prepends them to the left 



##################################################
# Tuple
##################################################

'''
Tuple
'''

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

# named tuples 
# collections.namedtuple function is a factory that produces subclasses of tuple enhanced with field names and a class name 
from collections import namedtuple

Card = collections.namedtuple('Card', ['rank', 'suit'])

# Two parameters are required to create a named tuple: a class name and a list of
# field names, which can be given as an iterable of strings or as a single spacedelimited
# string.

City = namedtuple('City', 'name country population coordinates')

# Data must be passed as positional arguments to the constructor (in contrast, the
# tuple constructor takes a single iterable).
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))

# can access fields by name or position
tokyo.population
tokyo[1]



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


# dict comprehensions
# build a dict instance by producing key:value pair from any iterable 
DIAL_CODES = [
    (81, 'Japan'),
    (7, 'Russia'),
    (55, 'Brazil')
]

country_code = {country:code for code, country in DIAL_CODES}


# empty dictionary is denoted {}
eng2sp = {}
eng2sp['one'] = 'uno'
eng2sp['two'] = 'dos'
eng2sp['three'] = 'tres'

# dictionary methods
# keys
# values
# items

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
Missing Keys & Default Keys
'''
# The end result of this line
# my_dict.setdefault(key, []).append(new_value)

# is the same as running
# if key not in my_dict:
#     my_dict[key] = []
#     my_dict[key].append(new_value)


# defaultdict: taking on missing keys 
# given an empty defaultdict created as dd = defaultdict(list), 
# if 'new-key' is not in dd, the expression dd['new-key'] does the following steps:
# 1. Calls list() to create a new list.
# 2. Inserts the list into dd using 'new-key' as key.
# 3. Returns a reference to that list.

# The __missing__ Method
# Underlying the way mappings deal with missing keys is the aptly named __missing__
# method. This method is not defined in the base dict class, but dict is aware of it: if you
# subclass dict and provide a __missing__ method, the standard dict.__getitem__ will
# call it whenever a key is not found, instead of raising KeyError.


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


##################################################
# Sets
##################################################

from unicodedata import name 
{chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i),'')}

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



