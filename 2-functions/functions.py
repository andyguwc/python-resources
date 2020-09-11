##################################################
#  Functions Basics
##################################################

'''
Function as Object
'''

# functions are first class objects, i.e.
#  - created at runtime
#  - assigned to a variable or element in a data structure
#  - passed as an argument to a function
#  - returned as the result of a function 


# Create and test a function, then read its __doc__ and check its type
def factorial(n):
    '''returns n!'''
    return 1 if n < 2 else n * factorial(n-1)
# >>> factorial(42)
# 1405006117752879898543142606244511569936384000000000
# doc is one of several attributes of function objects 
# >>> factorial.__doc__ 
# 'returns n!'
# factorial is an instance of the function class 
# >>> type(factorial)
# <class 'function'>

def yell(text):
    return text.upper() + '!'

bark = yell 

funcs = [bark, str.lower, str.capitalize]

for f in funcs:
    print(f, f('hey here'))

# functions can be passed to other functions 
def greet(func):
    greeting = func("Hi, a Python program")
    print(greeting)





'''
Variables and Parameters 
''' 
# variables and parameters are local 

# default value
# default value is determined at the time that the function is defined, not at the time that it is invoked. 
initial = 7
def f(x, y =3, z=initial):
    print("x, y, z, are: " + str(x) + ", " + str(y) + ", " + str(z))


# deep and shallow copies
# When you copy a nested list, you do not also get copies of the internal lists. 
# This means that if you perform a mutation operation on one of the original sublists, the copied version will also change.


##################################################
# Arguments 
##################################################

'''
args, kwargs (extended arguments)
'''
def func(positional, keyword=value, *args, **kwargs):
    pass 

# Positional arguments are mandatory and have no default values.
# Keyword arguments are optional and have default values.
# An arbitrary argument list is optional and has no default values.
# An arbitrary keyword argument dictionary is optional and has no default values.

# * returns tuple
# ** returns dictionary 

def hypervolume(length, *lengths): # accept a number of arguments with a lower bound
    print(lengths)
    print(type(lengths)) # tuple
    v = length
    for item in lengths:
        v*=length
    return v


def foo(required, *args, **kwargs):
    print(kwargs)
    print(type(kwargs)) # dictionary

foo('hello', 1, 2, 3, key1='value', key2=999)


def foo(arg1, arg2, *args, kwarg1, kwarg2, **kwargs):
    print(args)
    print(kwargs) 


# modify the arguments before passing to another function 
def foo(x, *args, **kwargs):
    kwargs['name'] = 'Alice'
    new_args = args + ('extra', )
    bar(x, *new_args, **kwargs)


# extended call syntax
def print_args(arg1, arg2, *args):
    print(args)

t = (1,2,3,4)
print_args(*t)
# (3, 4)


def print_args(arg1, arg2, **kargs):
    print(kargs)

k = {'arg1': 'a', 'arg2': 'b', 'c': 'd'}
print_args(**k)
# {'c': 'd'}

# common use case is to forward arguments

def trace(f, *args, **kwargs):
    result = f(*args, **kwargs)
    print("result= ", result)
    return result


# You can use the items from a sequence as the positional arguments for a function with the * operator.
# Using the * operator with a generator may cause your program to run out of memory and crash.
# Adding new positional parameters to functions that accept *args can introduce hard-to-find bugs.

# keyword arguments
# benefits
# make the caller clearer to reader
# have default values specified
# backwards compatible 

def function_name(arg1, arg2=8):
    # arg1 is positional argument, and arg2 is keyword argument, and 8 is default value
    pass


# function that accepts any uber of positional arguments
# rest is a tuple of all the extra positional arguments passed
def avg(first, *rest):
    return (first+sum(rest)) / (1+len(rest))

# example using arbitrary keyword arguments in configuration setups 
class Options:
    default_options = {
        'port': 21, 
        'host': 'localhost',
        'username': None, 
        'password': None, 
        'debug': False, 
    }

    def __init__(self, **kwargs):
        self.options = dict(Options.default_options)
        self.options.update(kwargs)
    
    def __getitem__(self, key):
        return self.options[key]


'''
default args
'''
# default values are evaluated at the moment of being imported
# if default value is supposed to be a mutable container (list, set, ord dict) 
# then use None
def spam(a, b=None):
    if be is None:
        b = []

# the values assigned as a default are bound only once at the time of function definition.
# not at each time the function is called 

# bad example 
def append_to(element, to=[]):
    to.append(element)
    return to

my_list = append_to(12)
print(my_list)
# returns [12]

my_other_list = append_to(42)
print(my_other_list)
# returns [12, 42]

# good example
def append_to(element, to=None):
    if to is None:
        to = []
    to.append(element)
    return to 




'''
signature (inspect pacakge)
'''
from clip import clip 
from inspect import signature 
sig = signature(clip)
sig 
for name, param in sig.parameters.items():
    print(param.kind, ":", name, "=", param.default)



##################################################
# Callable Objects 
##################################################

# The call operator (i.e., ()) may be applied to other objects beyond user-defined functions. __call__() # call method

# To determine whether an object is callable, use the callable() built-in function.
# callable instances
callable(some_object) # checks if something is callable

# following callable types 
#  - user defined functions, def and lambda 
#  - built in functions
#  - built in methods 
#  - methods, functions define in the body of a class 
#  - classes: when invoked, class runs its __new__ method to create an isntance, then __init__ to initialize it 
#  - class instances: if a class defines a __call__ method then instances can be invoked as functions
#  - generator functions: functions or methods that use the yield keyword. When called, generator functions return a generator object

def sequence_class(immutable):
    return tuple if immutable else list 

seq = sequence_class(immutable=False)

# implement cache for a callable instance
class Resolver:
    def __init__(self):
        self._cache = {}
    
    def __call__(self, host):
        if host not in self._cache:
            self._cache[host] = socket.gethostname(host)
        return self._cache[host]
    
    def clear(self):
        self._cache.clear()
    
    def has_host(self, host):
        return host in self._cache


# classes are also callable, and ClassName() invokes constructor (__init__)
class Adder:
    def __init__(self, n):
        self.n = n 
    
    def __call__(self, x):
        return self.n + x
    
plus_3 = Adder(3)
plus_3(4)


# using callable() to detect callable 
def is_even(x):
    return x % 2 == 0
callable(is_even)

is_odd = lambda x: x % 2 == 1

callable(is_odd)

# class can be made a callable with the __call__ method
add_me = Adder()
callable(add_me)


##################################################
# High-Order Functions
##################################################

# A function that takes a function as argument or returns a function as the result is a
# higher-order function.

# map takes a function object and an iterable, and then calls the function 
# on each element in the iterable, yielding the results as it goes along.

# example: map, filter, reduce, apply
list(map(fact, range(6)))

[fact(n) for n in range(6)]



# example: sorted function which take an optional key argument 
# pass the len function as the key
sorted(fruits, key=len)
# any one-argument function can be used with a key 
def reverse(word):
    return word[::-1]
sorted(fruits, key=reverse)


# Nested functions

def speak(text):
    def whisper(t):
        return t.lower() + '...'
    return whisper(text)


##################################################
# Lambda Functions
##################################################

# lambda functions
# same as anonymous functions
sorted(scientists, key=lambda name: name.split()[-1]) # creating a callable function using lambda

tuples = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]
sorted(tuples, key=lambda x: x[1])


# the inputs to lambda expression is a free variable that get bound at runtime not definition time



##################################################
# Local Functions / Namespace 
##################################################

# functions defined within the scope of other functions
def sort_by_last_letter(strings):
    def last_letter(s): # function is created each time def is called
        return s[-1]
    return sorted(strings, key=last_letter)

# uselful for specialized, one-off functions
# aid in code organization and readability
# similar to lambdas but more general

# functions can be treated like any other oject
# closures - maintain references to objects from earlier scopes 


# function factories - functions that return new, specialized functions
def raise_to(exp):
    def raise_to_exp(x):
        return pow(x, exp)
    return raise_to_exp


'''
local vs. global
'''

# LEGB
# first checking local scope, then enclosing scope, then global, finally built-in
# global keyword - introduces names from the enclosing namespace into the local namespace 
# nonlocal - introduce names from enclosing namespace into the local namespace

messsage = 'global'

def enclosing():
    message = 'enclosing'
    def local():
        message = 'local'

enclosing()
print(message) # 'global'

# global
# if want local functions to modify global variables 
messsage = 'global'

def enclosing():
    message = 'enclosing'
    
    def local():
        # use global binding 
        global message
        message = 'local'
    
    local()

enclosing()
print(message) # 'local'

# nonlocal
# if want to introduce names from the enclosing namespace into the local (i.e. let local change enclosing)
message = 'global'

def enclosing():
    message = 'enclosing'
    
    def local():
        # searches for enclosing binding from inner most to outer
        nonlocal message
        message = 'local'

    print('enclosing message', message)
    local()
    print('enclosing message', message)
 
print(message) # 'global'
enclosing() # enclosing, local

# Python does not require you to declare variables,
# but assumes that a variable assigned in the body of a function is local.


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


'''
factory function
'''

def raise_to(exp):
    def raise_to_exp(x):
        return pow(x, exp)
    return raise_to_exp

cube = raise_to(3)
cube(5) # 125


##################################################
# Decorators
##################################################

'''
decorators
'''
# modify or enhance functions without changing their definition (calling code does not need to change)
# implemented as callables that take and return other callables 

@my_decorator 
def my_function(x,y): # function object
    return x+y

# example of defining a decorator which puts things as unicode
# takes function f and returns wrap, which is a similar function to f 
def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)
    return wrap

@escape_unicode
def northern_city():
    return 'Tromse'

'''
class as decorators
'''
# classes as decorators as long as it implements __call__ (class instance is a callable)
# example, class CallCount which counts how many times function is called
class CallCount:
    def __init__(self, f): # init new instance
        self.f = f
        self.count = 0 
    
    def __call__(self, *args, **kwargs): # makes it a callable wrap function 
        self.count +=1
        return self.f(*args, **kwargs)

@CallCount
def hello(name):
    print('Hello, {}'.format(name))


class Trace:
    def __init__(self):
        self.enabled = True
    
    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print(f'Calling {f}')
            return f(*args, **kwargs)
        return wrap

tracer = Trace()

@tracer
def northern_city():
    return 'Tromse'

# >>> northern_city()
# Calling <function northern_city at 0x109849400>
# 'Tromse'
# >>> tracer.enabled = False
# >>> northern_city()
# 'Tromse'
# >>> 

'''
multiple decorators
'''

@decorator1
@decorator2
def some_func():
# first passed to decorator2 then passed to decorator1

'''
functools.wraps
'''
# naive decorators can lose important metadata
import functools
functools.wraps()
# properly update metadata on wrapped functions

# get metadata like below
hello.__name__
hello.__doc__
help(hello)


def noop(f):
    @functiontools.wrap(f)
    def noop_wrapper():
        return f()
    noop_wrapper.__name__ = f.__name__
    noop_wrapper.__doc__ = f.__doc__
    return noop_wrapper

# example check non negatives of argments 
def check_non_negative(index):
    # below is a decorator function 
    def validator(f):
        def wrap(*args):
            if args[index]<0:
                raise ValueError('Argument {} must be non-negative.'.format(index))
            return f(*args)
        return wrap
    return validator

@check_non_negative(1)
def create_list(value, size):
    return [value] *size 


##################################################
# Closures
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


# Replacing Single Method classes with functions using closures 

# Closure is just like a function but wiht an extra environment of the variables taht are used inside the function

from urllib.request import urlopen 

class UrlTemplate:
    def __init__(self, template):
        self.template = template 
    def open(self, **kwargs):
        return urlopen(self.template.format_map(kwargs))

# example use 
yahoo = UrlTemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
for line in yahoo.open(names='IBM,AAPL,FB', fields='sl1c1v'):
    print(line.decode('utf-8'))

# replacing with a closure function 
def urltemplate(template):
    def opener(**kwargs):
        return urlopen(template.format_map(kwargs))
    return opener 

# example use 
yahoo = urltemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
for line in yahoo(names='IBM,AAPL,FB', fields='sl1c1v'):
    print(line.decode('utf-8'))

# There are really two main approaches that are useful for capturing and carrying state.
# You can carry it around on an instance (attached to a bound method perhaps) or 
# you can carry it around in a closure (an inner function).


##################################################
# Function Introspection
##################################################

# Like the instances of a plain user-defined class, a function uses the __dict__ attribute
# to store user attributes assigned to it

# Within a function object, the __defaults__ attribute holds a tuple with the default
# values of positional and keyword arguments. The defaults for keyword-only arguments
# appear in __kwdefaults__. The names of the arguments, however, are found within the
# __code__ attribute, which is a reference to a code object with many attributes of its own.

'''
__dict__
'''
# Like the instances of a plain user-defined class, a function uses the __dict__ attribute
# to store user attributes assigned to it. This is useful as a primitive form of annotation.



##################################################
# Functional Programming
##################################################
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


'''
partial (functools)
'''
# allows partial application of a function 
# using partial to use a two-argument function where a one-argument callable is required
from operator import mul 
from functools import partial 
triple = partial(mul, 3) # binding the first positional argument to 3 
triple(7)
list(map(triple, range(10)))


##################################################
# Function Annotations
##################################################
# attach metadata to the parameters of a function declaration and its return value 
def clip(text:str, max_len:'int > 0'=80) -> str:
    """Return text clipped at the last space before or after max_len
    """
    pass 

# python store the annotations in the __annotations__ attribute 



##################################################
# Function Hooks
##################################################

# Many of Python’s built-in APIs allow you to customize behavior by passing in a function.
# These hooks are used by APIs to call back your code while they execute. For example, the
# list type’s sort method takes an optional key argument that’s used to determine each
# index’s value for sorting

names = [‘Socrates’, ‘Archimedes’, ‘Plato’, ‘Aristotle’]
names.sort(key=lambda x: len(x))
print(names)

# similarly, we can customize the behavior of the defaultdict class 
# This data structure allows you to supply a function that will be called each time a missing key is accessed.
# The function must return the default value the missing key should have in the dictionary.

def log_missing():
    print('key added')
    return 0 

current = {‘green’: 12, ‘blue’: 3}
increments = [
    (‘red’, 5),
    (‘blue’, 17),
    (‘orange’, 9),
] 
result = defaultdict(log_missing, current)


'''
unpacking
'''
# unpacking
filename, ext = "my_photo.orig.png".rsplit(".", 1)

# nested unpacking
a, (b, c) = 1, (2, 3)

# swapping
a, b = b, a

# arbitrary
a, *middle, c = [1, 2, 3, 4]

# ignoring
basename, _, ext = filename.rpartition('.')




##################################################
# References
##################################################


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



