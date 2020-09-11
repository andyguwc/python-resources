##################################################
#  Abstract Base Classes 
##################################################

# While duck typing is useful, it is not always easy to tell in advance if a class is going
# to fulfill the protocol you require. Therefore, Python introduced the idea of abstract
# base classes. Abstract base classes, or ABCs, define a set of methods and properties
# that a class must implement in order to be considered a duck-type instance of that
# class. The class can extend the abstract base class itself in order to be used as an
# instance of that class, but it must supply all the appropriate methods.


'''
using ABCs from Collections 
'''
# example using an ABC
# Container class from Collections
from collections import Container

# check which bstract methods need to be implemented
Container.__abstractmethods__
# frozenset(['__contains__'])

# check what the function signature should look like
help(Container.__contains__)

# define a dummy container
class OddContainer:
    def __contains__(self, x):
        if not isinstance(x, int) or not x % 2:
            return False
        return True

odd_container = OddContainer()

# even though we did not extend Container from OddContainer, the class is a Container object 
isinstance(odd_container, Container)
# True
# so with duck typing, we can create is a relationships without the overhead of using inheritance 


# Custom class to mimics the behavior of a common built-in container type 
# for example, if you want a custom iterator then start with Iterable ABC
# But you need to implment all the required special methods 
import collections

class A(collections.Iterable):
    pass 


# create a sequence where items are stored in sorted order 
import collections 
import bisect 

class SortedItem(collections.Sequence):
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial is None else []

    # required sequence methods 
    def __getitem__(self, index):
        return self._items[index]
    
    def __len__(self):
        return len(self._items)
    
    # methods for adding an item in the right location 
    def add(self, item):
        bisect.insort(self._items, item)

# Here’s an example of using this class:
# >>> items = SortedItems([5, 1, 3])
# >>> list(items)


# many abstract base classes in collections provide default implementations of common container methods 
class Items(collections.MutableSequence):
    def __init__(self, initial=None):
        self._items = list(initial) if initial is None else []
    
    # required sequence methods 
    def __getitem__(self, index):
        print('Getting:', index)
        return self._items[index]

    def __setitem__(self, index, value):
        print('Setting:', index, value)
        self._items[index] = value 
    
    def __delitem__(self, index):
        print('Deleting:', index)
        del self._items[index]
    
    def insert(self, index, value):
        print('Inserting:', index, value)
        self._items.insert(index, value)
    
    def __len__(self):
        print('Len')
        return len(self._items)
    
# If you create an instance of Items, you’ll find that it supports almost all of the core list
# methods (e.g., append(), remove(), count(), etc.). These methods are implemented in
# such a way that they only use the required ones.


'''
Defining an ABC
'''

# abstract methods load() and pick()
# concrete methods loaded() and inspect()

import abc

class Tombola(abc.ABC):

    @abc.abstractmethod 
    def load(self, iterable):
        """Add items from an iterable""" 

    @abc.abstractmethod 
    def pick(self):
        """Remove item at random, returning it 
        This method should raise `LookupError` when the instance is empty.
        """

    def loaded(self):
        """Return `True` if there's at least 1 item, `False` otherwise."""
        return bool(self.inspect())
    
    def inspect(self):
        """Return a sorted tuple with the items currently inside"""
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break 
        self.load(items)
        return tuple(sorted(items))


# another example defining an ABC 

import abc
# by passing in metaclass you are giving this class superclass capabilities
class MediaLoader(metaclass=abc.ABCMeta):
    # by making this method abstract, stating any subclass must implement that method 
    @abc.abstractmethod
    def play(self):
        pass
    
    # any subclass must supply that property 
    @abc.abstractproperty
    def ext(self):
        pass 
    
    # also implements an abstract property
    @property
    def anotherproerty(self):
        pass 
    
    # It is basically saying that any class that supplies concrete implementations of all the 
    # abstract attributes of this ABC should be considered a subclass of MediaLoader. Doesn't need to inherit from the MediaLoader class
    @classmethod 
    def __subclasshook__(cls, C):
        # is class C a subclass of this cls
        if cls is MediaLoader:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True
        return NotImplemented


# abstract superclass - raise an exception for methods that must be implemented by a subclass 
class BettingStrategy:
    # the subclass must overwrite the subclass
    def bet(self):
        raise NotImplementedError("No bet method")
    
    def record_win(self):
        pass 

    def record_loss(self):
        pass 

class Flat(BettingStrategy):
    def bet(self):
        return 1 



'''
Use ABC to Enforce 
'''

from abc import ABCMeta, abstractmethod

class Base(metaclass=ABCMeta):
    @abstractmethod 
    def foo(self):
        pass 
    
    @abstractmethod
    def bar(self):
        pass 

class Concrete(Base):
    def foo(self):
        pass 

assert issubclass(Concrete, Base) 
# Since Concrete didn't implement a required method,
# will raise an error at initiation 

# >>> C = Concrete()
# TypeError:
# "Can't instantiate abstract class Concrete
# with abstract methods bar"