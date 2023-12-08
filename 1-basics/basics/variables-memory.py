##################################################
# Variables
##################################################

'''
identifier names
'''

# identifier names are case-sensitive
# start with _ or (a-z, A-Z)

'''
conventions
'''
_my_var = 10

# _my_var indicate internal user or private objects
# objects named this way will not get imported by a statement like
# from module import * 

__my_var = 10
# class attributes, useful in inheritance chains

# __my_var__
# __init__
# used for system designed names that have a special meaning to the interpreter
# x < y --> x.__lt__(y)

'''
pep8 style guide
'''

# packages: short, all-lowercase names, no _, utilities
# modules: can have understores, db_utils, dbutils
# classes: CapWorld, NewClass
# functions: snake_case, open_account
# variables: snake_case, account_id
# constants: all-uppercase, MIN_APR


'''
memory references
'''
# Variables are memory references
# Can use more than one slot of memory address to store an object, just need to know where the object start in memory address
# Python Memory Manager stores memory in a heap

# We can find out the memory address referenced by a variable using the id() function
a = 10
id(a) # memory address of a
hex(id(a)) # hexadecimal


'''
reference counting
'''
a = 10
b = a # taking the reference of a and assign that to b, so both a and b are pointing to the same memory address
# hence the reference count is 2

import sys

sys.getrefcount(a) # finding the reference count, note this also increases the ref count by one since we are passing a to the function

b = a # ref count of a increases by 1
b = None # ref count of a decreases by 1

'''
garbage collection
'''
# if reference count goes down to 0, the var gets destroyed
# circular references present a challenge for reference counting
# causes memory leak

# that's where the garbage collector comes in and resolves the memory leak
# can be controlled programmatically using the `gc` module
# runs periodically on its own but can also call it manually


import ctypes
import gc

def ref_count(address):
    return ctypes.c_long.from_address(address).value


def object_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return "object exists"
    return "not found"


class A:
    def __init__(self):
        self.b = B(self)
        print('A: self: {0}, b: {1}').format(hex(id(self)), hex(id(self.b)))


class B:
    def __init__(self, a):
        self.a = a 
        print('B: self: {0}, a: {1}').format(hex(id(self)), hex(id(self.a)))

gc.disable()

my_var = A()

ref_count(a)
ref_count(b)

my_var = None # destroying the reference to my_var
gc.collect() # run the collector manually

'''
dynamic typing vs. static typing
'''
# static typing
# many languages are statically typed
# myVar is a variable of type String: String myVar = "hello"
# can't work when reassigning myVar = 10

# dynamic typing
# python is dynamically tu[ed
my_var = "hello" # a reference to a string object, no type attached
my_var = 10 # the variable my_var is now pointing to an integer object with value 10

# use type function to determine the type of the object currently referenced by a variable

type(my_var) # lookup the object my_var is referencing currently and print the type

# variable re-assignment - not changing the original value, just a new pointer to a new object


'''
mutability
'''

# changing the data inside the objectis called modifying the internal state of the object
# an object whose internal state can be changed is called mutable. An object whose internal state cannot be changed, is called immutable.

# Immutable
# Numbers (int, float, booleans), Strings, Tuples, Frozen Sets, User-Defined Classes
# For example, for Tuple, can't add, remove, or replace the elements

# Mutable
# Lists, Sets, Dictionaries
a = [1, 2]
t = (a,)

# did not change the element that is referenced (memory address)
# but can change the state of the object that is referenced.
a.append(3)
t # ([1,2,3],)
# therefore immutability doesn't mean this is frozen, this can still be changed because it contains mutable elements

'''
function arguments and immutability
'''

# immutable objects are safe from unintended side-effects
# for example, below function can't change the value of the string s

def process(s):
    s = s + "word"
    return s

my_var = "hello"
process(my_var) # my_var's reference is passed to process

# mutable objects are not safe from unintended side-effects

def process(lst):
    # this changes the lst value
    lst.append(100)

my_list = [1,2,3]
process(my_list)


def process(t):
    t[0].append(3)

my_tuple = ([1,2], "a")

process(my_tuple) # this modified the tuple since the list element is mutable 

'''
shared references and mutability
'''
# the concept of two variables referencing the same object in memory

# id(a) is the same as id(b) and both point to the same object in memory
# python's memory manager decides to automatically re-use memory references

a = 10
b = 10

# with mutable objects, python memory manager will never create shared references
a = "hello"
b = a
# id(a) and id(b) are different


'''
variable equality
'''
# Variable equality
# Are they pointing to the same Memory address
# object state (data) - i.e. same string, number, or elements in a list, using == equality operator, is != not equal operator
# memory address `is` using the identity operation - var_1 is var_2

a = 10
b = a 
a is b # true
a == b # true

a = 'hello'
b = 'hello'
a is b # true, python memory manager creates a shared reference
a == b # true

a = [1,2,3]
b = [1,2,3]
a is b # false, mutable objects, different memory addresses
a == b # same elements

a = 10
b = 10.0
a is b # false
a == b # true values are still equal

# None object is a real object that is managed by the python memory manager
# python memory manager always create a shared reference to None

'''
python optimizations
'''

# reusing objects on-demand
# at startup, python pre-loads (caches) a global list of intergers in the range [-5, 256]
# anytime an interger is referenced in that range, python will use the cached version

# singletons
# classes that can only be instantiated once
# optimization strategy - small integers show up often

a = 258
b = 258
a is b # false

a = 10
b = int(10) 
a is b #true

# string interning
# some strings are cached by python
# identifiers are interned - variable names, function names, class names
# checking memory addresses are equal is more efficient than comparing string character by character

