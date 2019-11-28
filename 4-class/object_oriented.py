##################################################
# Constructor / Initialization
##################################################


# what is the data you want to deal with 
# what will one instance of the class represent
# what information should each instance have as instance variables
# what instance methods should each instance have 


'''
Constructor
'''
# contructor 
class Point:
    """ Point class for representing and manipulating x, y coordinates"""
    def __init__(self):
        """Create a point at the origin"""
        self.x = 0
        self.y = 0
    
p = Point() # instantiate an object of type Point - i.e. a combination of making a new object and get settings initialized for the default settings
q = Point() # make a second point

# adding parameters to the Constructor
class Point:
    """ Point class for representing and manipulating x,y coordinates. """
    def __init__(self, initX, initY):
        self.x = initX # assigned to state of the object, in the instance variables x and y
        self.y = initY
p = Point(7,6)

# all methods defined in a class that operate on objects of that class will have self as their first parameter. 
# Again, this serves as a reference to the object itself which in turn gives access to the state data inside the object.
class Point:
    """ Point class for representing and manipulating x,y coordinates. """
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def distanceFromOrigin(self):
        return ((self.x**2)+(self.y**2))**0.5

    # an alternative is to define the function outside the object as distance(point1, point2)
    def distance(self, point2):
        xdiff = point2.getX()-self.getX()
        ydiff = point2.getY()-self.getY()

        dist = math.sqrt(xdiff**2 + ydiff**2)
        return dist

p = Point(7,6)
print(p.getX())
print(p.getY())


'''
Instances
'''

# instances as return values

class Point: 
    # ...
    # return the midpoint 
    def halfway(self, target):
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)

# sorting list of instances

class Fruit:
    def __init__(self, name, price):
        self.name = name
        self.price = price

L = [Fruit("Cherry", 10), Fruit("Apple",5), Fruit("Blueberry", 20)]
for f in sorted(L, key=lambda x: x.price):
    print(f.name)


'''
Instance Vairables vs. Class Variables
'''

# Attributes
# Each instance can have attributes, sometimes called instance variables
# Classes have associated methods, which are just a special kind of function

# in shipping.py
class ShippingContainer:
    new_serial = 1336 # class attributes
    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer.new_serial # global/module scope
        ShippingContainer.new_serial += 1

# from shipping import *
# c1 = ShippingContainer('MAE','tools')

# Calling class attributes
class Point:
    """ Point class for representing and manipulating x,y coordinates. """
    printed_rep = "*" # this is a class variable the same across all instances 
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def graph(self):

print(Point.printed_rep) # calling class attribute directly




'''
__init__() 
'''

# Each Python class definition has an implicit superclass: object. It's a very
# simple class definition that does almost nothing. 
# We can see below that a class is an object of the class named type and the base class is the class named object

# >>> class X:
# ...     pass
# ... 
# >>> X.__class__
# <class 'type'>
# >>> X.__class__.__base__
# <class 'object'>
# >>> 

# We can always add attributes to an object that's a subclass of the foundational base class, object
class Rectangle:
    def area( self ):
        return self.length * self.width

# r.length, r.width = 13, 8 # sometimes we don't need to set all of the attributes in the __init__() method

# implement __init__() in a superclass

# polymorphic design 
# each subclass provides a unique implementation of the _points() method 
class Card:
    # initializer at the superclass level 
    def __init__(self, rank, suit):
        self.rank = rank  
        self.suit = suit
        self.hard, self.soft = self._points()

class NumberCard(Card): 
    def _points(self):
        return int(self.rank), int(self.rank)

class AceCard(Card):
    def _points(self):
        return 1, 11

class FaceCard(Card):
    def _points(self):
        return 10, 10


#  different intialization function 

class Card:
    def __init__(self, rank, suit, hard, soft):
        self.rank= rank
        self.suit= suit
        self.hard= hard
        self.soft= soft
class NumberCard(Card):
    def __init__(self, rank, suit):
        super().__init__(str(rank), suit, rank, rank)
class AceCard(Card):
    def __init__(self, rank, suit):
        super().__init__("A", suit, 1, 11)
class FaceCard(Card):
    def __init__(self, rank, suit):
        super().__init__({ 11: 'J', 12: 'Q', 13: 'K' }[rank], suit, 10, 10)


# strategy objects (to implement an algorithm or decision) don't have __init__()



'''
Leveraging __init__() via a factory function
'''

# two approaches to factories 
#  - define a function that creates objects of the required classes 
#  - define a class that has methods of creating objects 

# If we have a factory class, we can add subclasses to the factory class when extending the target class hierarchy. This gives us
# polymorphic factory classes; the different factory class definitions have the same method signatures and can be used interchangeably.

# example factory function for Card subclasses 
# This function builds a Card class from a numeric rank number and a suit object


def card(rank, suit):
    if rank == 1: 
        return AceCard('A', suit)
    elif 2 <= rank < 11: 
        return NumberCard(str(rank), suit)
    elif 11 <= rank <14:
        # use mapping to simplify many elif mappings
        name = { 11: 'J', 12: 'Q', 13: 'K' }[rank]
        return FaceCard(name, suit)
    else: 
        # note never use a catchall else, leave the else to raise exceptions
        raise Exception("rank out of range")
# example applying the factory function to build a deck 
deck = [card(rank, suit)
        for rank in range(1,14)
            for suit in (Club, Diamond, Heart, Spade)]


'''
using keyword argument values during initialization
'''
class Player:
    def __init__(self, **kw):
        self.__dict__.update(kw)        

# The disadvantage of this is that we have obscure instance variables that aren't formally documented via a subclass definition


'''
initialization with type validation
'''
class ValidPlayer:
    def __init__( self, table, bet_strategy, game_strategy ):
        assert isinstance( table, Table )
        assert isinstance( bet_strategy, BettingStrategy )
        assert isinstance( game_strategy, GameStrategy )
        self.bet_strategy = bet_strategy
        self.game_strategy = game_strategy
        self.table= table


'''
Composite Objects
'''
# A collection of objects
#  - Wrap: This design pattern is an existing collection definition. This might be an example of the Facade design pattern.
#  - Extend: This design pattern is an existing collection class. This is ordinary subclass definition.
#  - Invent: This is designed from scratch. We'll look at this in Chapter 6, Creating Containers and Collections.

# Wrapping a collection class (Facade design pattern)
# contains an internal collection (list object), the pop() method delegates to the wrapped list object
# Generally, a Facade design pattern or wrapper class contains methods that are simply delegated to the underlying implementation class.
class Deck:
    def __init__(self):
        self._cards = [card(r+1, s) for r in range(13) for s in (Club,Diamond, Heart, Spade)]
        random.shuffle(self._cards)
    def pop(self):
        return self._cards.pop()

# Extending a collection class 
# in this case we don't have to reimplement the pop() method, we can inherit it 
class Deck(list):
    def __init__(self):
        super().__init__(card(r+1, s) for r in range(13) for s in (Club,Diamond, Heart, Spade))
        random.shuffle(self)



'''
String Representations
'''
# produces an unambiguous string representation of an object
# exactness more important - good for debugging and logging 
# usually the text you would type for recreateing the instance 
__repr__() 

# intended for clients
# readable, human-friendly output 
# if do not define str(), the defaul falls to repr()
__str__() 


class Point2D:
    def __init__(self, x, y):
        self.x=x
        self.y=y 
    # for use print('the circle is centered at {}.'.format(p))
    def __str__(self):
        return '({},{})'.format(self.x, self.y)
    
    def __repr__(self):
        return 'Point2D(x={}, y={})'.format(self.x, self.y)


# Specifically, the special !r formatting code indicates that the
# output of __repr__() should be used instead of __str__(), the default

# >>> p = Pair(3, 4)
# >>> print('p is {0!r}'.format(p))
# p is Pair(3, 4)
# >>> print('p is {0}'.format(p))
# p is (3, 4)



# format options 
__format__

# customized formatting 
_formats = {
    'ymd' : '{d.year}-{d.month}-{d.day}',
    'mdy' : '{d.month}/{d.day}/{d.year}',
    'dmy' : '{d.day}/{d.month}/{d.year}'
}

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day 
    
    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)
    



'''
simplifying intialization
'''
class Structure:
    # class variable that specifies expected fields 
    _fields = []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        
        # set the positional arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)
        
        # Set the remaining keyword arguments
        for name in self._fields[len(args):]:
            setattr(self, name, kwargs.pop(name))
        
        # Check for any remaining unknown arguments
        if kwargs:
            raise TypeError('Invalid argument(s): {}'.format(','.join(kwargs)))

# Example class definition 
if __name__ == '__main__':
    class Stock(Structure):
        _fields = ['name', 'shares', 'price']


'''
Define more than one constructor
'''
# create instances in more than one way 
# use a class method 
# receive the class as the first argument (cls)
# class polymorphism 

import time 

class Date:
    # Primary constructor 
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day 
    
    # alternate constructor 
    @classmethod 
    def today(cls):
        t = time.localtime()
        return cls(t.t,_year, t.tm_mon, t.tm_mday)

# to use alternate constructor, call it as a function, such as Date.today()
# a = Date(2012, 12, 21) # Primary
# b = Date.today() # Alternate

# since python only support __init__ as a single constructor per class 
# use @classmethod to define alternative constructors for your classes 
# use class method polymorphism to provide generic way to build and connect concrete subclasses 

class GenericWorker(object):
    # ...
    def map(self):
        raise NotImplementedError 
    
    def reduce(other, self):
        raise NotImplementedError 

    @classmethod
    def create_workers(cls, input_class, config):
        workers = []
        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_data))
        return workers 

'''
get attributes
'''
import math 

class Point: 
    def __init__(self, x, y):
        self.x = x
        self.y = y 
    
    def __repr__(self):
        return 'Point({!r:},{!r:})'.format(self.x, self.y)
    
    def distance(self, x, y):
        return math.hypot(self.x -x, self.y - y)

p = Point(2,3)
d = getattr(p, 'distance')(0, 0) # Calls p.distance(0,0)



'''
manager objects
'''
# management objects are like office managers, they don't do the actual visible work 
# the attributes on the management objects tend to refer to other objects that do the real work
# the behaviors on such a class delete to those other classes at the right time and pass messages between them

# example manager object ensuring 
# unzipping the file, performing the find and replace, zipping the new file 
import sys
import shutil
import zipfile 

from pathlib import Path 

class ZipReplace:
    def __init__(self, filename, search_string, replace_string):
        # initialization contains the actual objects to manipulate 
        self.filename = filename
        self.search_string = search_string
        self.replace_string = replace_string
        self.temp_directory = Path("unzipped-{}".format(filename))
    
    # then create an overall managemer object for the three steps 
    def zip_find_replace(self):
        self.unzip_files()
        self.find_replace()
        self.zip_files()

    def unzip_files(self):
        self.temp_directory.mkdir()
        with zipfile.ZipFile(self.filename) as zip:
            zip.extractall(str(self.temp_directory))
    
    def find_replace(self):
        for filename in self.temp_directory.iterdir():
            with filename.open() as file:
                contents = file.read()
            contents = contents.replace(self.search_string, self.replace_string)
            with filename.open("w") as file:
                file.write(contents)

    def zip_files(self):
        with zipfile.ZipFile(self.filename, 'w') as file:
            for filename in self.temp_directory.iterdir():
                file.write(str(filename), filename.name)
        shutil.rmtree(str(self.temp_directory))

if __name__ == "__main__":
    ZipReplace(*sys.argv[1:4]).zip_find_replace()



##################################################
#  Decorators / Wrapping 
##################################################



# A decorator is a callable that takes another function as argument (the decorated function).
# The decorator may perform some processing with the decorated function, and returns it or replaces it with another function or callable object.

# when python executes decorators 
# decorators run right after the decorated function is defined 
# this is usually at import time 

# built in decorators
@classmethod 
@staticmethod
@property 

# standard library decorators 
@functools.total_ordering

# In other words, assuming an existing decorator named decorate, this code:

@decorate
def target():
    print('running target()')

# Has the same effect as writing this:
def target():
    print('running target()')
target = decorate(target)


# the target name does not necessarily refer to the original target function, but to whatever function is returned
# by decorate(target).
def deco(func):
    def inner():
        print('running inner()')
    return inner 

@deco 
def target():
    print('running target()')

'''
using wraps
'''
# another example that adds extra processing (logging, timing)
# @wraps(func) is pretty important to preserve function metadata
# Using functools.wraps decorator assures that the original function
# name and docstring are preserved in the result function.

# The code inside a decorator typically involves creating a new function that accepts any
# arguments using *args and **kwargs, as shown with the wrapper() function in this
# recipe. Inside this function, you place a call to the original input function and return its
# result. However, you also place whatever extra code you want to add (e.g., timing). The
# newly created function wrapper is returned as a result and takes the place of the original
# function.

import time
from functools import wraps 

def timethis(func):
    '''
    Decorator that reports the execution time
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result 
    return wrapper 


# example using the decorator 
@timethis 
def countdown(n):
    '''
    Counts down
    ''' 
    while n > 0:
        n -=1 


# >>> target()
# running inner()  Invoking the decorated target actually runs inner.
# >>> target
# <function deco.<locals>.inner at 0x10063b598>  Inspection reveals that target is a now a reference to inner.

# A key feature of decorators is that they run right after the decorated function is defined.
# That is usually at import time (i.e., when a module is loaded by Python).


# Another Decorator Example
# output the running time of the functions 
import time
import functools 

def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0=time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print('[%0.8fs] %s(%s) -> %r ' % (elapsed, name, arg_str, result))
        return result
    return clocked 

'''
Unwrapping a Decorator
'''

# gain access to the original function by accessing the __wrapped__ attribute
@somedecorator
def add(x, y):
    return x+y

orig_add = add.__wrapped__
orig_add(3,4)


'''
Decorator that takes arguments
'''
from functools import wraps 
import logging 

# The outermost function logged() accepts the desired arguments and simply makes them
# available to the inner functions of the decorator
def logged(level, name=None, message=None):
    '''
    Add logging to a function
    '''
    # The inner function decorate() accepts a function and puts a wrapper around it as normal.
    def decorate(func):
        logname = name if name else func.__module__
        log logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper 
    return decorate 

# Example use 
@logged(logging.DEBUG)
def add(x, y):
    return x + y 

@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam')



''' 
Decorator Enhanced Strategy Pattern 
'''
promos = []

def promotion(promo_func):
    promos.append(promo_func)
    return promo_func

@promotion
def fidelity(order):
    return order.total()*0.05 if order.customer.fidelity >= 1000 else 0

@promotion 
def bulk_item(order):
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

def best_promo(order):
    return max(promo(order) for promo in promos)

''' 
Decorators in Standard Library
'''

# Memoization with functools.lru_cache
# functools.lru_cache. It implements memoization: an optimization technique that works by saving the results of previous invocations of an
# expensive function, avoiding repeat computations on previously used arguments.

# faster implmentation using caching 
import functools
from clockdeco import clock 

@functools.lru_cache() # @lru_cache() is applied on the function returned by @clock
@clock 
def fibonacci(n):
    if n <2: 
        return n 
    return fibonacci(n-2)+fibonacci(n-1)

if __name__=='__main__':
    print(fibonacci(6))


''' 
Stacked Decorators
'''
@d1
@d2
def f():
    print('f')

# is the same as 
def f():
    print('f')

f = d1(d2(f))


''' 
Parameterized Decorators
'''
# make a decorator factory and take arguments and return a decorator 
registry = []
def register(func):
    print('running register(%s)' %func)
    registry.append(func)
    return func 

@register 
def f1():
    print('running f1()')

print('running main()')
print('registry ->', registry)
f1()


# now change it to enable or disable functino registration 
# based on an optional active parameter 
registry = set()

def register(active=True):
    def decorate(func):
        print('running register(active=%s)->decorate(%s)' % (active, func))
        if active:
            registry.add(func)
        else:
            registry.discard(func)
        return func 
    return decorate 

@register(active=False)
def f1():
    print('running f1()')

@register()
def f2():
    print('running f2()')

def f3():
    print('running f3()')


'''
Example: enforcing type checking
'''
# optionally enforce type checking of funciton arguments 
@typeassert(int, int)
def add(x, y):
    return x+y


# create the @typeassert decorator
from inspect import signature
from functools import wraps 

def typeassert(*ty_args, **ty_kwargs):
    def decorate(func):
        # If in optimized mode, disable type checking, i.e. return the function unwrapped
        if not __debug__:
            return func 
        
        # map function argument names to supplied types 
        sig = signature(func)
        # rthis bind_partial().arguments return something like OrderedDict([('a', 10), ('b', 11)])
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            # Enforce type assertions across supplied arguments 
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError(
                        'Argument {} must be {}'.format(name, bound_types[name])
                        )
            return func(*args, **kwargs)
        return wrapper 
    return decorate 


'''
Applying decorators to Class and Static Methods
'''

import time 
from functools import wraps 

# A simple decorator 
def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print(end-start)
        return r 
    return wrapper 

# Class illustrating application of the decorator to different methods 
class Spam:
    @timethis
    def instance_method(self, n):
        print(self, n)
        while n > 0:
            n -=1
    
    # make sure classmethod appears first 
    @classmethod
    @timethis
    def class_method(cls, n):
        print(cls, n)
        while n > 0:
            n -= 1
    
    @staticmethod
    @timethis
    def static_method(n):
        print(n)
        while n > 0:
            n -=1 
        



##################################################
#  Class Method vs. Static Method
##################################################

# instance vs. class vs. static methods 
# https://realpython.com/instance-class-and-static-methods-demystified/

# class method
# Instead of accepting a self parameter, class methods take a cls parameter that points to the class—and not the object instance—when the method is called.
# classmethod changes the way the method is called, so it receives the class itself as the first argument, instead of an instance. Its most common use is for alternative constructors

'''
Class Method
'''


@classmethod
def frombytes(cls, octets):
    typecode = chr(octets[0])
    memv = memoryview(octets[1:]).cast(typecode)
    return cls(*memv)


class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'

    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])


# can use classmethod for factory methods
# >>> Pizza.margherita()
# Pizza(['mozzarella', 'tomatoes'])

# >>> Pizza.prosciutto()
# Pizza(['mozzarella', 'tomatoes', 'ham'])


# can use class method decorator as well 
# require access to the class object to call other class methods or the constructor
@classmethod 
def _get_next_serial(cls):
    result = cls.next_serial
    cls.next_serial +=1
    return result 

# use class methods for factory function (named constructors)
# so that we don't need to tweak the init function 
@classmethod
def create_empty(cls, owner_code):
    return cls(owner_code, contents=None)
# from shipping import *
# c3 = shippingContainer.create_empty("YML")
# c3.contents

@classmethod
def create_with_items(cls, owner_code, items):
    return cls(owner_code, content=list(items))

# static methods with inheritance
# static methods can be overwritten in subclasses 


# need to call by self if wants overwritten 

# use super() for subclass extending base class 



'''
Static Methods
'''
# static methods
# no access needed to either class or instance objects
# mostly likely an implementation detail of the class 
# can be moved to become a module-scope function

class ShippingContainer:
    next_serial = 1336

    # use the static method decorator
    @staticmethod
    def _get_next_serial():
        result = ShippingContainer.__get_next_serial
        ShippingContainer.new_serial += 1
        return result 

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer._get_next_serial


class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return (f'Pizza({self.radius!r}, '
                f'{self.ingredients!r})')

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi

# Because the circle_area() method is completely independent from the rest of the class it’s much easier to test.



##################################################
#  Abstract Base Classes 
##################################################

# While duck typing is useful, it is not always easy to tell in advance if a class is going
# to fulfill the protocol you require. Therefore, Python introduced the idea of abstract
# base classes. Abstract base classes, or ABCs, define a set of methods and properties
# that a class must implement in order to be considered a duck-type instance of that
# class. The class can extend the abstract base class itself in order to be used as an
# instance of that class, but it must supply all the appropriate methods.


'''
using ABCs from Collections 
'''
# example using an ABC
# Container class from Collections
from collections import Container

# check which bstract methods need to be implemented
Container.__abstractmethods__
# frozenset(['__contains__'])

# check what the function signature should look like
help(Container.__contains__)

# define a dummy container
class OddContainer:
    def __contains__(self, x):
        if not isinstance(x, int) or not x % 2:
            return False
        return True

odd_container = OddContainer()

# even though we did not extend Container from OddContainer, the class is a Container object 
isinstance(odd_container, Container)
# True
# so with duck typing, we can create is a relationships without the overhead of using inheritance 


# Custom class to mimics the behavior of a common built-in container type 
# for example, if you want a custom iterator then start with Iterable ABC
# But you need to implment all the required special methods 
import collections

class A(collections.Iterable):
    pass 


# create a sequence where items are stored in sorted order 
import collections 
import bisect 

class SortedItem(collections.Sequence):
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial is None else []

    # required sequence methods 
    def __getitem__(self, index):
        return self._items[index]
    
    def __len__(self):
        return len(self._items)
    
    # methods for adding an item in the right location 
    def add(self, item):
        bisect.insort(self._items, item)

# Here’s an example of using this class:
# >>> items = SortedItems([5, 1, 3])
# >>> list(items)


# many abstract base classes in collections provide default implementations of common container methods 
class Items(collections.MutableSequence):
    def __init__(self, initial=None):
        self._items = list(initial) if initial is None else []
    
    # required sequence methods 
    def __getitem__(self, index):
        print('Getting:', index)
        return self._items[index]

    def __setitem__(self, index, value):
        print('Setting:', index, value)
        self._items[index] = value 
    
    def __delitem__(self, index):
        print('Deleting:', index)
        del self._items[index]
    
    def insert(self, index, value):
        print('Inserting:', index, value)
        self._items.insert(index, value)
    
    def __len__(self):
        print('Len')
        return len(self._items)
    
# If you create an instance of Items, you’ll find that it supports almost all of the core list
# methods (e.g., append(), remove(), count(), etc.). These methods are implemented in
# such a way that they only use the required ones.


'''
Defining an ABC
'''

# abstract methods load() and pick()
# concrete methods loaded() and inspect()

import abc

class Tombola(abc.ABC):

    @abc.abstractmethod 
    def load(self, iterable):
        """Add items from an iterable""" 

    @abc.abstractmethod 
    def pick(self):
        """Remove item at random, returning it 
        This method should raise `LookupError` when the instance is empty.
        """

    def loaded(self):
        """Return `True` if there's at least 1 item, `False` otherwise."""
        return bool(self.inspect())
    
    def inspect(self):
        """Return a sorted tuple with the items currently inside"""
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break 
        self.load(items)
        return tuple(sorted(items))


# another example defining an ABC 

import abc
# by passing in metaclass you are giving this class superclass capabilities
class MediaLoader(metaclass=abc.ABCMeta):
    # by making this method abstract, stating any subclass must implement that method 
    @abc.abstractmethod
    def play(self):
        pass
    
    # any subclass must supply that property 
    @abc.abstractproperty
    def ext(self):
        pass 
   
    # It is basically saying that any class that supplies concrete implementations of all the 
    # abstract attributes of this ABC should be considered a subclass of MediaLoader. Doesn't need to inherit from the MediaLoader class
    @classmethod 
    def __subclasshook__(cls, C):
        # is class C a subclass of this cls
        if cls is MediaLoader:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True
        return NotImplemented


##################################################
#  Closures 
##################################################

# Actually, a closure is a function with an extended scope that encompasses nonglobal
# variables referenced in the body of the function but not defined there. It does not matter
# whether the function is anonymous or not; what matters is that it can access nonglobal
# variables that are defined outside of its body.

def make_averager():
    series = []
    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)
    return averager 

# avg = make_averager()
# >>> avg(10)
# 10.0
# >>> avg(11)
# 10.5
# >>> avg(12)

# The binding for series is kept in the __closure__ attribute of the returned function
# avg. Each item in avg.__closure__ corresponds to a name in avg.__code__.co_free
# vars.

# To summarize: a closure is a function that retains the bindings of the free variables that
# exist when the function is defined, so that they can be used later when the function is
# invoked and the defining scope is no longer available.


##################################################
#  Local vs. Global Variables (Scope)
##################################################

# Python does not require you to declare variables,
# but assumes that a variable assigned in the body of a function is local.

'''
nonlocal
'''
# The nonlocal declaration was introduced in Python 3. It lets you
# flag a variable as a free variable even when it is assigned a new value within the function.
# If a new value is assigned to a nonlocal variable, the binding stored in the closure is
# changed.

def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total 
        count +=1
        total +=new_value 
        return total/count
    return averager 


##################################################
#  Idioms
##################################################

'''
Variables Assigment 
'''
# Variables are like sticky notes 
>>> a = [1, 2, 3]
>>> b = a
>>> a.append(4)
>>> b
[1, 2, 3, 4]

# To understand an assignment in Python, always read the righthand
# side first: that’s where the object is created or retrieved. After
# that, the variable on the left is bound to the object, like a label
# stuck to it. Just forget about the boxes.



'''
Identify, Equality, and Aliases 
'''
>>> charles = {'name': 'Charles L. Dodgson', 'born': 1832}
>>> lewis = charles # lewis is an alias for charles.
>>> lewis is charles # The is operator and the id function confirm it.
True
>>> id(charles), id(lewis) # Adding an item to lewis is the same as adding an item to charles
(4300473992, 4300473992)
>>> lewis['balance'] = 950
>>> charles
{'name': 'Charles L. Dodgson', 'balance': 950, 'born': 1832}

>>> alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950} # alex refers to an object that is a replica of the object assigned to charles.
>>> alex == charles
True # The objects compare equal, because of the __eq__ implementation in the dict class 
>>> alex is not charles
True # But they are distinct objects. 


# == vs. is
# The == operator compares the values of objects (the data they hold), while is compares their identities

'''
Relative Immutability of Tuples
'''
# Tuples, like most Python collections—lists, dicts, sets, etc.—hold references to objects.
# If the referenced items are mutable, they may change even if the tuple itself does not.

# In other words, the immutability of tuples really refers to the physical contents of the
# tuple data structure (i.e., the references it holds), and does not extend to the referenced
# objects.


'''
Copy
'''
# Copies are shallow by default 
# easiest way to copy a list (or any built-in mutable collections) is to use the built-in constructor for the type itself
l1 = [3, [55, 44], (7, 8, 9)]
l2 = list(l1)
l2 == l1 # True 
l2 is l1 # False 

# Using the constructor or [:] produces a shallow copy (i.e., the outermost
# container is duplicated, but the copy is filled with references to the same items held by
# the original container). 


# Deep copy
# Working with shallow copies is not always a problem, but sometimes you need to make
# deep copies (i.e., duplicates that do not share references of embedded objects). The copy
# module provides the deepcopy and copy functions that return deep and shallow copies
# of arbitrary objects


# >>> import copy
# >>> bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
# >>> bus2 = copy.copy(bus1) # shallow copy
# >>> bus3 = copy.deepcopy(bus1) # deep copy
# >>> id(bus1), id(bus2), id(bus3)
# (4301498296, 4301499416, 4301499752)
# >>> bus1.drop('Bill')
# >>> bus2.passengers 
# ['Alice', 'Claire', 'David'] # if bus1 changes, so does bus2
# >>> id(bus1.passengers), id(bus2.passengers), id(bus3.passengers)
# (4302658568, 4302658568, 4302657800)
# >>> bus3.passengers
# ['Alice', 'Bill', 'Claire', 'David']


'''
Function Parameters as References
'''

# Call by sharing means that each formal parameter of the function gets a copy of each reference in the arguments. In other words,
# the parameters inside the function become aliases of the actual arguments

# The result of this scheme is that a function may change any mutable object passed as a
# parameter, but it cannot change the identity of those objects

# example: a function may change any mutable object it receives
def f(a, b):
    a += b
    return a 

a = [1,2]
b = [3,4]
f(a, b)
# >>> a, b
# ([1, 2, 3, 4], [3, 4]) # the list is changed


# Don't use mutable types as parameter defaults 
# The problem is that each default value is evaluated when the function is defined—i.e., usually when the module is loaded—and the
# default values become attributes of the function object. So if a default value is a mutable
# object, and you change it, the change will affect every future call of the function.

# instead use None as default 

def __init__(self, names=None):
    if names is None:
        self.names = []
    else:
        self.names = list(names)

'''
Weak References 
'''


# The presence of references is what keeps an object alive in memory. When the reference
# count of an object reaches zero, the garbage collector disposes of it. But sometimes it is
# useful to have a reference to an object that does not keep it around longer than necessary.

# A common use case is a cache
# Weak references are useful in caching applications because you don’t want the cached
# objects to be kept alive just because they are referenced by the cache.




##################################################
#  Object Representations
##################################################

'''
repr vs. str 
'''
# As you know, we implement the special methods __repr__ and __str__ to support
# repr() and str().

# repr()
# Return a string representing the object as the developer wants to see it.

# str()
# Return a string representing the object as the user wants to see it.


class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.x=float(x)
        self.y=float(y)
    
    # makes unpacking work 
    # implement via generator expression
    def __iter__(self):
        return (i for i in (self.x, self.y))
    
    def __repr__(self):
        class_name = type(self).__name__
        # interpolating the components with {!r} to get their repr
        return '{}({!r}, {!r})'.format(class_name, *self)
    
    def __str__(self):
        return str(tuple(self))
    
    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
        bytes(array(self.typecode, self)))
    
    def __eq__(self, other):
        return tuple(self) == tuple(other)
    
    def __abs__(self):
        return math.hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(abs(self))

''' 
format
'''
# The format() built-in function and the str.format() method delegate the actual formatting
# to each type by calling their .__format__(format_spec) method

# The format() method of a string can also access these methods. When we
# use {!r} or {!s} formatting, we're requesting __repr__() or __str__(),
# respectively.


# '1 BRL = {rate:0.2f} USD'.format(rate=brl)

from datatime import datetime 
now = datetime.now()
format(now, '%H:%M:%S')
"It's now {:%I:%M %p}".format(now)


# def format 
def __format__(self, fmt_spec=''):
    components = (format(c, fmt_spec) for c in self)
    return '({},{})'.format(*components)

class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self._x = float(x)
        self._y = float(y)
    
    @property
    def x(self):
        return self.__x 
    
    @property 
    def y(self):
        return self.__y 
    
    def __iter__(self):
        return (i for i in (self.x, self.y))
    
'''
Saving Space with __slots__ class attribute
'''
# If you are dealing with millions of instances with few attributes, the
# __slots__ class attribute can save a lot of memory, by letting the interpreter store the
# instance attributes in a tuple instead of a dict.

class Vector2d:
    __slots__ = ('__x', '__y')
    typecode = 'd'
    # methods follow 



##################################################
#  Inheritance 
##################################################

'''
Calling a method on a Parent class 
'''

# use the super() function 

# specify just the differences in the new inherited class
# class variable sounds starts out with the string "Meow" instead of the string "mrrp", and there is a new method chasing_rats

class HighSchoolStudent(Student):
    school_name = 'new high school'

    def get_name(self):
        original_value = super().get_name()



# class SubClass(BaseClass)
# base class __init__() is not called if overwritten, unless define init as super().__init__()

# super() used to call method on base class

class SimpleList:
    def __init__(self, items):
        self._items = items
    
    def add(self, item):
        self._items.append(item)
    
    def __getitem__(self, index):
        return self._items[index]
    
    def sort(self):
        self._items.sort()
    
    def __len__(self):
        return len(self._items)
    
    def __repr__(self):
        return "Simplelist({!r})".format(self._items)

# handling the __init__() method to make sure the superclasses are property intialized 
class SortedList(SimpleList):
    def __init__(self, items=()):
        super().__init__(items)
        self.sort()
    
    def add(self, item):
        super().add(item)
        self.sort()
    
    def __repr__(self):
        return "SortedList({!r})".format(list(self))

# isinstance() determines if an object is of a specified type
# also returns true if subclass of the type
isinstance('hello', str)

# issubclass()
# determines if one type is a subclass of another


'''
polymorphism
'''
# different behaviors happen depending on which subclass is being used, without having to explicitly know what the subclass actually is.
# use objects of different types through a common interface
# determined at the time of use

# Polymorphism is a way for multiple classes in a hierarchy to implement their own unique
# versions of a method. This allows many classes to fulfill the same interface or abstract
# base class while providing different functionality 

# checka valid extension was given upon initialization. Note the __init__ method in the parent class is able to access
# the ext class variable from different subclasses. That's polymorphism at work. If the filename doesn't end with the correct name, it raises an exception. 
# The fact that AudioFile doesn't actually store a reference to the ext variable doesn't stop it from being able to access it on the subclass.

class AudioFile:
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception("Invalid file format")
        self.filename = filename

class MP3File(AudioFile):
    ext = "mp3"
    def play(self):
        print("playing {} as mp3".format(self.filename))

'''
duck typing
'''

# Polymorphism is one of the most important reasons to use inheritance in many
# object-oriented contexts. Because any objects that supply the correct interface can
# be used interchangeably in Python, it reduces the need for polymorphic common
# superclasses. Inheritance can still be useful for sharing code but, if all that is being
# shared is the public interface, duck typing is all that is required. This reduced need
# for inheritance also reduces the need for multiple inheritance; often, when multiple
# inheritance appears to be a valid solution, we can just use duck typing to mimic one
# of the multiple superclasses.

# Duck typing in Python allows us to use any object that provides the required behavior
# without forcing it to be a subclass. The dynamic nature of Python makes this trivial.
# The following example does not extend AudioFile, but it can be interacted with in
# Python using the exact same interface:
class FlacFile:
    def __init__(self, filename):
        if not filename.endswith(".flac"):
        raise Exception("Invalid file format")
        self.filename = filename
    
    def play(self):
        print("playing {} as flac".format(self.filename))


# Another useful feature of duck typing is that the duck-typed object only needs to
# provide those methods and attributes that are actually being accessed. For example,
# if we needed to create a fake file object to read data from, we can create a new object
# that has a read() method; we don't have to override the write method if the code
# that is going to interact with the object will only be reading from the file. More
# succinctly, duck typing doesn't need to provide the entire interface of an object that
# is available, it only needs to fulfill the interface that is actually accessed.


'''
Subclassing Built-in Types
'''
# Subclassing built-in types like dict or list or str directly is errorprone because the built-in methods mostly ignore user-defined overrides. 
# Instead of subclassing the built-ins, derive your classes from the collections module using UserDict, UserList, and UserString, which are designed to be easily extended.


'''
Delegate Attribute Access
'''
# want an instance to delegate attribute access to an internally held instance 
# as an alternative to inheritance or in order to implement a proxy

class A: 
    def spam(self, x):
        pass 

    def foo(self):
        pass 

class B: 
    def __init__(self):
        self._a = A()
    
    def spam(self, x):
        # delegate to the internal self._a instance 
        return self._a.spam(x)

    def foo(self)
        return self._a.foo()
    
    def bar(self):
        pass 

# if having a lot of attributes to delegate, define the __getattr__()

class A: 
    def spam(self, x):
        pass

    def foo(self):
        pass 

class B: 
    def __init__(self):
        self._a = A()

    def bar(self):
        pass 

    # expose all of the methods defined on class A 
    def __getattr__(self, name):
        return getattr(self._a, name)

# The __getattr__() method is kind of like a catch-all for attribute lookup. It’s a method
# that gets called if code tries to access an attribute that doesn’t exist.


'''
strategy object initilization
'''

# create strategy objects 
# raise an exception for methods that must be implemented by a subclass
class BettingStrategy:
    def bet( self ):
        raise NotImplementedError( "No bet method" )
    def record_win( self ):
        pass
    def record_loss( self ):
        pass

class Flat(BettingStrategy):
    def bet( self ):
        return 1

# subclass must overrride the basic bet() method 


'''
multiple inheritance
'''
# We can use multiple inheritance in a disciplined way to create cross-cutting aspects. 
# We'll consider a base class plus mixin class definitions to introduce features. Often, we'll use the mixin classes to build cross-cutting aspects.


# define class with more than one base class 
class SubClass(Base1, Base2):
    pass
# subclass inherit methods of all bases 
# if a class defines no intializer, then only the init from the first base class is called
# __bases__ a tuple of base classes 
# method resolution order 
SortedList.__mro__ # to print out the method resolution order 

# super()
# given a method resolution order and a class C, super gives you an object which resolves method using only the part which comes after C
# super() returns a proxy object which routes method calls
super(base-class, derived-class) 
# instance bound proxy
super(class, instance-of-class)

# object model
# the ultimate base class of every class object 
NoBaseClass.__bases__
dir(object) # outputs ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

# best practice
# use multiple inheritance only for mix-in utility 
# If you find yourself desiring the convenience and encapsulation that comes with multiple
# inheritance, consider writing a mix-in instead. A mix-in is a small class that only defines a
# set of additional methods that a class should provide. Mix-in classes don’t define their
# own instance attributes nor require their __init__ constructor to be called.


# MRO 
# An object's class will define a Method Resolution Order (MRO).
# This defines how base classes are searched to locate an attribute or method name.
# The MRO works its way up the inheritance hierarchy; this means that subclass
# names override superclass names. This implementation method search meets our
# expectation for what inheritance means.

bool.__mro__
# (<class 'bool'>, <class 'int'>, <class 'object'>)

# type of inehritance 
# distinguish interface inheritance from implementation inheritance
# inheritance of interface creates a subtype, implying a "is-a" relationship
# inheritance of implementation avoids code duplication by reuse 

# making interfaces explicit with ABCs
# if a class is designed to define an interface, it should be an explicit ABC (i.e. subclass abc.ABC)

# use Mixins for code reuse 
# a mixin does not define a new type, it merely bundles methods for reuse
# a mixin should never be instantiated, and concrete classes should not inherit only from mixins

# Every class has an interface: the set public attributes (methods or data attributes) implemented or inherited
# by the class. This includes special methods, like __getitem__ or __add__.

class Foo:
    def __getitem__(self, pos):
        return range(0,30,10)[pos]

# There is no method __iter__ yet Foo instances are iterable because—as a fallback—
# when Python sees a __getitem__ method, it tries to iterate over the object by calling
# that method with integer indexes starting with 0. Because Python is smart enough to
# iterate over Foo instances, it can also make the in operator work even if Foo has no
# __contains__ method: it does a full scan to check if an item is present.

# deals with multiple init needed
# pass in the **kwargs to manage different sets of arguments

# We've changed all arguments to keyword arguments by giving them an empty
# string as a default value. We've also ensured that a **kwargs parameter is included
# to capture any additional parameters that our particular method doesn't know what
# to do with. It passes these parameters up to the next class with the super call.

class Contact:
    all_contacts = []
    def __init__(self, name='', email='', **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        self.all_contacts.append(self)

class AddressHolder:
def __init__(self, street='', city='', state='', code='',**kwargs):
    super().__init__(**kwargs)
    self.street = street
    self.city = city
    self.state = state
    self.code = code

class Friend(Contact, AddressHolder):
    def __init__(self, phone='', **kwargs):
        super().__init__(**kwargs)
        self.phone = phone


##################################################
#  Descriptors 
##################################################

# A descriptor is a class that mediates attribute access. The descriptor class can be used
# to get, set, or delete attribute values. Descriptor objects are built inside a class at class
# definition time.

# The descriptor design pattern has two parts: an owner class and the attribute
# descriptor itself.

# The owner class uses one or more descriptors for its attributes.

# A descriptor class defines some combination of get, set, and delete methods. 
# An instance of the descriptor class will be an attribute of the owner class.


class Integer:
    def __init__(self, name):
        self.name = name 
    
    def __get__(self, instance, cls):
        if instance is None:
            return self 
        else:
            return instance.__dict__[self.name]
        
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeErrr('Expected an int')
        instance.__dict__[self.name] = value 

    def __delete__(self, instance):
        del instance.__dict__[self.name]

# to use a descriptor, instances of the descriptor are placed into a class definition as class variables 
# Unlike other attributes, descriptors are created at the class level. They're not created within the __init__() initialization. While descriptor values can be set during initialization, 

class Point: 

    # descriptors are generally built as part of the class, outside any method functions.
    x = Integer('x')
    y = Integer('y')
    def __init__(self, x, y):
        self.x = x
        self.u = y 

p = Point(2,3)
p.x # calls Point.x.__get__(p, Point)

# By defining a descriptor, you can capture the core instance operations (get, set, delete)
# at a very low level and completely customize what they do


# Different types of descriptors
# The descriptor object has, or acquires, the data. In this case, the descriptor
# object's self variable is relevant and the descriptor is stateful. With a data
# descriptor, the __get__() method returns this internal data. With a nondata
# descriptor, the descriptor has other methods or attributes to access this data.

# The owner instance contains the data. In this case, the descriptor object must
# use the instance parameter to reference a value in the owning object. With
# a data descriptor, the __get__() method fetches the data from the instance.
# With a nondata descriptor, the descriptor's other methods access the
# instance data.

# The owner class contains the relevant data. In this case, the descriptor
# object must use the owner parameter. This is commonly used when the
# descriptor implements a static method or class method that applies to the
# class as a whole.


# The most compelling cases for creating new descriptors relate to mapping between
# Python and something non-Python. Object-relational database mapping, for example,
# requires a great deal of care to ensure that a Python class has the right attributes in
# the right order to match a SQL table and columns. Also, when mapping to something
# outside Python, a descriptor class can handle encoding and decoding data or fetching
# the data from external sources.

'''
Timeit module for testing performance
'''
timeit.timeit("f()", """def f(): pass""")


##################################################
# Attribute Access & Properties
##################################################

'''
attribute access
'''
# it's not required to provide all attributes in the __init__() method 
# optional attributes imply an informal subclass relationship 

# special methods for attribute access
# __getattr__(), __setattr__(), and __delattr__()

# The __setattr__() method will create and set attributes.
# The __getattr__() method will do two things. Firstly, if an attribute
# already has a value, __getattr__() is not used; the attribute value is
# simply returned. Secondly, if the attribute does not have a value, then
# __getattr__() is given a chance to return a meaningful value. If there is
# no attribute, it must raise an AttributeError exception.
# The __delattr__() method deletes an attribute.

# if your class defines __getattr__,that method is called every time an attribute can't be found in an object's instance dictionary
class LazyDB(object):
    def __init__(self):
        self.exists = 5
    
    def __getattr__(self, name):
        value = 'Value for %s' % name 
        setattr(self, name, value)
        return value 

# if accessing a missing property, this __getattr mutates the instance dictionary __dict__
data = LazyDB()
print('Before:', data.__dict__)
print('foo', data.foo)
print('after', data.__dict__)

# The exists attribute is present in the instance dictionary, so __getattr__ is never
# called for it. The foo attribute is not in the instance dictionary initially, so
# __getattr__ is called the first time. But the call to __getattr__ for foo also does
# a setattr, which populates foo in the instance dictionary. This is why the second time
# I access foo there isn’t a call to __getattr__.



'''
properties
'''

# A simple way to customize access to an attribute is to define it as a “property.” 

# a property is a method funciton that appears to be a simple attribute. We can get, set, and delete property values similarly to how we can get, set, and delete attribute values

# Properties should only be used in cases where you actually need to perform extra processing
# on attribute access.

# Will make program run a lot slower and add confusion 

# The advantage of using properties is that the syntax doesn't have to change when
# the implementation changes. We can make a similar claim for getter/setter method
# functions. However, getter/setter method functions involve extra syntax that isn't
# very helpful nor informative.

'''
getter, setter and deleter properties
'''
# getter, setter, deleter should all have the same name 
# setter and deleter depends on getter (first defining the property)

class Person:
    def __init__(self, first_name):
        # use first_name instead of _first_name, apply type checking when setting an attribute
        # the set operation uses the setter method as opposed to bypassing it by self._first_name
        self.first_name = first_name
    
    # Getter function
    @property
    def first_name(self):
        return self._first_name

    # Setter function
    @first_name.setter 
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value 
    
    # Delete function 
    @first_name.deleter 
    def first_name(self):
        raise AttributeError("Can't delete attribute")

# >>> a = Person('Guido')
# >>> a.first_name # Calls the getter
# 'Guido'
# >>> a.first_name = 42 # Calls the setter
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# File "prop.py", line 14, in first_name
# raise TypeError('Expected a string')
# TypeError: Expected a string
# >>> del a.first_name
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# AttributeError: can't delete attribute


# properties can be a way to define computed attributes
import math 
class Circle:
    def __init__(self, radius):
        self.radius = radius
    @property
    def area(self):
        return math.pi * self.radius **2
    @property 
    def perimeter(self):
        return 2 * math.pi * self.radius 


# don't just implement plain getter and setter methods 
# if you need special behavior when an attribute is set, can migrate to the @property decorator and setter attribute 

class VoltageResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)
        self._voltage = 0
        @property
        def voltage(self):
            return self._voltage
       
        @voltage.setter
        def voltage(self, voltage):
            self._voltage = voltage
            self.current = self._voltage / self.ohms
        # Now, assigning the voltage property will run the voltage setter method, updating the
        # current property of the object to match.

# setter can be used for validation as well 
class BoundedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)
    
    @property
    def ohms(self):
        return self._ohms
    
    @ohms.setter
    def ohms(self, ohms):
        if ohms <= 0:
            raise ValueError('%f ohms must be >0' % ohms)
            self._ohms = ohms 

# make parent class attribute immutable 
class FixedResistance(Resistor):
    @property
    def ohms(self):
        return self._ohms
    
    @ohms.setter
    def ohms(self, ohms):
        if hasattr(self, '_ohms'):
            raise AttributeError("can't set attribute")
        self._ohms = ohms 

# defining descriptor class 


##################################################
# Comparison Operator
##################################################

'''
Comparison operations
'''
# • x<y calls x.__lt__(y)
# • x<=y calls x.__le__(y)
# • x==y calls x.__eq__(y)
# • x!=y calls x.__ne__(y)
# • x>y calls x.__gt__(y)
# • x>=y calls x.__ge__(y)

class BlackJackCard:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit 
    def __lt__(self, other):
        print( "Compare {0} < {1}".format( self, other ) )
        return self.rank < other.rank
    def __str__(self):
        return "{rank}{suit}".format(**self.__dict__)


# example implementing comparison operators 
class BlackJackCard:
    def __init__(self, rank, suit, hard, soft):
        self.rank = rank
        self.suit = suit
        self.hard = hard 
        self.soft = soft 
    def __lt__(self, other):
        if not isinstance(other, BlackJackCard): 
            return NotImplemented
        return self.rank < other.rank 
    def __le__(self, other):
        try:
            return self.rank <= other.rank 
        except AttributeError:
            return NotImplemented
    def __gt__(self, other):
        if not isinstance(other, BlackJackCard):
            return NotImplemented
        return self.rank > other.rank 
    def __ge__(self, other):
        if not isinstance(other, BlackJackCard):
            return NotImplemented
        return self.rank >= other.rank 
    def __eq__( self, other ):
        if not isinstance( other, BlackJackCard ): 
            return NotImplemented
        return self.rank == other.rank and self.suit == other.suit
    def __ne__( self, other ):
        if not isinstance( other, BlackJackCard ): 
            return NotImplemented
        return self.rank != other.rank and self.suit != other.suit
    def __str__( self ):
        return "{rank}{suit}".format( **self.__dict__ )


'''
total ordering
'''

# The functools.total_ordering decorator can be used to simplify this process. To use
# it, you decorate a class with it, and define __eq__() and one other comparison method
# (__lt__, __le__, __gt__, or __ge__). The decorator then fills in the other comparison
# methods for you

from functools import total_ordering
class Room:
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width
        self.square_feet = self.length * self.width 

@total_ordering 
class House:
    def __init__(self, name, style):
        self.name = name
        self.style = style
        self.rooms = list()

    @property
    def living_space_footage(self):
        return sum(r.square_feet for r in self.rooms) 

    def add_room(self, room):
        self.rooms.append(room)

    def __str__(self):
        return '{}:{} square foot {}'.format(self.name,
                                             self.living_space_footage,
                                             self.style)
    def __eq__(self, other):
        return self.living_space_footage == other.living_space_footage

    def __lt__(self, other):
        return self.living_space_footage < other.living_space_footage


# explicit and implicit type checking 
# Two kinds of type checking: explicit and implicit. The explicit type
# checking uses isinstance(). The implicit type checking uses a try: block. There's
# a tiny conceptual advantage to using the try: block: it avoids repeating the name of
# a class. It's entirely possible that someone might want to invent a variation on a card
# that's compatible with this definition of BlackJackCard but not defined as a proper
# subclass. Using isinstance() might prevent an otherwise valid class from working
# correctly.

'''
mixed class comparison 
'''


# using isinstance
# example of comparing both against integer and against another object instance
def __eq__(self, other):
    if isinstance(other, int):
        return self.total() == other 
    try:
        return(self.cards == other.cards
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



##################################################
# __del__() method 
##################################################

# The intent is to give an object a chance to do any cleanup or finalization just before
# the object is removed from memory.

# reference count and destruction 
# objects have a reference count. The count is incresented when the object is assigned to a variable and decremented when the variable is removed 
# when reference count is zero, the object is no longer needed and can be destroyed
class Noisy:
    def __del__(self):
        print("Removing {0}".format(id(self)))


# Circular references and the weakref module
# In the cases where we need circular references but also want __del__() to work
# nicely, we can use weak references. One common use case for circular references are
# mutual references: a parent with a collection of children; each child has a reference
# back to the parent. If a Player class has multiple hands, it might be helpful for a
# Hand object to contain a reference to the owning Player class.



##################################################
# __new__() method
##################################################

'''
new
'''
# One use case for the __new__() method is to initialize objects that are otherwise
# immutable. The __new__() method is where our code can build an uninitialized
# object. This allows processing before the __init__() method is called to set the
# attribute values of the object.

# The __new__() method is used to extend the immutable classes where the
# __init__() method can't easily be overridden.

# The default implementation of __new__() simply does this: return super().__new__( cls )

class Float_Units( float ):
    def __new__( cls, value, unit ):
        obj= super().__new__( cls, value )
        obj.unit= unit
        return obj


##################################################
# metaclass 
##################################################

'''
metaclass
'''
# A metaclass builds a class. Once a class object has been built, the class object is used to build instances

# metaclass is defined by inheriting from type 
# a metaclass receives the content of associated class statements in its __new__ method


# use metaclass to control instance creation 
# make it impossible to create instance in the normal way 
class Spam:
    def __init__(self, name):
        self.name = name 
a = Spam('a')
b = Spam('b')

class NoInstances(type):
    def __call__(self, *args, **kwargs):
        raise TypeError("can't instantiate directly")

class Spam(metaclass=NoInstances):
    @staticmethod
    def grok(x):
        print('Spam.grok')

# another example, implement the singleton pattern 
# a class where only one instance is ever created 
class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None 
        super().__init__(*args, **kwargs)
    
    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instnace = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance 

# Example 
class Spam(metaclass=Singleton):
    def __init__(self):
        print('Creating Spam')

# Example - validate subclasses with metaclass
# receives the contents of associated class statements in its __new__ method. 
# Here you can modify class information before type is actually constructed

class Meta(type):
    def __new__(meta, name, bases, class_dict):
        print((meta, name, bases, class_dict))
        return type.__new__(meta, name, bases, class_dict)

class MyClass(object, metaclass=Meta):
    stuff = 123

    def foo(self):
        pass 

# Metaclasses let you run registration code automatically each time your base class is subclassed in a program.
# Using metaclasses for class registration avoids errors by ensuring that you never
# miss a registration call.

# descriptors and metaclasses make a powerful combination




##################################################
# Argument Signature
##################################################


# The inspect.signature() function allows you to extract signature information from a callable. For example:
from inspect import signature
def spam(x, y, z=42):
    pass
sig = signature(spam)
print(sig)
# (x, y, z=42)
# >>> sig.parameters
# mappingproxy(OrderedDict([('x', <Parameter at 0x10077a050 'x'>),
# ('y', <Parameter at 0x10077a158 'y'>), ('z', <Parameter at 0x10077a1b0 'z'>)]))
# >>> sig.parameters['z'].name
# 'z'
# >>> sig.parameters['z'].default
# 42

# Enforcing Argument signature on *args and **kwargs

from inspect import Signature, Parameter 
# make a signature for a func(x, y=42, *, z=None)
parms = [ Parameter('x', Parameter.POSITIONAL_OR_KEYWORD),
          Parameter('y', Parameter.POSITIONAL_OR_KEYWORD, default=42),
          Parameter('z', Parameter.KEYWORD_ONLY, default=None) ]
sig = Signature(parms)
print(sig)
# (x, y=42, *, z=None)

def func(*args, **kwargs):
    bound_values = sig.bind(*args, **kwargs)
    for name, value in bound_values.arguments.items():
        print(name, value)



##################################################
# Mixins 
##################################################

'''
cross cutting scenarios
'''
# Logging: We often need to have logging features implemented consistently
# in many classes. We want to be sure the loggers are named consistently and
# logging events follow the class structure in a consistent manner.

# Auditability: A variation of the logging theme is to provide an audit trail
# that shows each transformation of a mutable object. In many commerceoriented
# applications, the transactions are business records that represent
# bills or payments.

# Security: Our applications will often have security aspects that pervade
# each HTTP request and each piece of content downloaded by the website.
# The idea is to confirm that each request involves an authenticated user
# who is authorized to make the request.


# to support that, python offers 
# Decorators: With a decorator, we can establish a consistent aspect
# implementation at one of two simple join points in a function. We can
# perform the aspect's processing before or after the existing function. We
# can't easily locate join points inside the code of a function. It's easiest for
# decorators to transform a function or method by wrapping it with additional
# functionality.

# Mixins: With a mixin, we can define a class that exists outside a single
# class hierarchy. The mixin class can be used with other classes to provide
# a consistent implementation of a cross-cutting aspect. For this to work, the
# mixin API must be used by the classes that it is mixed into. Generally, mixin
# classes are considered abstract since they can't be meaningfully instantiated.

'''
mixin examples
'''
# context manager 
import contextlib.ContextDecorator 

class TestDeck(ContextDecorator, Deck):
    def __init__(self, size=1, seed=0):
        super().__init__(size=size)
        self.seed=seed

    def _init_shuffle(self):
        pass 
    
    def __enter__(self):
        self.rng.seed(self.seed, version=1)
        self.rng.shuffle(self)
        return self 
    
    def __exit__(self, exc_type, exc_value, traceback):
        pass 


# example using MailSender mixin to send emails 
class MailSender:
    def send_mail(self, message):
    print("Sending mail to " + self.email)
    # Add e-mail logic here

class EmailableContact(Contact, MailSender):
    pass

# e = EmailableContact("John Smith", "jsmith@example.net")
# e.send_mail("Hello, test e-mail here")

# using the contextmanager decorator 
# make objects/functions capable of use in with statements by using the contextlib built in modle 
# example - elevate the log level of a function temporarily by using a context manager
@contextmanager 
def debug_logging(level):
    logger = logging.getLogger()
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield logger 
    finally:
        logger.setLevel(old_level)

# The yield expression is the point at which the with block’s contents will execute. Any
# exceptions that happen in the with block will be re-raised by the yield expression for
# you to catch in the helper function

# usage 
with log_level(logging.DEBUG, 'my-log') as logger:
    logger.debug('This is my message')
    logging.debug('This will not print')


'''
monkey patching
'''
# changing a class or module at runtime without touching the source code 
# for example replace or add methods (using functions as attributes) at run time 
def set_card(deck, position, card):
    deck._cards[position] = card 

FrenchDeck.__setitem__ = set_card 
shuffle(deck)

# The trick is that set_card knows that the deck object has an attribute named _cards,
# and _cards must be a mutable sequence. The set_card function is then attached to the
# FrenchDeck class as the __setitem__ special method


##################################################
# Operator Overloading 
##################################################

# negation
__neg__

# plus
__pos__

# inverse
__invert__

def __abs__(self):
    return math.sqrt(sum(x*x for x in self))

def __neg__(self):
    return Vector(-x for x in self)

def __pos__(self):
    return Vector(self)

# overwrriding scalar multiplication
def __mul__(self, scalar):
    return Vector(n * scalar for n in self)

# implementing equal 
def __eq__(self, other):
    if isinstance(other, Vector):
        return (len(self)==len(other)) and 
                all(a==b for a, b in zip(self, other))
    else:
        return NotImplemented 

