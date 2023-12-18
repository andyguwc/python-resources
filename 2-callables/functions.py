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

# high order functions
# high-order functions are functions taht 
#  - take a function as an argument
#  - and/or return a function

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


'''
Docstrings and Annotations
'''
# the docstrings and annotations do not change how the code is executed
# mainly used by external tools and modules

# help(x) returns some documentation for x (x be a function or module or class)
# we can document the functions to achieve the same result using docstrings

def my_func(a):
    "documentation for my_func"
    return a

# docstrings are stored in the function's __doc__ property

# function annotations
# annotations can be any expression
def my_func(a: str, b: 'int > 0') -> str:
    return a * b

def my_func(a: str = 'xyz', b: int = 1) -> str:
    pass

# annotations are stored in the __annotations__ property of the function
# dictionary keys are the parameter names and values are the annotations
# my_func.__annotations__
# {'a': <class 'str'>, 'b': <class 'int'>, 'return': <class 'str'>}

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


# using callable to make it easier to call from other API
class BettingStrategy:
    def __init__(self):
        self._win = 0
        self._loss = 0
    
    @property
    def win(self):
        return self._win

    @win.setter
    def win(self, value):
        self._win = value
    
    @property
    def loss(self):
        return self._loss
    
    @loss.setter
    def loss(self, value):
        self._loss = value

    def __call__(self):
        return 1
    

# we can use the above BettingStrategy
def win(self, amount):
    self.bet.win += 1
    self.stake += amount
    
# when player placing a bet can use something like this
def initial_bet(self):
    return self.bet()

bt = BettingStrategy()


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
# Lambda Expressions
##################################################
# lambda expressions are also called anonymous functions
# lambda [parameter list]: expression
# the expression is evaluated and returned when the lambda function is called
lambda x: x*2
lambda x, y: x + y
lambda s: s[::-1].upper()

# the inputs to lambda expression is a free variable that get bound at runtime not definition time

# passing as an argument to another function

def apply_func(x, fn):
    return fn(x)

apply_func(3, lambda x: x **2)


# limitations
# the body of a lambda function is limited to a single epxression
# no assignments and no annotations

# lambda functions and sorting
l = ['c', 'B', 'D', 'a']
sorted(l) # ['B', 'D', 'a', 'c']
sorted(l, key=lambda s: s.upper()) # ['a', 'B', 'c', 'D']

sorted(scientists, key=lambda name: name.split()[-1]) # creating a callable function using lambda

tuples = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]
sorted(tuples, key=lambda x: x[1])


##################################################
# Scope
##################################################

'''
scopes and namespaces
'''
# the variable points to some object - the variable is bound to that object
# the variable name and its binding only exists in specific parts of our code (scope). These bindings are stored in namespaces.


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

# the global scope is essentially the module scope. It spans a single file. 
# global scopes are nested inside the built-in scope

# local scope
# when we create functions, we can create variable names inside those functions (using assignments)
a = 10
# variables defined inside a function are not created until the function is called
# every time the function is called, a new scope is created
# once a function finished, the scope goes away too
# scopes are nested: local scope -> module scope -> buit-in scope

'''
global keyword
'''
# accessing global scope from a local scope
# we can tell python that a variable is meant to be scoped in the global scope by using the global keyword

# below the local variable a masks the global variable a
a = 0

def my_func():
    a = 100 # assignment, interprets this as a local variable during compile time
    print(a)


a = 10
def my_func():
    print(a) # a is referenced only in entire function at compile time - a non-local

a = 0
def my_func():
    global a
    a = 100

my_func()
print(a) # 100

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


'''
nonlocal
'''
# inner functions
# inner_func is nested within the scope of outer_func

# both functions have access to global and built-in scopes and their respective local scopes
# but the inner function also has access to its enclosing scope - the scope of the outer function
# that scope is called nonlocal


def outer_func():
    a = 10

    def inner_func():
        print(a) # a is nonlocal

    inner_func()

outer_func()


# declaring a variable nonlocal
# it will look for it in the enclosing local scopes until it encounters the specified variable name
# it will not look in the global scope

def outer_func():
    x = 'hello'

    def inner_func():
        # explicitly tell python we are modifying a nonlocal variable
        nonlocal x
        x = 'python'

    inner_func()
    print(x)
# outer_func() -> python


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
# Closures
##################################################

'''
closure
'''
# A closure is a function with an extended scope that encompasses nonglobal variables referenced in the body of the function but not defined there. 
# It does not matter whether the function is anonymous or not; what matters is that it can access nonglobal variables that are defined outside of its body.

# value of x is shared between two scopes: outer and the closure
# the label x is in two different scopes but always reference the same "value"
# python does this by creating a cell as an intermediary object
# every time the function in the closure is called and the free variable is referenced, python looks up the cell object and then whatever the cell is pointing to 


def outer():
    # value of x is shared between two scopes: outer and the closure
    x = 'python'
    def inner():
        # x is a free variable in inner that is bound to variable x in outer
        print("{0} rocks".format(x))
    
    return inner # we are returning the closure

fn = outer() # outer finished running, the scope is gone
fn() # when called fn, python determined the value of x in the extended scope

def outer():
    a = 100
    x = 'python'
    def inner():
        a = 10
        print("{0} rocks".format(x))
    return inner

# fn = outer()
# >>> fn.__closure__
# (<cell at 0x108e363d0: str object at 0x108ea7bb0>,)

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

'''
mulitple instances of closures
'''
# every time we run a function, a new scope is created
# if that function generates a closure, a new closure is created every time as well

def counter():
    count = 0

    def inc():
        nonlocal count
        count += 1
        return count

    return inc

f1 = counter()
f2 = counter() # a different closure

'''
shared scopes
'''

def adder(n):
    def inner(x):
        return x + n
    return inner


add_1 = adder(1)
add_2 = adder(2)

# these are separate closures
add_1.__closure__
add_2.__closure__ # different cells and variables

adders = []

# n in shared across scopes, as a global variable
for n in range(1, 4):
    adders.append(lambda x: x + n)

adders[0].__closure__
adders[1].__closure__

'''
closure applications
'''

# oftentimes what's written as a class can be writter as a closure


class Averager:
    """for calculating averages
    """
    def __init__(self):
        self.total = 0
        self.count = 0

    def add(self, number):
        self.total += number
        self.count += 1
        return self.total / self.count

def averager():
    numbers = []

    def add(number):
        numbers.append(number)
        total = sum(numbers)
        count = len(numbers)
        return total / count

    return add


def averager():
    total = 0
    count = 0
    def add(number):
        # make total nonlocal
        nonlocal total
        nonlocal count
        total = total + number
        count = count + 1
        return total / count
    
    return add

a = averager()
a(10)
a(20)
a(30)

# For timer
from time import perf_counter
from typing import Any

class Timer:
    def __init__(self):
        self.start = perf_counter()

    def __call__(self):
        return perf_counter() - self.start

t1 = Timer()
t1() # callable


# use closure instead of class
def timer():
    start = perf_counter()
    def poll():
        return perf_counter() - start
    
    return poll

t2 = timer()
t2()


def counter(initial_value=0):
    def inc(increment=1):
        nonlocal initial_value
        initial_value += increment
        return initial_value
    return inc


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
# as first class objects, functions have attributes

# dir is a built-in function that, given an object as an argument, will return a list of valid attributes for that object
dir(my_func)


# Like the instances of a plain user-defined class, a function uses the __dict__ attribute
# to store user attributes assigned to it

# __name__ is the name of hte function
# Within a function object, the __defaults__ attribute holds a tuple with the default
# values of positional and keyword arguments. The defaults for keyword-only arguments
# appear in __kwdefaults__. The names of the arguments, however, are found within the
# __code__ attribute, which is a reference to a code object with many attributes of its own.

'''
__code__
'''
# The __code__ object itself has various properties

# co_varnames: parameters and local variables
# co_argcount: number of parameters


'''
__dict__
'''
# Like the instances of a plain user-defined class, a function uses the __dict__ attribute
# to store user attributes assigned to it. This is useful as a primitive form of annotation.


'''
inspect
'''

import inspect

inspect.ismethod(my_func)
inspect.isfunction(my_func)

# classes and objects have attributes - an object that is bound (to the class or the object)
# an attribute that is callable is called a method

# code instrospection
inspect.getsource(my_func) # a string containig entire def statement, including annotations, docstrings

# find out in which module the function was created
inspect.getmodule(my_func)

# function comments
inspect.getcomments(my_func)


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






