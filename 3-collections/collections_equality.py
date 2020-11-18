'''
equality and inequality
'''

# implement equality and inequality
# without implementing this, two objects with the same component can be different 
def __eq__(self, rhs):
    if not isinstance(rhs, SortedSet):
        return NotImplemented # return NotImplemented object instead of raising the error
    return self._items == rhs._items

# can overwrite the inequality method 
def __ne__(self, rhs):
    if not isinstance(rhs, SortedSet):
        return NotImplemented
    return self._items != rhs._items

SortedSet([1,2,3]) == SortedSet([1,2,3]) # return False 
SortedSet([1,2,3]) is SortedSet([1,2,3]) # return False 


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank
    
    def __hash__(self):
        return hash(self.suit) ^ hash(self.rank)


# mixed class comparison example 
# full implementation of a class with comparisons

class Hand:
    def __init__(self, dealer_card, *cards):
        self.dealer_card = dealer_card
        self.cards = list(cards)
    
    def __str__(self):
        return ", ".join(map(str, self.cards))

    def __repr__(self):
        return "{__class__.__name__}({dealer_card!r}, {_cards_str})".format(
            __class__=self.__class__,
            _cards_str_=", ".join(map(repr, self.cards)),
            **self.__dict__)
    
    def __eq__(self, other):
    # mixed class comparison check for instance type
        if isinstance(other, int):
            return self.total() == other 
        
        try: 
            return (self.cards == other.cards
                and self.dealer_card == other.dealer_card)
        except AttributeError:
            return NotImplemented 
    
    def __lt__(self, other):
        if isinstance(other, int):
            return self.total() < other 
        try:
            return self.total() < other.total()
        except AttributeError:
            return NotImplemented 
    
    def __le__(self, other):
        if isinstance(other, int):
            return self.total() <= other 
        try:
            return self.total() <= other.total()
        except AttributeError:
            return NotImplemented 
    
    __hash__ = None 
    
    def total(self):
        pass 

    
'''
Set
'''
__contains__
__iter__
__len__

__le__() # <= subset
__ge__() # >= superset

# mutable set 
# implement add() and discard()


'''
__hash__() method
'''
# The built-in hash() function invokes the __hash__() method of a given object.
# This hash is a calculation which reduces a (potentially complex) value to a small
# integer value.

# The hash() function (and the associated __hash__() method) is used to create a
# small integer key that is used to work with collections such as set, frozenset, and
# dict. These collections use the hash value of an immutable object to rapidly locate
# the object in the collection.

# mutable objects should never return a hash value 
# immutable object can return a hash value so the object can be used as the key in a dictionary or a member of a set

# immutable objects overrride both __eq__ and __hash__

def __eq__(self, other):
    return self.suit == other.suit and self.rank == other.rank 

def __hash__(self):
    return hash(self.suit)^hash(self.rank)

# mutable objects define __eq__() but set __hash__ to None
def __eq__(self, other):
    return self.suit == other.suit and self.rank == other.rank 
__hash__ = None 

    