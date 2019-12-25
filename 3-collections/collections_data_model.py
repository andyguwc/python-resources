
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
# Collections
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

# iteraration is often implifict. If a collection has no contain method, the iteration does a sequential scan


# memebership testing using in and not in 
__contains__(item)

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
Iterable vs.Iterator
'''

# python obtain iterators from iterables 

# iterables have an __iter__ method that instantiates a new iterator every time.
# Iterators implement a __next__ method that returns individual items, and an __iter__
# method that returns self.

s = 'ABC' # str 'ABC' is the iterable here
for char in s: # iterator behind the scenes
    print(char)

s = 'ABC'
it = iter(s) # build an iterator it from the iterable
while True: 
    try:
        print(next(it)) # call next on the iterator to obtain the next item 
    except StopIteration:
        del it
        break 

# classic iterator 
# iterator pattern
import re 
import reprlib 

RE_WORD = re.compile('\w+')
class Sentence: 
    def __init__(self, text):
        self.text = text
        self.words = RE_WORLD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)    
    
    # Sentence is iterable because it implements the __iter__ special method
    # which builds and returns a SentenceIterator
    def __iter__(self):
        return SentenceIterator(self.words)

class SentenceIterator:
    def __init__(self, words):
        self.words = words # holds a reference to the list of words
        self.index = 0 
    
    def __next__(self): 
        try:
            word = self.words[self.index]
        except IndexError: # if no word at self.index, raise StopIteration
            raise StopIteration()
        self.index+=1
        return word 
    
    def __iter__(self): #implement the self.__iter__
        return self 


# alternative implementation
# use the yield (generator function) to replace the SentenceIterator class 
import re 
import reprlib 

RE_WORD = re.compile('\w+')


class Sentence: 
    def __init__(self, text):
        self.text = text 
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    
    def __iter__(self):
        for word in self.words: 
            yield word 
        return 


# another example 
# loop through each of the words in a string and output them with the first letter capitalized 
class CapitalIterable:
    def __init__(self, string):
        self.string = string 

    def __iter__(self):
        return CapitalIterator(self.string)
    
class CapitalIterator:
    def __init__(self, string):
        self.words = [w.capitalize() for w in string.split()]
        self.index = 0 
    
    def __next__(self):
        if self.index = len(self.words):
            raise StopIteration()
    
        word = self.words[self.index]
        self.index += 1
        return word 
    
    def __iter__(self):
        return self 

# example utilizing the iterable 
iterable = CapitalIterable('the quick brown fox')
iterator = iter(iterable)
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break 


'''
Sequence
'''
# implies container, sized, and iterable 

def __getitem__(self, index):
    result = self._items[index]
    return SortedSet(result) if isinstance(index, slice) else result 


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

# retrieve elements by index 
item = seq[index] # no special methods
# find items by value
index = seq.index(item)
# count items
num = seq.count(item)
# reversed sequence
r = reversed(seq)

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


'''
__hash__() method
'''
# The built-in hash() function invokes the __hash__() method of a given object.
# This hash is a calculation which reduces a (potentially complex) value to a small
# integer value.

# The hash() function (and the associated __hash__() method) is used to create a
# small integer key that is used to work with collections such as set, frozenset, and
# dict. These collections use the hash value of an immutable object to rapidly locate
# the object in the collection.

# mutable objects should never return a hash value 

# immutable objects overrride both __eq__ and __hash__

def __eq__(self, other):
    return self.suit == other.suit and self.rank == other.rank 

def __hash__(self):
    return hash(self.suit)^hash(self.rank)

# mutable objects define __eq__() but set __hash__ to None
def __eq__(self, other):
    return self.suit == other.suit and self.rank == other.rank 
__hash__ = None 


# mixed class comparison example 
# full implementation of a class with comparisons

class Hand:
    def __init__(self, dealer_card, *cards):
        self.dealer_card = dealer_card
        self.cards = list(cards)
    
    def __str__(self):
        return ", ".join(map(str, self.cards))

    def __repr__(self):
        return "{__class__.__name__}({dealer_card!r}, {_cards_str})".format(
            __class__=self.__class__,
            _cards_str_=", ".join(map(repr, self.cards)),
            **self.__dict__)
    
    def __eq__(self, other):
    # mixed class comparison check for instance type
        if isinstance(other, int):
            return self.total() == other 
        
        try: 
            return (self.cards == other.cards
                and self.dealer_card == other.dealer_card)
        except AttributeError:
            return NotImplemented 
    
    def __lt__(self, other):
        if isinstance(other, int):
            return self.total() < other 
        try:
            return self.total() < other.total()
        except AttributeError:
            return NotImplemented 
    
    def __le__(self, other):
        if isinstance(other, int):
            return self.total() <= other 
        try:
            return self.total() <= other.total()
        except AttributeError:
            return NotImplemented 
    
    __hash__ = None 
    def total(self):
        pass 

    

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
extending a colleciton
'''
# upgrade a Counter to add mean and standard deviation 
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

