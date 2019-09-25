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
    def __init_-(self, x, y):
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
# 2 The decorator may perform some processing with the decorated function, and
# returns it or replaces it with another function or callable object.

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
    print(running target())

# >>> target()
# running inner()  Invoking the decorated target actually runs inner.
# >>> target
# <function deco.<locals>.inner at 0x10063b598>  Inspection reveals that target is a now a reference to inner.

# A key feature of decorators is that they run right after the decorated function is defined.
# That is usually at import time (i.e., when a module is loaded by Python).

''' 
Decorator Enhanced Strategy Pattern 
'''




##################################################
#  Closures 
##################################################