##################################################
#  Decorators / Wrapping 
##################################################

# A decorator function:
# - takes a function as an argument
# - returns a closure
# - the closure usually accepts any combination of parameters
# - runs some code in the inner function (closure)
# - the closure function calls the original function using the arguments
# - return whatever is returned by that function call

# A decorator is a callable that takes a callable as an argument (the decorated function) and returns a callable
# The decorator may perform some processing with the decorated function, and returns it or replaces it with another function or callable object.
# benefits
#  - improve maintainability 
#  - increase clarity
#  - reduce complexity 

# Use cases:
# • logging
# • enforcing access control and authentication
# • instrumentation and timing functions
# • rate-limiting
# • caching, and more

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


# this uppercase decorator defines a new function on the fly (a closure) and uses it 
# to wrap the input function in order to modify its behavior at call time

def uppercase(func):
    # @functools.wraps(func)
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper 

@uppercase
def greet():
    return 'hello'

# >>> greet()
# 'HELLO'


'''
multiple decorators
'''
# applied from bottom to top 

def strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'
    return wrapper

def emphasis(func):
    def wrapper():
        return '<em>' + func() + '</em>'
    return wrapper

@strong
@emphasis 
def greet():
    return 'Hello!'

# similar to greet = strong(emphasis(greet))

# >>> greet()
# '<strong><em>Hello!</em></strong>'


'''
arguments
'''

def trace(func):
    def wrapper(*args, **kwargs):
        print(f'TRACE: calling {func.__name__}() '
              f'with {args}, {kwargs}')
        original_result = func(*args, *kwargs)

        print(f'TRACE: {func.__name__}() '
              f'returned {original_result!r}')
        return original_result
    return wrapper 


'''
using functools.wraps
'''
# use @functools.wraps(func) in your own decorators to copy over the
# lost metadata (name, docstring, etc.) from the undecorated function to the decorator closure.

# The code inside a decorator typically involves creating a new function that accepts any arguments using *args and **kwargs, as shown with the wrapper() function in this recipe. 
# Inside this function, you place a call to the original input function and return its result. However, you also place whatever extra code you want to add (e.g., timing). The newly created function wrapper is returned as a result and takes the place of the original function.

# wraps function is itself a decorator

from functools import wraps

def counter(fn):
    count = 0

    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(count)
        return fn(*args, **kwargs)
    return inner

@counter
def mul(a, b, c):
    """Returns a product
    """
    return a * b * c

# help(mult) now still retains the original metadata

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


def debug(function):
    @functools.wraps(function)
    def logged_function(*args, **kwargs):
        logging.debug( "%s( %r, %r )", function.__name__, args, kw,)
        result = function(*args, **kw)
        logging.debug( "%s = %r", function.__name__, result )
        return result
    return logged_function 


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
Decorator Class
'''
def my_dec(a, b):
    def dec(fn):
        def inner(*args, **kwargs):
            print("decorated function called: a = {0}, b = {1}".format(a, b))
            return fn(*args, **kwargs)
        return inner

    return dec


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, fn):
        def inner(*args, **kwargs):
            print("decorated function called: a = {0}, b = {1}".format(self.a, self.b))
            return fn(*args, **kwargs)
        return inner

# obj = MyClass(10, 20) - the instance is itself callable

@MyClass(10, 20)
def my_func(s):
    print("Hello {0}".format(s))

'''
Decorating Classes
'''
# python allows modifying at runtime - monkeypatching
# add attributes dynamically

from fractions import Fraction

f = Fraction(2, 3)
# add a new attribute to Fraction
Fraction.speak = "something"
f.speak 

Fraction.speak = lambda self, message: "Fraction says {0}".format(message) 
f.speak("something")



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

# sequence is to run d1 first then run d2

def d1(fn):
    def inner():
        result = fn()
        print("running decorator 1")
        return result
    return inner


def d2(fn):
    def inner():
        result = fn()
        print("running decorator 2")
        return result
    return inner


@d1
@d2
def my_func():
    print("Running my_func")

my_func()
# running my_func
# running d2
# running d1

# first run the authorization, then run the logging
@auth
@logged
def save_resource():
    pass

''' 
Parameterized Decorators
'''

# Decorator that takes arguments
# reps is the extra parameter


# startegy is outer(10) will return a decorator
# it is a decoractor factory

def timed(reps):
    def dec(fn):
        from time import perf_counter

        @wraps(fn)
        def inner(*args, **kwargs):
            total_elapsed = 0
            # free variable bound to reps in outer
            for i in range(reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                total_elapsed += (perf_counter() - start)
            avg_elapsed = total_elapsed / reps
            print(avg_elapsed)
            return result
        
        return inner

    # this decorator knows what reps is
    return dec

@timed(10)
def my_func():
    pass



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
        log = logging.getLogger(logname)
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


# assuming we want a decorator to take argument like log_name 
# @debug('log_name')
# def some_function(args):
#     pass

def debug_named(log_name):
    def concrete_decorator(function):
        @functools.wraps(function)
        def wrapped(*args, **kw):
            log = logging.getLogger(log_name)
            log.debug( "%s( %r, %r )", function.__name__, args, kw, )
            result = function(*args, **kw)
            log.debug( "%s = %r", function.__name__, result )
            return result
        return wrapped
    return concrete_decorator


# Example: enforcing type checking
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
cached property
'''
# the cached_property subclasses the property class 

class cached_property(property):
    """A decorator that converts a function into a lazy property. The
    function wrapped is called the first time to retrieve the result,
    and then that calculated result is used the next time you access
    the value
    """
    def __init__(self, func, name=None, doc=None):
        self.__name__ = name or func.__name__
        self.__module__ = func.__module__
        self.__doc__ = doc or func.__doc__
        self.func = func
    
    def __set__(self, obj, value):
        obj.__dict__[self.__name__] = value 

    def __get__(self, obj, type=None):
        if obj is None:
            return self
        value = obj.__dict__.get(self.__name__, _missing)
        if value is _missing:
            value = self.func(obj)
            obj.__dict__[self.__name__] = value
        return value

class Foo(object):
    @cached_property
    def foo(self):
        print("You have just called Foo.foo()!")
        return 42

# >>> bar = Foo()
# >>> bar.foo
# You have just called Foo.foo()!
# 42
# >>> bar.foo 
# 42


'''
Applying decorators to Class and Static Methods
'''

# almost identical to a decorator for a standalone function
# in the definition, make sure explicitly name the self variable

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
        
'''
class decorators
'''

# loggers for each class 

def logged(class_):
    class_.loggger = logging.getLogger(class.__qualname__)
    return class_ 

@logged 
class SomeClass:
    def __init__(self):
        self.logger.info("new thing")
    
    def method(self, *args):
        self.logger.info("method %r", args)

# example like functools.total_ordering 
# can also add method functions to a class 
# two steps: creating the method function, and then inserting it into the class definition

def memento(class_):
    def memento(self):
        return "{0.__class__.__qualname__}({0!r})".format(self)
    class_.memento = memento
    return class_ 

@memento
class SomeClass:
    def __init__(self, value):
        self.value = value 

    def __repr__(self):
        return "{0.value}".format(self)


'''
decorator applications
'''

# logger decorator
from functools import wraps
from datetime import datetime, timezone

def logged(fn):

    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.now(timezone.utc)
        result = fn(*args, **kwargs)
        print('{0}: called {1}'.format(run_dt, fn.__name__))
        return result
    
    return inner


@logged
def func_1():
    pass

@logged
def func_2():
    pass


# memoization decorator
# decorators can modify the behvaior of a function

def fib(n):
    print("calculating fib({0})".format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)

# using cache
def fib():
    cache = {1: 1, 2: 1}

    def calc_fib(n):
        if n not in cache:
            cache[n] = calc_fib(n-1) + calc_fib(n-2)
        
        return cache[n]
    
    return calc_fib

f = fib()
f(10) # calculating fib with cache

# doesn't care about the function, just cache the outputs
def memoize(fn):
    cache = dict()
    def inner(n):
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]

    return inner

# decorator returned a closure and the closure is doing the caching
@memoize
def fib(n):
    print("calculating fib({0})".format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)


# just use lru_cache
# lru_cache also limits the cache size
from functools import lru_cache

@lru_cache(maxsize=None) # unlimited cache
def fib(n):
    return 1 if n < 3 else fib(n-1) + fib(n-2)


