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
setattr for easier initialization
'''

class TwitterModel(object):
    """Base class from which all twitter models will inherit
    """

    def __init__(self, **kwargs):
        self.param_defaults = {}
    
    def __str__(self):
        return self.as_json_str()
    
    def __eq__(self, other):
        return other and self._asdict() == other._asdict()
    
    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        if hasattr(self, 'id'):
            return hash(self.id) 
        else:
            raise TypeError('unhashable type: {} (no id attribute)'
                            .format(type(self)))

    def as_json_str(self, ensure_ascii=True):
        return json.dumps(self.asdict(), ensure_ascii=ensure_ascii, sort_keys=True)

    def asdict(self):
        data = {}
        for (key, value) in self.param_defaults.items():
            # If the value is a list, we need to create a list to hold the
            # dicts created by an object supporting the AsDict() method,
            # i.e., if it inherits from TwitterModel. If the item in the list
            # doesn't support the AsDict() method, then we assign the value
            # directly. An example being a list of Media objects contained
            # within a Status object.
            if isinstance(getattr(self, key, None), (list, tuple, set)):
                data[key] = list()
                for subobj in getattr(self, key, None):
                    if getattr(subobj, 'asdict', None):
                        data[key].append(subobj.asdict())
                    else:
                        data[key].append(subobj)
            
            # not a ;ist, but still a subclass and we can assign directly asdict
            elif getattr(getattr(self, key, None), 'asdict', None):
                data[key] = getattr(self, key).asdict()
            
            elif getattr(self, key, None):
                data[key] = getattr(self, key, None)
        return data  


class Media(TwitterModel):
    """A class representing Media component of a tweet"""

    def __init__(self, **kwargs):
        self.param_defaults = {
            'display_url': None,
            'expanded_url': None,
            'ext_alt_text': None,
            'id': None,
            'media_url': None,
            'media_url_https': None,
            'sizes': None,
            'type': None,
            'url': None,
            'video_info': None,
        }

        for (param, default) in self.param_defaults.items():
            setattr(self, param, kwargs.get(param, default))
    
    def __repr__(self):
        return "Media(ID={media_id}, Type={media_type}, DisplayURL='{url}'".format(
            media_id=self.id,
            media_type=self.type, 
            url=self.display_url)

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

# Modifying class Attributes
# Each instance can have attributes, sometimes called instance variables
# Classes have associated methods, which are just a special kind of function

# in shipping.py
# can also replace ShippingContainer.new_serial as self.new_serial but it's more confusing
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


class CountedObject:
    num_instances = 0

    def __init__(self):
    self.__class__.num_instances += 1

# >>> CountedObject.num_instances
# 0
# >>> CountedObject().num_instances
# 1
# >>> CountedObject().num_instances
# 2

# assignment to attributes always creates an isntance attribute, never a class attribute
# in fact, it crates an instance attribute
self.attr = something

# WARNING: This implementation contains a bug
class BuggyCountedObject:
    num_instances = 0
    def __init__(self):
        self.num_instances += 1 # !!!
# this bad implementation never increments the shared counter variable
# this accidentally “shadowed” the num_instance class variable by creating an instance variable of the same name in the constructor.


##################################################
#  Advanced Init
##################################################

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
class Card:
    def __init__(self, rank, suit):
        self.suite = suit
        self.rank = rank
        self.hard, self.soft = self._points()


class NumberCard(Card):
    def _points(self):
        return int(self.rank), int(self.rank)


class AceCard(Card):
    def _points(self):
        return 1, 11 


def card(rank, suit):
    if rank == 1: 
        return AceCard('A', suit)
    elif 2 <= rank < 11: 
        return NumberCard(str(rank), suit)
    elif 11 <= rank < 14:
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


# alternative implementations, replacing the elif statements with mapping
def card(rank, suit):
    cls = {1: AceCard, 11: FaceCard, 12: FaceCard, 13: FaceCard}.get(rank, NumberCard)
    return cls(rank, suit)

# alternative implementations, using __init__ in each subclass to rely on super().__init__
class Card:
    def __init__(self, rank, suit, hard, soft):
        self.rank = rank
        self.suit = suit
        self.hard = hard
        self.soft = soft


class NumberCard(Card):
    def __init__(self, rank, suit):
        super().__init__(str(rank), suit, rank, rank)


class AceCard(Card):
    def __init__(self, rank, suit):
        super().__init__("A", suit, 1, 11)



'''
using keyword argument values during initialization
'''
class Player:
    def __init__(self, table, bet_strategy, **extras):
        self.table = table
        self.bet_strategy = bet_strategy
        self.__dict__.update(extras)        

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
__new__
'''
# inherited __new__() allocates the object which is passed to __init__() as self
# the __new__() method is how to build unitialized object, allows processing before the __init__() method is called
class ChessCoordinates:
    def __new__(cls, *args, **kwargs):
        print("args=" , repr(args))
        print("kwargs= ", repr(kwargs))
        obj = super().__new__(cls)
        print(id(obj))
        return obj

    def __init__(self, file, rank):
        print(id(self)) # this id should be same as the one printed in __new__
        self.file = file
        self.rank = rank


# __new__() method is automatically a static method, without using @staticmethod. And doesn't use a self variable



##################################################
#  Class Method vs. Static Method
##################################################

'''
instance vs. class vs. static methods 
'''

# https://realpython.com/instance-class-and-static-methods-demystified/

# instance method can't be called by class 
# can access class itself through self.__class__ attribute

# static method 
#  - no access needed to either class or instance objects. No knowledge of the class
#  - an implementation detail 

# class method 
#  - require access to the class object to call other class methods or constructor 


'''
Class Method
'''

# Instead of accepting a self parameter, class methods take a cls parameter that points to the class—and not the object instance—when the method is called.
# classmethod changes the way the method is called, so it receives the class itself as the first argument, instead of an instance. Its most common use is for alternative constructors

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

# static methods with inheritance
# static methods can be overwritten in subclasses 


'''
Class Method as Constructor
'''
# use class methods for factory function (named constructors)
# so that we don't need to tweak the init function 

class ShippingContainer:
    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
   
    @classmethod
    def create_empty(cls, owner_code):
        return cls(owner_code, contents=None)

    @classmethod
    def create_with_items(cls, owner_code, items):
        return cls(owner_code, content=list(items))


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


'''
Collection Class
'''
# wrapper design that contains an internal collection

# implementation uses delegate to the internal underlying class
class Deck:
    def __init__(self):
        self._cards = [card(r+1, s) for r in range(13) for s in (Club, Diamond, Heart, Spade)]
        random.shuffle(self._cards)

    def pop(self):
        return self._cards.pop()

d = Deck()
hand = [d.pop(), d.pop()]


# alternative implementation by extending a collection class 
# other methods inherit from 
class Deck(list):
    def __init__(self):
        super().__init__(card(r+1, s) for r in range(13) for s in (Club, Diamond, Heart, Spade))
        random.shuffle(self)


'''
circular reference and weakref
'''
# here parent and child classes have circular reference
# they both contain references to each other

class Parent:
    def __init__(self, *children):
        self.children = list(children)
        for child in self.children:
            child.parent = self

    def __del__(self):
        print(f"Removing {(self.__class__, id(self))}")
    

class Child:
    def __init__(self):
        print(f"Removing {self.__class__, }")


import weakref
class Parent:
    def __init__(self, *children):
        self.children = list(children)
        for child in self.children:
            child.parent = weakref.ref(self)
    
    def __del__(self):
        print(f"Removing {(self.__class__, id(self))}")