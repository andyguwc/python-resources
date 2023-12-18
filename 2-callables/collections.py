

##################################################
# Collections Protocols
##################################################


'''
fundamental base classes
'''
# that requires a single special method 

# The Container base class requires the concrete class to implement the __
# contains__() method. This special method implements the in operator.

# The Iterable base class requires __iter__(). This special method is used
# by the for statement and the generator expressions as well as the iter()
# function.

# The Sized base class requires __len__(). This method is used by the len()
# function. It's also prudent to implement __bool__(), but it's not required by
# this abstract base class.

# The Hashable base class requires __hash__(). This is used by the hash()
# function. If this is implemented, it means that the object is immutable.

'''
higher level composite structures
'''

# The Sequence and MutableSequence classes build on the basics and fold in
# methods such as index(), count(), reverse(), extend(), and remove().
# The Mapping and MutableMapping classes fold in methods such as keys(),
# items(), values(), and get(), among others.
# The Set and MutableSet classes fold in comparison and arithmetic operators
# to perform set operation


''' 
Container
'''

# iteration is often implicit. 
# If a collection has no contain method, the iteration does a sequential scan

# memebership testing using in and not in 
__contains__(item)

class SortedSet:
    def __init__(self, items=None):
        self._items = sorted(items) if items is not None else []

    def __contains__(self, item):
        return item in self._items 

# if it's sorted already then faster implementation
def __contains__(self, item):
    index = bisect_left(self._items, item)
    return (index != len(self._items) and (self._items[index] == item))


# another example modify the meaning of contains
def __contains__(self, rank):
    returna any(c.rank==rank for c in hand.cards)

# so instead of doing
any(c.rank == 'A' for c in hand.cards)
# we can do 
'A' in hand.cards


'''
Size
'''
# determine number of elements with len(s)
def __len__(self):
    return len(self._items) # calling len on the underlying list 


'''
Iterable
'''
# iterable protocol which returns an iterator with __iter__()
# can produce iterator with iter(s)
# iterable can be used in the for loop
for item in iterable:
    do_something(item)

def __iter__(self):
    return iter(self._items)
    # or use below

def __iter__(self):
    for item in self._items:
        yield item

# if __iter__ is not implemented, but __getitem__ is implemented, Python creates
# an interator that attempts to fetch items in order, starting from index 0
# if failing, raises TypeError 
# because all python sequences implement __getitem__, any python sequence is iterable 

class Foo:
    def __iter__(self):
        pass 
    
from collections import abc 
issubclass(Foo, abc.Iterable) # True
f = Foo()
isinstance(f, abc.Iterable) # True 


'''
Sequence
'''

# retrieve elements by index 
item = seq[index] # no special methods

# retrieve slices by slicing 
item = seq[start:stop]

# further more 
# return first matching index of item or raise error 
index = seq.index(item)
# count items
num = seq.count(item)

# concatenation with + operator and repetition with * operator 

# implies container, sized, and iterable 
# index can be a slice 
def __getitem__(self, index):
    result = self._items[index]
    return SortedSet(result) if isinstance(index, slice) else result 


class Explore(list):
    def __getitem__(self, index):
        print(index, index.indices(len(self)))
        return super().__getitem__(index)



# example object - collection of cards 
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.rank]
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        # because __getitem__ delegates to the [] operator of self._cards
        # our deck automatically supports slicing
        return self._cards[position]

deck = FrenchDeck()
len(deck)
deck[1] # calls __getitem__ method

from random import choice
choice(deck) # picks a random card


# iteration is often implicit, the in operator does a sequential scan if no __contains__ method implemented
Card('Q', 'hearts') in deck

# implement customized sorting 
# first define a value function for each card 
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

# now list in order of increasing rank 
for card in sorted(deck, key=spades_high):
    print(card)

# reversed sequence
r = reversed(seq) # special method __reversed__() fallback to __getitem__() and __len__()

# overwriting index
def index(self, item):
    index = bisect_left(self._items, item)
    if (index != len(self._items)) and (self._items[index] == item):
        return index 
    raise ValueError("{} not found".format(repr(item)))

# concatenationg + 
from itertools import chain 

def __add__(self, rhs):
    return SortedSet(chain(self._items, rhs._items))

# repetition with * operator
def __mul__(self, rhs):
    return self if rhs >0 else SortedSet()


'''
__bool__() method
'''

# By default, instances of user-defined classes are considered truthy, unless either
# __bool__ or __len__ is implemented. Basically, bool(x) calls x.__bool__() and uses
# the result. 
# If __bool__ is not implemented, Python tries to invoke x.__len__(), and if
# that returns zero, bool returns False. Otherwise bool returns True.
# Our implementation of __bool__ is conceptually simple: it returns False if the magnitude
# of the vector is zero, True otherwise. We convert the magnitude to a Boolean
# using bool(abs(self)) because __bool__ is expected to return a boolean.

# under the hood, this uses __bool__() method
# An empty collection should be equivalent to False. A nonempty collection can return True.
if some_object:
    process(some_object)


# If we're wrapping a list, we might have something as shown in the following code snippet:
def __bool__( self ):
  return bool( self._cards )
# This delegates the Boolean function to the internal _cards collection.
# If we're extending a list, we might have something as follows:
def __bool__( self ):
    return super().__bool__( self )
# This delegates to the superclass definition of the __bool__() function.

'''
Example Implementation
'''

class Vector:
    def __init__(selflt, x= 0, y=0):
        self.x=x
        self.y=y
    
    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)
    
    def __abs__(self):
        return hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x+other.x
        y = self.y+other.y 
        return Vector(x, y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


'''
Extending a colleciton
'''
# upgrade a Counter to add mean and standard deviation 
# lazy evaluation as properties
from collections import Counter 
class StatsCounter(Counter):
    @property
    def mean(self):
        sum0 = sum(v for k,v in self.items())
        sum1 = sum(v*v for k, v in self.items())
        return sum1/sum0
    
    @property
    def stdev(self):
        sum0= sum( v for k,v in self.items() )
        sum1= sum( k*v for k,v in self.items() )
        sum2= sum( k*k*v for k,v in self.items() )
        return math.sqrt( sum0*sum2-sum1*sum1 )/sum0

# eager evaluations
# class that calculates statistical measures
class StatsList(list):
    def __init__(self):
        self.sum0 = 0
        self.sum1 = 0.0
        self.sum2 = 0.0
        super().__init__()
        for x in self:
            self._new(x)
        
    def _new(self, value):
        self.sum0 += 1
        self.sum1 += value
        self.sum2 += value * value
    
    def _rmv(self, value):
        self.sum0 -= 1
        self.sum1 -= value
        self.sum2 -= value * value

    def insert(self, index, value):
        super().insert(index, value)
        self._new(value)

    def pop(self, index):
        value = super().pop(index)
        self._rmv(value)
        return value


'''
Wrapping a colleciton
'''
class StatsList:
    def __init__(self):
        self._list = list()
        self.sum0 = 0
        self.sum1 = 0
        self.sum2 = 0
    
    def append(self, value):
        self._list.append(value)
        self.sum0 += 1
        self.sum1 += value
        self.sum2 += value * value
    
    def __getitem__(self, index):
        return self._list.__getitem__(index)
    
    @property
    def mean(self):
        return self.sum1 / self.sum0

    def stdev(self):
        return math.sqrt(
            self.sum0*self.sum2 - self.sum1*self.sum1
        ) / self.sum0

    # make this an iterable
    # create generator functions
    def __iter__(self):
        return iter(self._list)


##################################################
# Design Considerations
##################################################

# When working with containers and collections, we have a multistep design strategy:

# 1. Consider the built-in versions of sequence, mapping, and set.
# 2. Consider the library extensions in the collection module, as well as extras
# such as heapq, bisect, and array.
# 3. Consider a composition of existing class definitions. In many cases, a list of
# tuple objects or a dict of lists provides the needed features.
# 4. Consider extending one of the earlier mentioned classes to provide
# additional methods or attributes.
# 5. Consider wrapping an existing structure as another way to provide
# additional methods or attributes.
# 6. Finally, consider a novel data structure. Generally, there is a lot of careful
# analysis available. Start with Wikipedia articles such as this
# one: http://en.wikipedia.org/wiki/List_of_data_structures.

# Once the design alternatives have been identified, there are two parts of the
# evaluation left:
# How well the interface fits with the problem domain. This is a relatively
# subjective determination.
# How well the data structure
