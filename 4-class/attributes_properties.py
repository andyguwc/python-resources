##################################################
# Attribute Access & Properties
##################################################

'''
__dict__
'''
v = Vector(5,3)
v.__dict__
# name of attributes as keys, values as values
del v.__dict__['x']
v.x # deleted, hence throw attribute error

vars(v) # access __dict__

'''
methods in __class__.__dict__
'''
# methods are __class__ attributes

v = Vector(x=3, y=3)
v.__class__
v.__class__.__dict__
v.__class__.__dict__['__repr__'](v) # self argument


'''
__getattr__(), __setattr__(), and __delattr__()
'''

# The __setattr__() method will create and set attributes.

# The __getattr__() invoked after requested attribute/property not found by normal lookup

# The __getattribute__() invoked instead of normal lookup. Lower level attribute processing. If the attribute is not found, it calls __getattr__() as a fallback

# The __delattr__() method deletes an attribute.

getattr(v, 'y')
hasattr(v, 'x')
delattr(v, 'z')
setattr(v, 'x', 9)
v.x 


class Vector:
    def __init__(self, **coords):
        private_coords = {'_' + k:v for k,v in coord.items()}
        self.__dict__.update(private_coords)
    
    def __repr__(self):
        return "{}({})".format(
            self.__class__.__name__,
            ', '.join("{k}={v}".format(
                k=k[1:],
                v=self.__dict__[k])
                for k in sorted(self.__dict__.keys())))


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


class LoggingProxy:
    def __init__(self, target):
        super().__setattr__('target', target)
    
    def __getattribute__(self, name):
        target = super().__getattribute__('target')

        try:
            value = getattr(target, name)
        except AttributeError as e:
            raise AttributeError("{} cold not forward request {} to {}".format(
                super().__getattribute__('__class__').__name__,
                name,
                target)) from e
        print("Retrieved attribute {!r} = {!r} from {!r}".format(name, value, target))
        return value

    def __setattribute__(self, name):
        target = super().__getattribute__('target')

        try:
            setattr(target, name, value)
        except AttributeError as e:
            raise AttributeError("{} cold not forward request {} to {}".format(
                super().__getattribute__('__class__').__name__,
                name,
                target)) from e
        print("Set attribute {!r} = {!r} from {!r}".format(name, value, target))


# use __getattribute__ to prevent access to internal __dict__ attribute

class BlackJack:
    def __init__(self, rank, suit):
        super().__setattr__('rank', rank)
        super().__setattr__('suit', suit)
    
    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise AttributeError(f"cannot set {name}")
        raise AttributeError("Have no attribute")

    def __getattribute__(self, name):
        if name.startswith('_'):
            raise AttributeError
        return objet.__getattribute__(self, name)



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
    # additional validations of input
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

