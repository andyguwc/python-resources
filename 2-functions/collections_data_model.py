
##################################################
# Python Data Model & Special Methods
##################################################


# The Python interpreter invokes special methods to perform basic object operations,
# often triggered by special syntax
# the syntxax object[key] is supported by __getitem__ special method. my_collection[key] triggers my_collection.__getitem__(key)

# by implementing __len__ and __getitem__ the object behaves like a standard sequence with iteration and slicing 


# Normally, your code should not have many direct calls to special methods. Unless youare doing a lot of metaprogramming, you should be implementing special methods
# more often than invoking them explicitly. The only special method that is frequently called by user code directly is __init__, to invoke the initializer of the superclass in
# your own __init__ implementation.


# Type of special methods
# Attribute Access Attribute Access: These special methods implement what we see as object.attribute in an expression, object.attribute on the left-hand side of an assignment, and object.attribute in a del statement.
# Callables: This special method implements what we see as a function that is applied to arguments, much like the built-in len() function.
# Collections: These special methods implement the numerous features of collections. This involves methods such as sequence[index], mapping[key], and some_set|another_set.
# Numbers: These special methods provide arithmetic operators and comparison operators. We can use these methods to expand the domain of numbers that Python works with.
# Contexts: There are two special methods we'll use to implement a context manager that works with the with statement.
# Iterators: There are special methods that define an iterator. This isn't essential since generator functions handle this feature so elegantly. However, we'll take a look at how we can design our own iterators.



##################################################
# Callables 
##################################################

# callable object inclues function definition created with the def statement
# also any class with a __call__() method 
# >>> abs(3)
# 3
# >>> isinstance(abs, collections.abc.Callable)
# True

# example callable 
# define as a subclass of abc.Callable
# then define the __call__ method 
# create an instance of the class 

import collections.abc 
class Power(collections.abc.Callable):
    def __call__(self, x, n):
        p = 1
        for i in range(n):
            p *=x 
        return p 

power = Power() # power became like a function
pow(2, 0)


# another example
# martingale - double up on each loss strategy 

class BettingMartingale(BettingStrategy):
    def __init__(self):
        self._win = 0 
        self._loss = 0
        self.stage = 1
    
    @property 
    def win(self):
        return self._win 
    
    @win.setter 
    def win(self, value):
        self._win = value 
        self.stage = 1 
    
    @property 
    def loss(self):
        return self._loss 
    
    @loss.setter 
    def loss(self, value):
        self._loss = value 
        self.stage *= 2 
    
    def __call__(self):
        return self.stage 

# >>> bet= BettingMartingale()
# >>> bet()
# 1
# >>> bet.win += 1
# >>> bet()
# 1
# >>> bet.loss += 1
# >>> bet()
# 2



'''
LRU Memoization Decorator
'''
# The requests are tracked in the cache, and the size is limited. The idea behind an LRU cache is that
# the most recently made requests are kept and the least recently made requests are
# quietly deleted

from functools import lru_cache
@lru_cache(None)
def pow(x, n):
    if n ==0: return 1 
    elif n%2 == 1:
        return pow(x, n-1)*x
    else:
        t = pow(x, n//2)
        return t*t 



'''
callable API
'''
# the idea behind a callable object is to have an API that's focused on a single method

# The first is the API of the object. If there's a reason for the object to have a
# function-like interface, then a callable object is a sensible design approach.
# Using collections.abc.Callable assures that the callable API is built
# correctly, and it informs anyone reading the code what the intent of the class is.

# The second is the statefulness of the function. Ordinary functions in Python
# have no hysteresis—there's no saved state. A callable object, however, can
# easily save a state. The memoization design pattern makes good use of
# stateful callable objects


##################################################
# Context
##################################################

# almost all contexts are associated with basic I/O operations
# locking and database transactions (acquire and release an external lock)


''' 
context management protocol
'''
# To make an object compatible with the with statement, implement __enter__() and __exit__()

from socket import socket, AF_INET, SOCK_STREAM

class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = AF_INET
        self.type = SOCK_STREAM
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Aready Connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock
    
    def __exit__(self, exc_ty, exc_val, tb):
        self.sock.close()
        self.sock = None
    
# use case 
conn = LazyConnection(('www.python.org', 80))
# Connection closed
with conn as s:
# conn.__enter__() executes: connection open
    s.send(b'GET /index.html HTTP/1.0\r\n')
    s.send(b'Host: www.python.org\r\n')
# conn.__exit__() executes: connection closed
    

# Exceptions that arise in a block will be passed to the __exit__() method of the
# context manager.

# The __exit__() method can do one of the following two things with the
# exception information:

# • Silence the exception by returning some True value.
# • Allow the exception to rise normally by returning any other False value.
# Returning nothing is the same as returning None, which is a False value; this
# allows the exception to propagate.




##################################################
# Collections Protocols
##################################################


'''
fundamental base classes
'''
# that requires a single special method 

# The Container base class requires the concrete class to implement the __
# contains__() method. This special method implements the in operator.

# The Iterable base class requires __iter__(). This special method is used
# by the for statement and the generator expressions as well as the iter()
# function.

# The Sized base class requires __len__(). This method is used by the len()
# function. It's also prudent to implement __bool__(), but it's not required by
# this abstract base class.

# The Hashable base class requires __hash__(). This is used by the hash()
# function. If this is implemented, it means that the object is immutable.

'''
higher level composite structures
'''

# The Sequence and MutableSequence classes build on the basics and fold in
# methods such as index(), count(), reverse(), extend(), and remove().
# The Mapping and MutableMapping classes fold in methods such as keys(),
# items(), values(), and get(), among others.
# The Set and MutableSet classes fold in comparison and arithmetic operators
# to perform set operation


''' 
Container
'''

# iteration is often implicit. 
# If a collection has no contain method, the iteration does a sequential scan

# memebership testing using in and not in 
__contains__(item)

class SortedSet:
    def __init__(self, items=None):
        self._items = sorted(items) if items is not None else []

    def __contains__(self, item):
        return item in self._items 

# if it's sorted already then faster implementation
def __contains__(self, item):
    index = bisect_left(self._items, item)
    return (index != len(self._items) and (self._items[index] == item))


# another example modify the meaning of contains
def __contains__(self, rank):
    returna any(c.rank==rank for c in hand.cards)

# so instead of doing
any(c.rank == 'A' for c in hand.cards)
# we can do 
'A' in hand.cards


'''
Size
'''
# determine number of elements with len(s)
def __len__(self):
    return len(self._items) # calling len on the underlying list 


'''
Iterable
'''
# iterable protocol which returns an iterator with __iter__()
# can produce iterator with iter(s)
# iterable can be used in the for loop
for item in iterable:
    do_something(item)

def __iter__(self):
    return iter(self._items)
    # or use below

def __iter__(self):
    for item in self._items:
        yield item

# if __iter__ is not implemented, but __getitem__ is implemented, Python creates
# an interator that attempts to fetch items in order, starting from index 0
# if failing, raises TypeError 
# because all python sequences implement __getitem__, any python sequence is iterable 

class Foo:
    def __iter__(self):
        pass 
    
from collections import abc 
issubclass(Foo, abc.Iterable) # True
f = Foo()
isinstance(f, abc.Iterable) # True 


'''
Sequence
'''

# retrieve elements by index 
item = seq[index] # no special methods

# retrieve slices by slicing 
item = seq[start:stop]

# further more 
# return first matching index of item or raise error 
index = seq.index(item)
# count items
num = seq.count(item)

# concatenation with + operator and repetition with * operator 

# implies container, sized, and iterable 
# index can be a slice 
def __getitem__(self, index):
    result = self._items[index]
    return SortedSet(result) if isinstance(index, slice) else result 


class Explore(list):
    def __getitem__(self, index):
        print(index, index.indices(len(self)))
        return super().__getitem__(index)



# example object - collection of cards 
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.rank]
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        # because __getitem__ delegates to the [] operator of self._cards
        # our deck automatically supports slicing
        return self._cards[position]

deck = FrenchDeck()
len(deck)
deck[1] # calls __getitem__ method

from random import choice
choice(deck) # picks a random card


# iteration is often implicit, the in operator does a sequential scan if no __contains__ method implemented
Card('Q', 'hearts') in deck

# implement customized sorting 
# first define a value function for each card 
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

# now list in order of increasing rank 
for card in sorted(deck, key=spades_high):
    print(card)

# reversed sequence
r = reversed(seq) # special method __reversed__() fallback to __getitem__() and __len__()

# overwriting index
def index(self, item):
    index = bisect_left(self._items, item)
    if (index != len(self._items)) and (self._items[index] == item):
        return index 
    raise ValueError("{} not found".format(repr(item)))

# concatenationg + 
from itertools import chain 

def __add__(self, rhs):
    return SortedSet(chain(self._items, rhs._items))

# repetition with * operator
def __mul__(self, rhs):
    return self if rhs >0 else SortedSet()


'''
__bool__() method
'''

# By default, instances of user-defined classes are considered truthy, unless either
# __bool__ or __len__ is implemented. Basically, bool(x) calls x.__bool__() and uses
# the result. 
# If __bool__ is not implemented, Python tries to invoke x.__len__(), and if
# that returns zero, bool returns False. Otherwise bool returns True.
# Our implementation of __bool__ is conceptually simple: it returns False if the magnitude
# of the vector is zero, True otherwise. We convert the magnitude to a Boolean
# using bool(abs(self)) because __bool__ is expected to return a boolean.

# under the hood, this uses __bool__() method
# An empty collection should be equivalent to False. A nonempty collection can return True.
if some_object:
    process(some_object)


# If we're wrapping a list, we might have something as shown in the following code snippet:
def __bool__( self ):
  return bool( self._cards )
# This delegates the Boolean function to the internal _cards collection.
# If we're extending a list, we might have something as follows:
def __bool__( self ):
    return super().__bool__( self )
# This delegates to the superclass definition of the __bool__() function.

'''
Example Implementation
'''

class Vector:
    def __init__(selflt, x= 0, y=0):
        self.x=x
        self.y=y
    
    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)
    
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


'''
Extending a colleciton
'''
# upgrade a Counter to add mean and standard deviation 
# lazy evaluation as properties
from collections import Counter 
class StatsCounter(Counter):
    @property
    def mean(self):
        sum0 = sum(v for k,v in self.items())
        sum1 = sum(v*v for k, v in self.items())
        return sum1/sum0
    
    @property
    def stdev(self):
        sum0= sum( v for k,v in self.items() )
        sum1= sum( k*v for k,v in self.items() )
        sum2= sum( k*k*v for k,v in self.items() )
        return math.sqrt( sum0*sum2-sum1*sum1 )/sum0

# eager evaluations
# class that calculates statistical measures
class StatsList(list):
    def __init__(self):
        self.sum0 = 0
        self.sum1 = 0.0
        self.sum2 = 0.0
        super().__init__()
        for x in self:
            self._new(x)
        
    def _new(self, value):
        self.sum0 += 1
        self.sum1 += value
        self.sum2 += value * value
    
    def _rmv(self, value):
        self.sum0 -= 1
        self.sum1 -= value
        self.sum2 -= value * value

    def insert(self, index, value):
        super().insert(index, value)
        self._new(value)

    def pop(self, index):
        value = super().pop(index)
        self._rmv(value)
        return value


'''
Wrapping a colleciton
'''
class StatsList:
    def __init__(self):
        self._list = list()
        self.sum0 = 0
        self.sum1 = 0
        self.sum2 = 0
    
    def append(self, value):
        self._list.append(value)
        self.sum0 += 1
        self.sum1 += value
        self.sum2 += value * value
    
    def __getitem__(self, index):
        return self._list.__getitem__(index)
    
    @property
    def mean(self):
        return self.sum1 / self.sum0

    def stdev(self):
        return math.sqrt(
            self.sum0*self.sum2 - self.sum1*self.sum1
        ) / self.sum0

    # make this an iterable
    # create generator functions
    def __iter__(self):
        return iter(self._list)


##################################################
# Design Considerations
##################################################

When working with containers and collections, we have a multistep design strategy:

1. Consider the built-in versions of sequence, mapping, and set.
2. Consider the library extensions in the collection module, as well as extras
such as heapq, bisect, and array.
3. Consider a composition of existing class definitions. In many cases, a list of
tuple objects or a dict of lists provides the needed features.
4. Consider extending one of the earlier mentioned classes to provide
additional methods or attributes.
5. Consider wrapping an existing structure as another way to provide
additional methods or attributes.
6. Finally, consider a novel data structure. Generally, there is a lot of careful
analysis available. Start with Wikipedia articles such as this
one: http://en.wikipedia.org/wiki/List_of_data_structures.

Once the design alternatives have been identified, there are two parts of the
evaluation left:
How well the interface fits with the problem domain. This is a relatively
subjective determination.
How well the data structure