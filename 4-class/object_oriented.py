##################################################
#  Object Oriented
##################################################

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

# encapsulating using the @property decorator
# converts a method to something like an attribute (similar to a get method)
@property
def celsius(self): # getter function
    return self._celsius

@celsius.setter
def celsius(self, value):
    self._celsius = value 

class Example:
    @property
    def p(self):
        return self._p 
    @p.setter 
    def p(self, value):
        self._p = value

# @property with inheritance
def volume_ft3(self):
    return super().volume_ft3 - RefrigeratedShippingContainer.FRIDGE_VOLUME_FT3

# template method


# strings and representations
# functions for making string representations 

# produces an unambiguous string representation of an object
# exactness more importan - good for debugging and logging 
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

# format options 
__format__


##################################################
#  Decorators 
##################################################

# A decorator is a callable that takes another function as argument (the decorated function).
# The decorator may perform some processing with the decorated function, and returns it or replaces it with another function or callable object.

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


# >>> target()
# running inner()  Invoking the decorated target actually runs inner.
# >>> target
# <function deco.<locals>.inner at 0x10063b598>  Inspection reveals that target is a now a reference to inner.

# A key feature of decorators is that they run right after the decorated function is defined.
# That is usually at import time (i.e., when a module is loaded by Python).


# Another Decorator Example

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
@functools.lru_cache()
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
classmethod vs. staticmethod
'''
# to define a method that operates on the class and not on instances. classmethod changes the way the method is called,
# so it receives the class itself as the first argument, instead of an instance. Its most common use is for alternative constructors

@classmethod
def frombytes(cls, octets):
    typecode = chr(octets[0])
    memv = memoryview(octets[1:]).cast(typecode)
    return cls(*memv)

# In contrast, the staticmethod decorator changes a method so that it receives no special
# first argument. In essence, a static method is just like a plain function that happens to
# live in a class body, instead of being defined at the module level.

class Demo:
    @classmethod
    def klassmeth(*args):
        return args
    @staticmethod
    def statmeth(*args):
        return args 

# Demo.klassmeth()
# Demo.klassmeth('spam')


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
>>> l1 = [3, [55, 44], (7, 8, 9)]
>>> l2 = list(l1)
>>> l2 == l1
True 
>>> l2 is l1
False 

# Using the constructor or [:] produces a shallow copy (i.e., the outermost
# container is duplicated, but the copy is filled with references to the same items held by
# the original container). 


# Deep copy
# Working with shallow copies is not always a problem, but sometimes you need to make
# deep copies (i.e., duplicates that do not share references of embedded objects). The copy
# module provides the deepcopy and copy functions that return deep and shallow copies
# of arbitrary objects


# Weak References 
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
If you are dealing with millions of instances with few attributes, the
__slots__ class attribute can save a lot of memory, by letting the interpreter store the
instance attributes in a tuple instead of a dict.

class Vector2d:
    __slots__ = ('__x', '__y')
    typecode = 'd'
    # methods follow 



##################################################
#  Private vs. Public Attributes
##################################################

# The single underscore prefix has no special meaning to the Python interpreter when
# used in attribute names, but it’s a very strong convention among Python programmers
# that you should not access such attributes from outside the class.

