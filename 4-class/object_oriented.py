##################################################
# Constructor / Initialization
##################################################


# what is the data you want to deal with 
# what will one instance of the class represent
# what information should each instance have as instance variables
# what instance methods should each instance have 


'''
Constructor
'''
# contructor 
class Point:
    """ Point class for representing and manipulating x, y coordinates"""
    def __init__(self):
        """Create a point at the origin"""
        self.x = 0
        self.y = 0
    
p = Point() # instantiate an object of type Point - i.e. a combination of making a new object and get settings initialized for the default settings
q = Point() # make a second point

# adding parameters to the Constructor
class Point:
    """ Point class for representing and manipulating x,y coordinates. """
    def __init__(self, initX, initY):
        self.x = initX # assigned to state of the object, in the instance variables x and y
        self.y = initY
p = Point(7,6)

# all methods defined in a class that operate on objects of that class will have self as their first parameter. 
# Again, this serves as a reference to the object itself which in turn gives access to the state data inside the object.
class Point:
    """ Point class for representing and manipulating x,y coordinates. """
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def distanceFromOrigin(self):
        return ((self.x**2)+(self.y**2))**0.5

    # an alternative is to define the function outside the object as distance(point1, point2)
    def distance(self, point2):
        xdiff = point2.getX()-self.getX()
        ydiff = point2.getY()-self.getY()

        dist = math.sqrt(xdiff**2 + ydiff**2)
        return dist

p = Point(7,6)
print(p.getX())
print(p.getY())


'''
Instances
'''

# instances as return values

class Point: 
    # ...
    # return the midpoint 
    def halfway(self, target):
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)

# sorting list of instances

class Fruit:
    def __init__(self, name, price):
        self.name = name
        self.price = price

L = [Fruit("Cherry", 10), Fruit("Apple",5), Fruit("Blueberry", 20)]
for f in sorted(L, key=lambda x: x.price):
    print(f.name)


'''
Instance Vairables vs. Class Variables
'''

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

# Calling class attributes
class Point:
    """ Point class for representing and manipulating x,y coordinates. """
    printed_rep = "*" # this is a class variable the same across all instances 
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def graph(self):

print(Point.printed_rep) # calling class attribute directly


'''
__init__() 
'''

# Each Python class definition has an implicit superclass: object. It's a very
# simple class definition that does almost nothing. 
# We can see below that a class is an object of the class named type and the base class is the class named object

# >>> class X:
# ...     pass
# ... 
# >>> X.__class__
# <class 'type'>
# >>> X.__class__.__base__
# <class 'object'>
# >>> 

# We can always add attributes to an object that's a subclass of the foundational base class, object
class Rectangle:
    def area( self ):
        return self.length * self.width

# r.length, r.width = 13, 8 # sometimes we don't need to set all of the attributes in the __init__() method

# implement __init__() in a superclass

# polymorphic design 
# each subclass provides a unique implementation of the _points() method 
class Card:
    # initializer at the superclass level 
    def __init__(self, rank, suit):
        self.rank = rank  
        self.suit = suit
        self.hard, self.soft = self._points()

class NumberCard(Card): 
    def _points(self):
        return int(self.rank), int(self.rank)

class AceCard(Card):
    def _points(self):
        return 1, 11

class FaceCard(Card):
    def _points(self):
        return 10, 10


#  different intialization function 

class Card:
    def __init__(self, rank, suit, hard, soft):
        self.rank= rank
        self.suit= suit
        self.hard= hard
        self.soft= soft
class NumberCard(Card):
    def __init__(self, rank, suit):
        super().__init__(str(rank), suit, rank, rank)
class AceCard(Card):
    def __init__(self, rank, suit):
        super().__init__("A", suit, 1, 11)
class FaceCard(Card):
    def __init__(self, rank, suit):
        super().__init__({ 11: 'J', 12: 'Q', 13: 'K' }[rank], suit, 10, 10)


# strategy objects (to implement an algorithm or decision) don't have __init__()


'''
Leveraging __init__() via a factory function
'''

# two approaches to factories 
#  - define a function that creates objects of the required classes 
#  - define a class that has methods of creating objects 

# If we have a factory class, we can add subclasses to the factory class when extending the target class hierarchy. This gives us
# polymorphic factory classes; the different factory class definitions have the same method signatures and can be used interchangeably.

# example factory function for Card subclasses 
# This function builds a Card class from a numeric rank number and a suit object


def card(rank, suit):
    if rank == 1: 
        return AceCard('A', suit)
    elif 2 <= rank < 11: 
        return NumberCard(str(rank), suit)
    elif 11 <= rank <14:
        # use mapping to simplify many elif mappings
        name = { 11: 'J', 12: 'Q', 13: 'K' }[rank]
        return FaceCard(name, suit)
    else: 
        # note never use a catchall else, leave the else to raise exceptions
        raise Exception("rank out of range")

# example applying the factory function to build a deck 
deck = [card(rank, suit)
    for rank in range(1,14)
        for suit in (Club, Diamond, Heart, Spade)]


'''
using keyword argument values during initialization
'''
class Player:
    def __init__(self, **kw):
        self.__dict__.update(kw)        

# The disadvantage of this is that we have obscure instance variables that aren't formally documented via a subclass definition


'''
initialization with type validation
'''
class ValidPlayer:
    def __init__( self, table, bet_strategy, game_strategy ):
        assert isinstance( table, Table )
        assert isinstance( bet_strategy, BettingStrategy )
        assert isinstance( game_strategy, GameStrategy )
        self.bet_strategy = bet_strategy
        self.game_strategy = game_strategy
        self.table= table


'''
Composite Objects
'''
# A collection of objects
#  - Wrap: This design pattern is an existing collection definition. This might be an example of the Facade design pattern.
#  - Extend: This design pattern is an existing collection class. This is ordinary subclass definition.
#  - Invent: This is designed from scratch. We'll look at this in Chapter 6, Creating Containers and Collections.

# Wrapping a collection class (Facade design pattern)
# contains an internal collection (list object), the pop() method delegates to the wrapped list object
# Here the pop methods delegates to the wrapped list object
class Deck:
    def __init__(self):
        self._cards = [card(r+1,s) for r in range(12) for s in (Club, Diamond, Hear, Spade)]
        random.shuffle(self._cards)
    
    def pop(self):
        return self._cards.pop()


# Extending a collection class 
# in this case we don't have to reimplement the pop() method, we can inherit it 
# disadvantage too many functions we don't need
class Deck(list):
    def __init__(self):
        super().__init__(card(r+1, s) for r in range(13) for s in (Club,Diamond, Heart, Spade))
        random.shuffle(self)


# taking in variable number of inputs 
class Hand:
    def __init__(self, dealer_card, *cards):
        self.dealer_card = dealer_card
        self.cards = list(cards)
    
    def hard_total(self):
        return sum(c.hard for c in self.cards)
    
    def soft_total(self):
        return sum(c.soft for c in self.cards)


# wrapping in a list and implement __getitem__ 
# with __getitem__ several things like for loop and slicing works 
class StatsList:
    def __init_-(self):
        self._list = list() # wrap a list 
        self.sum0 = 0 
        self.sum1 = 0
    
    def append(self, value):
        self._list.append(value) # delegate to the internal list 
        self.sum0 +=1 
        self.sum1 += value 

    # implement __getitem__
    def __getitem__(self, index):
        return self._list.__getitem__(index)
    
    @property
    def mean(self):
        return self.sum1/self.sum0 

# the for loop works 
statslist = StatsList()
for x in statslist:
    print(x) 


'''
simplifying intialization
'''
class Structure:
    # class variable that specifies expected fields 
    _fields = []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        
        # set the positional arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)
        
        # Set the remaining keyword arguments
        for name in self._fields[len(args):]:
            setattr(self, name, kwargs.pop(name))
        
        # Check for any remaining unknown arguments
        if kwargs:
            raise TypeError('Invalid argument(s): {}'.format(','.join(kwargs)))

# Example class definition 
if __name__ == '__main__':
    class Stock(Structure):
        _fields = ['name', 'shares', 'price']


'''
Define more than one constructor
'''
# create instances in more than one way 
# use a class method 
# receive the class as the first argument (cls)
# class polymorphism 

import time 

class Date:
    # Primary constructor 
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day 
    
    # alternate constructor 
    @classmethod 
    def today(cls):
        t = time.localtime()
        return cls(t.t,_year, t.tm_mon, t.tm_mday)

# to use alternate constructor, call it as a function, such as Date.today()
# a = Date(2012, 12, 21) # Primary
# b = Date.today() # Alternate

# since python only support __init__ as a single constructor per class 
# use @classmethod to define alternative constructors for your classes 
# use class method polymorphism to provide generic way to build and connect concrete subclasses 

class GenericWorker(object):
    # ...
    def map(self):
        raise NotImplementedError 
    
    def reduce(other, self):
        raise NotImplementedError 

    @classmethod
    def create_workers(cls, input_class, config):
        workers = []
        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_data))
        return workers 

'''
get attributes
'''
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



'''
manager objects
'''
# management objects are like office managers, they don't do the actual visible work 
# the attributes on the management objects tend to refer to other objects that do the real work
# the behaviors on such a class delete to those other classes at the right time and pass messages between them

# example manager object ensuring 
# unzipping the file, performing the find and replace, zipping the new file 
import sys
import shutil
import zipfile 

from pathlib import Path 

class ZipReplace:
    def __init__(self, filename, search_string, replace_string):
        # initialization contains the actual objects to manipulate 
        self.filename = filename
        self.search_string = search_string
        self.replace_string = replace_string
        self.temp_directory = Path("unzipped-{}".format(filename))
    
    # then create an overall managemer object for the three steps 
    def zip_find_replace(self):
        self.unzip_files()
        self.find_replace()
        self.zip_files()

    def unzip_files(self):
        self.temp_directory.mkdir()
        with zipfile.ZipFile(self.filename) as zip:
            zip.extractall(str(self.temp_directory))
    
    def find_replace(self):
        for filename in self.temp_directory.iterdir():
            with filename.open() as file:
                contents = file.read()
            contents = contents.replace(self.search_string, self.replace_string)
            with filename.open("w") as file:
                file.write(contents)

    def zip_files(self):
        with zipfile.ZipFile(self.filename, 'w') as file:
            for filename in self.temp_directory.iterdir():
                file.write(str(filename), filename.name)
        shutil.rmtree(str(self.temp_directory))

if __name__ == "__main__":
    ZipReplace(*sys.argv[1:4]).zip_find_replace()



##################################################
#  Class Method vs. Static Method
##################################################

# instance vs. class vs. static methods 
# https://realpython.com/instance-class-and-static-methods-demystified/
# static method 
#  - no access needed to either class or instance objects 
#  - an implementation detail 
# class method 
#  - require access to the class object to call other class methods or constructor 

# class method
# Instead of accepting a self parameter, class methods take a cls parameter that points to the class—and not the object instance—when the method is called.
# classmethod changes the way the method is called, so it receives the class itself as the first argument, instead of an instance. Its most common use is for alternative constructors


'''
Class Method
'''

@classmethod
def frombytes(cls, octets):
    typecode = chr(octets[0])
    memv = memoryview(octets[1:]).cast(typecode)
    return cls(*memv)


# can use classmethod for factory methods
# create multiple functions similar behavior like constructors
# without need to change the __init__

class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'

    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])


# >>> Pizza.margherita()
# Pizza(['mozzarella', 'tomatoes'])

# >>> Pizza.prosciutto()
# Pizza(['mozzarella', 'tomatoes', 'ham'])


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

'''
Static Methods
'''
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


class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return (f'Pizza({self.radius!r}, '
                f'{self.ingredients!r})')

    def area(self):
        return self.circle_area(self.radius)

    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi

# Because the circle_area() method is completely independent from the rest of the class it’s much easier to test.


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





##################################################
# __new__() method
##################################################

'''
new
'''
# One use case for the __new__() method is to initialize objects that are otherwise
# immutable. The __new__() method is where our code can build an uninitialized
# object. This allows processing before the __init__() method is called to set the
# attribute values of the object.

# The __new__() method is used to extend the immutable classes where the
# __init__() method can't easily be overridden.

# The default implementation of __new__() simply does this: return super().__new__( cls )

class Float_Units( float ):
    def __new__( cls, value, unit ):
        obj= super().__new__( cls, value )
        obj.unit= unit
        return obj


##################################################
# metaclass 
##################################################

'''
metaclass
'''
# A metaclass builds a class. Once a class object has been built, the class object is used to build instances

# metaclass is defined by inheriting from type 
# a metaclass receives the content of associated class statements in its __new__ method


# use metaclass to control instance creation 
# make it impossible to create instance in the normal way 
class Spam:
    def __init__(self, name):
        self.name = name 
a = Spam('a')
b = Spam('b')

class NoInstances(type):
    def __call__(self, *args, **kwargs):
        raise TypeError("can't instantiate directly")

class Spam(metaclass=NoInstances):
    @staticmethod
    def grok(x):
        print('Spam.grok')

# another example, implement the singleton pattern 
# a class where only one instance is ever created 
class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None 
        super().__init__(*args, **kwargs)
    
    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instnace = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance 

# Example 
class Spam(metaclass=Singleton):
    def __init__(self):
        print('Creating Spam')

# Example - validate subclasses with metaclass
# receives the contents of associated class statements in its __new__ method. 
# Here you can modify class information before type is actually constructed

class Meta(type):
    def __new__(meta, name, bases, class_dict):
        print((meta, name, bases, class_dict))
        return type.__new__(meta, name, bases, class_dict)

class MyClass(object, metaclass=Meta):
    stuff = 123

    def foo(self):
        pass 

# Metaclasses let you run registration code automatically each time your base class is subclassed in a program.
# Using metaclasses for class registration avoids errors by ensuring that you never
# miss a registration call.

# descriptors and metaclasses make a powerful combination




##################################################
# Argument Signature
##################################################


# The inspect.signature() function allows you to extract signature information from a callable. For example:
from inspect import signature
def spam(x, y, z=42):
    pass
sig = signature(spam)
print(sig)
# (x, y, z=42)
# >>> sig.parameters
# mappingproxy(OrderedDict([('x', <Parameter at 0x10077a050 'x'>),
# ('y', <Parameter at 0x10077a158 'y'>), ('z', <Parameter at 0x10077a1b0 'z'>)]))
# >>> sig.parameters['z'].name
# 'z'
# >>> sig.parameters['z'].default
# 42

# Enforcing Argument signature on *args and **kwargs

from inspect import Signature, Parameter 
# make a signature for a func(x, y=42, *, z=None)
parms = [ Parameter('x', Parameter.POSITIONAL_OR_KEYWORD),
          Parameter('y', Parameter.POSITIONAL_OR_KEYWORD, default=42),
          Parameter('z', Parameter.KEYWORD_ONLY, default=None) ]
sig = Signature(parms)
print(sig)
# (x, y=42, *, z=None)

def func(*args, **kwargs):
    bound_values = sig.bind(*args, **kwargs)
    for name, value in bound_values.arguments.items():
        print(name, value)



##################################################
# __del__() method 
##################################################

# The intent is to give an object a chance to do any cleanup or finalization just before
# the object is removed from memory.

# reference count and destruction 
# objects have a reference count. The count is incresented when the object is assigned to a variable and decremented when the variable is removed 
# when reference count is zero, the object is no longer needed and can be destroyed
class Noisy:
    def __del__(self):
        print("Removing {0}".format(id(self)))


# Circular references and the weakref module
# In the cases where we need circular references but also want __del__() to work
# nicely, we can use weak references. One common use case for circular references are
# mutual references: a parent with a collection of children; each child has a reference
# back to the parent. If a Player class has multiple hands, it might be helpful for a
# Hand object to contain a reference to the owning Player class.

import weakref
class Parent:
    def __init__(self, *children):
        self.children = list(children)
        for child in self.children:
            child.parent = weakref.ref(self)
    def __del__(self):
        print("Removing {__class__.__name__} {id:d}".format(__class__=self.__class__, id = id(self)))


