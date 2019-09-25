
##################################################
# Python Data Model & Special Methods
##################################################


# The Python interpreter invokes special methods to perform basic object operations,
# often triggered by special syntax
# the syntxax object[key] is supported by __getitem__ special method. my_collection[key] triggers my_collection.__getitem__(key)

# by implementing __len__ and __getitem__ the object behaves like a standard sequence with iteration and slicing 


# Normally, your code should not have many direct calls to special methods. Unless you
# are doing a lot of metaprogramming, you should be implementing special methods
# more often than invoking them explicitly. The only special method that is frequently
# called by user code directly is __init__, to invoke the initializer of the superclass in
# your own __init__ implementation.


##################################################
# Example Implementation 
##################################################

class Vector:
    def __init__(self, x= 0, y=0):
        self.x=x
        self.y=y
    
    def __repr__(self):
        return 'Vector(%r, %r') % (self.x, self.y)
    
    def __abs__(self):
        return hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x+other.x
        y = self.y+other.y 
        return Vector(x, y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

# By default, instances of user-defined classes are considered truthy, unless either
# __bool__ or __len__ is implemented. Basically, bool(x) calls x.__bool__() and uses
# the result. 
# If __bool__ is not implemented, Python tries to invoke x.__len__(), and if
# that returns zero, bool returns False. Otherwise bool returns True.
# Our implementation of __bool__ is conceptually simple: it returns False if the magnitude
# of the vector is zero, True otherwise. We convert the magnitude to a Boolean
# using bool(abs(self)) because __bool__ is expected to return a boolean.



##################################################
# Collections
##################################################

''' 
Container
'''

# iteraration is often implifict. If a collection has no contain method, the iteration does a sequential scan


# memebership testing using in and not in 
__contains__(item)

def __contains__(self, item):
    return item in self._items 

# if it's sorted already then faster implementation
def __contains__(self, item):
    index = bisect_left(self._items, item)
    return (index != len(self._items) and (self._items[index] == item))

'''
Size
'''
# determine number of elements with len(s)
__len__()
def __len__(self):
    return len(self._items) # calling len on the underlying list 

'''
Iterable
'''
# can produce iterator with iter(s)
for item in iterable:
    do_something(item)

__iter__()
def __iter__(self):
    return iter(self._items)
    # or use below
    # for item in self._items:
    #   yield item

'''
Sequence
'''
# implies container, sized, and iterable 

def __getitem__(self, index):
    result = self._items[index]
    return SortedSet(result) if isinstance(index, slice) else result 


# retrieve elements by index 
item = seq[index] # no special methods
# find items by value
index = seq.index(item)
# count items
num = seq.count(item)
# reversed sequence
r = reversed(seq)


# implement equality and inequality
def __eq__(self, rhs):
    if not isinstance(rhs, SortedSet):
        return NotImplemented
    return self._items == rhs._items
# inequality
__ne__(self, rhs)

SortedSet([1,2,3]) == SortedSet([1,2,3]) # return False 
SortedSet([1,2,3]) is SortedSet([1,2,3]) # return False 

# index is automatic for any subclasses of collections.abc
# define SortedSet as class from Sequence
from collections.abc import Sequence
class SortedSet(Sequence):
    pass 
# count is also automatically implemented 

# overwriting index
def index(self, item):
    index = bisect_left(self._items, item)
    if (index != len(self._items)) and (self._items[index] == item):
        return index 
    raise ValueError("{} not found".format(repr(item)))

# concatenationg + 
def __add__(self, rhs):
    return SortedSet(chain(self._items, rhs._items))

# repetition with * operator
def __mul__(self, rhs):
    return self if rhs >0 else SortedSet()
    

'''
Set
'''
__contains__
__iter__
__len__

__le__() # subset
__ge__() # superset

# mutable set 
# implement add() and discard()