
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

# callable is an object that can be called using the () operator
# to check if an object is callable, use the built-in function callable(print) -> true
# callables include
# built in functions, method, user-defined functions, methods, classes, class istances if it implements __call__ method, generators


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
# implements the __call__ method to let the class instance become a callable

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
# High Order Functions
##################################################
# A function that takes a function as a parameter and/or returns a function as its return value

# map
# returns an iterator that calculates the function applies to each element of the iterables

# iterables is a variable number of iterable objects, and func is a function that takes as many arguments as there are iterable objects passed to iterables
map(func, *iterables)
list(map(lambda x: x**2, [1,2,3])) # [1, 4, 9]


def add(x, y):
    return x + y

l1 = [1,2,3]
l2 = [10,20,30]
list(map(add, l1, l2)) # [11, 22, 33]


# filter
# filter will return an iterator that contains all the elements of the iterable for which the function called on it is truthy
filter(func, iterable) # iterable is a single iterable, and func is a function that takes a single argument.
l = [0,1,2,3,4]

def is_even(n):
    return n %2 == 0

list(filter(is_even, l)) # [0, 2, 4]


# list comprehension alternative to map
# return one iterable
zip(*iterables)

zip([1,2,3,4], [10, 20, 30, 40]) # [(1, 10), (2, 20), (3, 30), (4, 40)]
# with uneven length, it stops at the shortest one
zip([1,2,3,4,5], [10,20,30]) # [(1, 10), (2, 20), (3, 30)]

# l1 = [1,2,3], l2 = [10,20,30]
list(map(lambda x, y: x+y, l1, l2))
[x + y for x, y in zip(l1, l2)] # [11,22,33]

# list comprehension alternative to filter

[x for x in l if x % 2 == 0]

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
# Equality 
##################################################

'''
equality and inequality
'''

# implement equality and inequality
# without implementing this, two objects with the same component can be different 
def __eq__(self, rhs):
    if not isinstance(rhs, SortedSet):
        return NotImplemented # return NotImplemented object instead of raising the error
    return self._items == rhs._items

# can overwrite the inequality method 
def __ne__(self, rhs):
    if not isinstance(rhs, SortedSet):
        return NotImplemented
    return self._items != rhs._items

SortedSet([1,2,3]) == SortedSet([1,2,3]) # return False 
SortedSet([1,2,3]) is SortedSet([1,2,3]) # return False 


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank
    
    def __hash__(self):
        return hash(self.suit) ^ hash(self.rank)


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
Set
'''
__contains__
__iter__
__len__

__le__() # <= subset
__ge__() # >= superset

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
# immutable object can return a hash value so the object can be used as the key in a dictionary or a member of a set

# immutable objects overrride both __eq__ and __hash__

def __eq__(self, other):
    return self.suit == other.suit and self.rank == other.rank 

def __hash__(self):
    return hash(self.suit)^hash(self.rank)

# mutable objects define __eq__() but set __hash__ to None
def __eq__(self, other):
    return self.suit == other.suit and self.rank == other.rank 
__hash__ = None 

    