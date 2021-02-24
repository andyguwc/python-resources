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
# An OrderedDict is a dictionary subclass that remembers the order in which its contents are added.
# Before Python 3.6 a regular dict did not track the insertion order, and iterating over it produced the values in order based on how the keys are stored in the hash table, which is in turn influenced by a random value to reduce collisions. In an OrderedDict, by contrast, the order in which the items are inserted is remembered and used when creating an iterator.

# OrderedDict preserves the original insertion order of data when iterating 
# An OrderedDict can be particularly useful when you want to build a mapping that you may want to later serialize or encode into a different format. 
# For example, if you want to precisely control the order of fields appearing in a JSON encoding, first building the data in an OrderedDict will do the trick

from collections import OrderedDict
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2

import json
json.dumps(d)

# An OrderedDict internally maintains a doubly linked list that orders the keys according
# to insertion order. When a new item is first inserted, it is placed at the end of this list.
# Subsequent reassignment of an existing key doesn’t change the order

from collections import OrderedDict
d = collections.OrderedDict(one=1, two=2, three=3)
d['four'] = 4
# >>> d 
# OrderedDict([('one', 1), ('two', 2), ('three', 3), ('four', 4)])



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
# similar to 
rows_by_uid = sorted(rows, key=itemgetter(2))


from operator import itemgetter
l = [('h', 4), ('n', 6), ('o', 5), ('p', 1), ('t', 3), ('y', 2)]
l.sort(key=itemgetter(1))


# or use the lambda expression 
rows_by_fname = sorted(rows, key=lambda r: r['fname'])

print(rows_by_fname)
print(rows_by_uid)

# sort the key, value pairs
xs = {'a': 4, 'c': 2, 'b': 3, 'd': 1}
sorted(xs.items())
# [('a', 4), ('b', 3), ('c', 2), ('d', 1)]

sorted(xs.items(), key=lambda x: x[1])
# [('d', 1), ('c', 2), ('b', 3), ('a', 4)]




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

'''
emulating case statements with dicts
'''
if cond == 'cond_a':
    handle_a()
elif cond == 'cond_b':
    handle_b()
else: 
    handle_default()

# can be achieved with below 
func_dict = {
    'cond_a': handle_a, 
    'cond_b': handle_b 
}

func_dict.get(cond, handle_default)()

'''
pretty print with json.dumps()
'''
import json 
json.dumps(mapping, indent=4, sort_keys=True)

# or use pprint 
import pprint 
pprint.pprint(mapping)


