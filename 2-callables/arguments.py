##################################################
# Arguments 
##################################################

'''
positional arguments
'''
# assign arguments to parameters via the order in which they are passed

# a positional arguments can be made optional by specifying a default value for the corresponding parameter

def my_func(a, b=100):
    pass

my_func(10, 20)
my_func(10)

# if a positional parameter is defined with a default value
# then every positional parameter after it must also be given a default value

def my_func(a, b=5, c=10):
    pass

# positional arguments can optionally be specified by using the parameter name whether or not the parameters have default values

def my_func(a, b, c):
    pass


my_func(1, 2, 3)
my_func(1, 2, c=3)
my_func(a=1, b=2, c=3)
my_func(c=3, a=1, b=2) # the order doesn't matter with named



'''
keyword arguments
'''

# named arguments
my_func(a=1, c=2)

# Once you use a named arguments, all arguments thereafter must be named too

# keyword arguments
# positional parameters can optionally be passed as named arguments
# but sometimes want keyword arguments mandatory
# to do so, we create parameters after the positional parameters have been exhausted


'''
unpacking iterables
'''
# packed values are values that are bundled together
# iterables - like tuples and lists are packed values
# unpacking is the act of splitting packed values into individual variables contained in a list or tuple
# this unpacking is based on the relative positions of each element
a = 10
b = 20

a, b = b, a # unpacking to swap values
# in python the entire RHS is evaluated first and completely then assignments are made to the LHS

# unpacking sets and dictionaries
# when we unpack d, we are unpacking the keys of d
# dictionaries are unordered types, then can be iterated, but there is no guarantee the order of the results will match yours

'''
extended unpacking
'''
d = {'key1': 1, 'key2': 2, 'key3': 3}


l = [0, 1, 2]
l2 = (-10, 5, 2)
a, *b = l
a, *b = l2 # b is still a list, unpacking always return a list

a, *b = 'XYZ' # b = ['Y', 'Z']
a, b, *c, d = 1, 2, 3, 4, 5 # a = 1, b = 2, c = [3, 4], d = 5

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l = [*l1, *l2]

# usage with unordered types should be avoided, especially sets and dictionaries have no ordering

# using **
d1 = {'p': 1, 'y': 2}
d2 = {'p': 3, 'h': 4}

d = {**d1, **d2} # ** operator can only be used in RHS
# {'p': 3, 'y': 2, 'h': 4}

d1 = {'a': 1, 'b': 2}
{'a': 10, 'c': 3, **d1} # {'a': 1, 'c': 3, 'b': 2}


'''
*args, **kwargs (extended arguments)
'''

# *args exhausts positional arguments - variable amount of remaining positional arguments. args returns a tuple
# **kwargs is used to scoop up a variable amount of remaining keyword arguments. kwargs returns a dictionary

# *args: catch-all for any optional additional positional arguments
def avg(*args):
    count = len(args)
    total = sum(args)
    return count and total / count


def func(**kwargs):
    pass

func(a=1, b=2, c=3) # kwargs = {'a': 1, 'b': 2, 'c': 3}


def func(positional, keyword=value, *args, **kwargs):
    pass 

# Positional arguments are mandatory and have no default values.
# Keyword arguments are optional and have default values.
# An arbitrary argument list is optional and has no default values.
# An arbitrary keyword argument dictionary is optional and has no default values.



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

# default values are evaluated at the moment of being imported (when module executes)
# below code dt is executed when the function is defined
from datetime import datetime


def log(msg, *, dt=datetime.utcnow()):
    print('{0}: {1}'.format(dt, msg))

# solution - set a default to None
# inside the function, check if the argument dt is still None, if dt is None, set it to the current data/time

def log(msg, *, dt=None):
    dt = dt or datetime.utcnow()
    print('{0}: {1}'.format(dt, msg))

# generally be aware of using a mutable object for an argument default
# if default value is supposed to be a mutable container (list, set, ord dict) 
# then use None
def spam(a, b=None):
    if b is None:
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

# solution to the problem
# assign to None
def append_to(element, to=None):
    if to is None:
        to = []
    to.append(element)
    return to 

# utilize this mutable default parameter to cache results
def factorial(n, cache={}):
    if n < 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        result = n * factorial(n-1, cache=cache)
        cache[n] = result
        return result 

factorial(3)



'''
signature (inspect pacakge)
'''
from clip import clip 
from inspect import signature 
sig = signature(clip)
sig 
for name, param in sig.parameters.items():
    print(param.kind, ":", name, "=", param.default)

