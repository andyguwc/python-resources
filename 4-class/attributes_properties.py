##################################################
# Attribute Access & Properties
##################################################

'''
attribute access
'''
# it's not required to provide all attributes in the __init__() method 
# optional attributes imply an informal subclass relationship 
# although it's better to have attributes added or deleted more clearly by creating a subclass 
# special methods for attribute access

# __getattr__(), __setattr__(), and __delattr__()

# The __setattr__() method will create and set attributes.
# The __getattr__() method will do two things. Firstly, if an attribute
# already has a value, __getattr__() is not used; the attribute value is
# simply returned. Secondly, if the attribute does not have a value, then
# __getattr__() is given a chance to return a meaningful value. If there is
# no attribute, it must raise an AttributeError exception.
# The __delattr__() method deletes an attribute.

# __getattribute__()
# An even lower level attribute processing is the __getattribute__() method.
# The default implementation attempts to locate the value as an existing attribute
# in the internal __dict__ (or __slots__). If the attribute is not found, it calls __getattr__() as a fallback.

# example using __getattribute__() to concecal the internal names (with _) from the __dict__
class BlackJackCard:
    def __init__(self, rank, suit):
        super().__setattr__( 'rank', rank )
        super().__setattr__( 'suit', suit )

    def __setattr__( self, name, value ):
        if name in self.__dict__:
            raise AttributeError( "Cannot set {name}".format(name=name) )

        raise AttributeError( "'{__class__.__name__}' has no attribute'{name}'". \
            format( __class__= self.__class__, name= name ))

    def __getattribute__( self, name ):
        if name.startswith('_'): 
            raise AttributeError
        return object.__getattribute__( self, name )


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

'''
creating properties - eager vs. lazy
'''
# eager calculation: when we set a value via property, other attributes are also computed 
# lazy calculation: calculations are deferred until requested via a property 

class Hand_Lazy(Hand):
    def __init__(self, dealer_card, *cards):
        self.dealer_card = dealer_card
        self._cards = list(cards)
    
    @property
    def total(self):
        delta_soft = max(c.soft-c.hard for c in self._cards)
        hard_total = sum(c.hard for c in self._cards)
        if hard_total+ delta_soft <=21: 
            return hard_total+delta_soft
        return hard_total 
   
    @property
    def card(self):
        return self._cards 
   
    @card.setter
    # doesn't trigger re-compute of the total
    def card(self, aCard):
        self._cards.append(aCard)
    
    @card.deleter
    def card(self):
        self._cards.pop(-1)

# setter and deleter properties enable use to add a card to the hand with statement like 
    h.card = d.pop()


# total is an attribute that's computed eagerly as each card is added 
class Hand_Eager(Hand):
    def __init__(self, dealer_card, *cards):
        self.dealer_card = dealer_card
        self.total = 0
        self._delta_soft = 0
        self._hard_total = 0
        self._cards = list()
        for c in cards:
            self.card = c
    
    @property
    def card(self):
        return self._cards

    # Each time a card is added, the total attribute is updated.
    @card.setter
    def card(self, aCard):
        self._cards.append(aCard)
        self._delta_soft = max(aCard.soft - aCard.hard. self._delta_soft)
        self._hard_total += aCard.hard
        self._set_total()
    
    def _set_total(self):
        if self._hard_total+self._delta_soft <= 21:
            self.total= self._hard_total+self._delta_soft
        else:
            self.total= self._hard_total


# another example of eager evaluation when extending a collections class
# calculate sum each time you modify an item 

class StatsList(list):
    def __init__(self, *args, **kwargs):
        self.sum0 = 0 # len
        self.sum1 = 1 # sum
        self.sum2 = 0 # squared
        super().__init__(*args, **kwargs)
        for x in self:
            self._new(x)
    
    def _new(self, value):
        sum0 += 1
        sum1 += value
        sum2 += value*value
    
    def _rmv(self, value):
        self.sum0 -=1 
        self.sum1 -= value 
        self.sum2 -= value*value 
    
    def insert(self, index, value):
        super().insert(index, value)
        self._new(value)
    
    def pop(self, index=0):
        value = super().pop(index)
        self._rmv(value)
        return value 
    


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

# example descriptor which logs something when it's accessed

class Verbose_attribute():
    def __get__(self, obj, type=None) -> object:
        print("accessing the attribute to get the value")
        return 42
    
    def __set__(self, obj, value) -> None:
        print("accessing the attribute to get the value")
        raise AttributeError("can't change the value")

class Foo():
    attribute1 = Verbose_attribute()


'''
Timeit module for testing performance
'''
timeit.timeit("f()", """def f(): pass""")

timeit.timeit(setup="from __main__ import resolve", stmt="resolve('python.org", number=1)

