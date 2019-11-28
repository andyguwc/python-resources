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
# Callable Objects 
##################################################

# The call operator (i.e., ()) may be applied to other objects beyond user-defined functions.
# To determine whether an object is callable, use the callable() built-in function.
# callable instances

# following callable types 
#  - user defined functions, def and lambda 
#  - built in functions
#  - built in methods 
#  - methods, functions define in the body of a class 
#  - classes: when invoked, class runs its __new__ method to create an isntance, then __init__ to initialize it 
#  - class instances: if a class defines a __call__ method then instances can be invoked as functions
#  - generator functions: functions or methods that use the yield keyword. When called, generator functions return a generator object

__call__() # call method


##################################################
# High-Order Functions
##################################################

# A function that takes a function as argument or returns a function as the result is a
# higher-order function.

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




##################################################
# Lambda Functions
##################################################

# lambda functions
# same as anonymous functions
sorted(scientists, key=lambda name: name,split()[-1]) # creating a callable function using lambda

# using callable() to detect callable 
def is_event(x):
    return x % 2 == 0
callable(is_event)

# the inputs to lambda expression is a free variable that get bound at runtime not definition time



##################################################
# Arguments 
##################################################

'''
args, kwargs (extended arguments)
'''
# * returns tuple
# ** returns dictionary 

def hypervolume(length, *lengths): # accept a number of arguments with a lower bound
    v = length
    for item in lengths:
        v*=length
    return v

# You can use the items from a sequence as the positional arguments for a function
# with the * operator.
# Using the * operator with a generator may cause your program to run out of
# memory and crash.
# Adding new positional parameters to functions that accept *args can introduce
# hard-to-find bugs.


# keyword arguments
# benefits
# make the caller clearer to reader
# have default values specified
# backwards compatible 

def function_name(arg1, arg2=8):
    # arg1 is positional argument, and arg2 is keyword argument, and 8 is default value
    pass

def extended(*args, **kwargs): 
    # args is passed as a tuple

    # kwargs a dictionary
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
# if default value is supposed to be a mutable container (list, set, ord dict) then use None
def spam(a, b=None):
    if be is None:
        b = []

# the values assigned as a default are bound only once at the time of function definition.
def decode(data, default={}):
    try:
        return json.loads(data)
    except ValueError:
        return default 

# foo and bar are equal to the default parameter
# and the default parameter is evaluated only once so foo=bar 
foo = decode(‘bad data’)
foo[‘stuff’] = 5
bar = decode(‘also bad’)
bar[‘meep’] = 1
print(‘Foo:’, foo)
print(‘Bar:’, bar)



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
# Local Functions 
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

# LEGB
# global keyword - introduces names from the enclosing namespace into the local namespace 
# nonlocal - introduce names from enclosing namespace into the local namespace



##################################################
# Decorators
##################################################

# decorators
# modify or enhance functions without changing their definition
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

# other objects (callables) can be decorators as well 
# classes as decorators
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


# instances as decorators


# multiple decorators
@decorator1
@decorator2
def some_func():
# first passed to decorator2 then passed to decorator1

# naive decorators can lose important metadata
# help() only shows the wrapper function not the original function
# so have to update the __name__ and __doc__ 
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


