#################################################
#  Partial (functools)
##################################################
# The primary tool supplied by the functools module is the class partial, which can be used to “wrap” a callable object with default arguments. The resulting object is itself callable and can be treated as though it is the original function. It takes all of the same arguments as the original, and can be invoked with extra positional or named arguments as well. A partial can be used instead of a lambda to provide default arguments to a function, while leaving some arguments unspecified.

# allows partial application of a function 
# using partial to use a two-argument function where a one-argument callable is required
from operator import mul 
from functools import partial 
triple = partial(mul, 3) # binding the first positional argument to 3 
triple(7)
list(map(triple, range(10)))

# Acquiring Function Properties
# The partial object does not have __name__ or __doc__ attributes by default, and without those attributes, decorated functions are more difficult to debug. Using update_wrapper(), copies or adds attributes from the original function to the partial object.

functools.update_wrapper(triple, mul)


#################################################
#  total_order (functools)
##################################################

# The rich comparison API is designed to allow classes with complex comparisons to implement each test in the most efficient way possible. However, for classes where comparison is relatively simple, there is no point in manually creating each of the rich comparison methods. The total_ordering() class decorator takes a class that provides some of the methods, and adds the rest of them.


import functools

@functools.total_ordering
class MyObject:

    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        return self.val == other.val

    def __gt__(self, other):
        return self.val > other.val

import inspect
print('Methods:\n')
pprint(inspect.getmembers(MyObject, inspect.isfunction))
[('__eq__', <function MyObject.__eq__ at 0x10139a488>),
 ('__ge__', <function _ge_from_gt at 0x1012e2510>),
 ('__gt__', <function MyObject.__gt__ at 0x10139a510>),
 ('__init__', <function MyObject.__init__ at 0x10139a400>),
 ('__le__', <function _le_from_gt at 0x1012e2598>),
 ('__lt__', <function _lt_from_gt at 0x1012e2488>)]


#################################################
#  caching (functools)
##################################################

# https://pymotw.com/3/functools/index.html
# The lru_cache() decorator wraps a function in a least-recently-used cache. Arguments to the function are used to build a hash key, which is then mapped to the result. Subsequent calls with the same arguments will fetch the value from the cache instead of calling the function. The decorator also adds methods to the function to examine the state of the cache (cache_info()) and empty the cache (cache_clear()).

# The keys for the cache managed by lru_cache() must be hashable, so all of the arguments to the function wrapped with the cache lookup must be hashable.


import functools

@functools.total_ordering
def expensive(a, b):
    print('expensive({}, {})'.format(a, b))
    return a * b

MAX = 2

print('First set of calls:')
for i in range(MAX):
    for j in range(MAX):
        expensive(i, j)
print(expensive.cache_info())

print('\nSecond set of calls:')
for i in range(MAX + 1):
    for j in range(MAX + 1):
        expensive(i, j)
print(expensive.cache_info())

print('\nClearing cache:')
expensive.cache_clear()
print(expensive.cache_info())

print('\nThird set of calls:')
for i in range(MAX):
    for j in range(MAX):
        expensive(i, j)
print(expensive.cache_info())

# To prevent the cache from growing without bounds in a long-running process, it is given a maximum size. The default is 128 entries, but that can be changed for each cache using the maxsize argument.


#################################################
# Operators
##################################################

# One of the most unusual features of the operator module is the concept of getters. These are callable objects constructed at runtime to retrieve attributes of objects or contents from sequences. Getters are especially useful when working with iterators or generator sequences, where they are intended to incur less overhead than a lambda or Python function.


'''
reduce (functools)
'''
# the operator module 
# provide arithmetic operator as a function 
from functools import reduce 
from operator import mul 

def fact(n):
    return reduce(mul, range(1, n+1))
    # same as 
    # return reduce(lambda a, b: a*b, range(1, n+1))

'''
itemgetter, attrgetter
'''
# https://pymotw.com/3/operator/index.html

# using itemgetter and attrgetter to build custom functions
# essentially itemgetter(1) does the same as lambda fields: fields[1]: 
# create a function that, given a collection, returns the item at index 1.
metro_data = [
    ('Tokyo', 'JP', 36.933, (35.682, 130.212)),
    ('Mexico City', 'MX', 20.142, (19.682, -30.212))
]

from operator import itemgetter
for city in sorted(metro_data, key=itemgetter(1)):
    print(city)

# passing multiple index arguments, the function will return tuples
cc_name = itemgetter(1,0)
for city in metro_data:
    print(cc_name(city))

# A sibling of itemgetter is attrgetter, which creates functions to extract object attributes
# by name. If you pass attrgetter several attribute names as arguments, it also
# returns a tuple of values. In addition, if any argument name contains a . (dot), attrgetter navigates through nested objects to retrieve the attribute.
from collections import namedtuple
LatLong = namedtuple('LatLong', 'lat long') # using namedtuple to define LatLong
Metropolis = namedtuple('Metropolis', 'name cc pop coord') 
metro_areas = [Metropolis(name, cc, pop,LatLong(lat, long))
    for name, cc, pop, (lat, long) in metro_data]
metro_areas[0] # a named tuple Metropolis(name='Tokyo', cc='JP', pop=36.933, coord=LatLong(lat=35.689722,long=139.691667))

from operator import attrgetter
name_lat = attrgetter('name', 'coord.lat') # get nested attribute with coord.lat
for city in sorted(metro_areas, key=attrgetter('coord.lat')):
    print(name_lat(city))



