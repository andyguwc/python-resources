##################################################
# Comparison Operator
##################################################

'''
Comparison operations
'''
# • x<y calls x.__lt__(y)
# • x<=y calls x.__le__(y)
# • x==y calls x.__eq__(y)
# • x!=y calls x.__ne__(y)
# • x>y calls x.__gt__(y)
# • x>=y calls x.__ge__(y)

class BlackJackCard:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit 
    def __lt__(self, other):
        print( "Compare {0} < {1}".format( self, other ) )
        return self.rank < other.rank
    def __str__(self):
        return "{rank}{suit}".format(**self.__dict__)


# example implementing comparison operators 
class BlackJackCard:
    def __init__(self, rank, suit, hard, soft):
        self.rank = rank
        self.suit = suit
        self.hard = hard 
        self.soft = soft 
    def __lt__(self, other):
        if not isinstance(other, BlackJackCard): 
            return NotImplemented
        return self.rank < other.rank 
    def __le__(self, other):
        try:
            return self.rank <= other.rank 
        except AttributeError:
            return NotImplemented
    def __gt__(self, other):
        if not isinstance(other, BlackJackCard):
            return NotImplemented
        return self.rank > other.rank 
    def __ge__(self, other):
        if not isinstance(other, BlackJackCard):
            return NotImplemented
        return self.rank >= other.rank 
    def __eq__( self, other ):
        if not isinstance( other, BlackJackCard ): 
            return NotImplemented
        return self.rank == other.rank and self.suit == other.suit
    def __ne__( self, other ):
        if not isinstance( other, BlackJackCard ): 
            return NotImplemented
        return self.rank != other.rank and self.suit != other.suit
    def __str__( self ):
        return "{rank}{suit}".format( **self.__dict__ )


'''
total ordering
'''

# The functools.total_ordering decorator can be used to simplify this process. To use
# it, you decorate a class with it, and define __eq__() and one other comparison method
# (__lt__, __le__, __gt__, or __ge__). The decorator then fills in the other comparison
# methods for you

from functools import total_ordering
class Room:
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width
        self.square_feet = self.length * self.width 

@total_ordering 
class House:
    def __init__(self, name, style):
        self.name = name
        self.style = style
        self.rooms = list()

    @property
    def living_space_footage(self):
        return sum(r.square_feet for r in self.rooms) 

    def add_room(self, room):
        self.rooms.append(room)

    def __str__(self):
        return '{}:{} square foot {}'.format(self.name,
                                             self.living_space_footage,
                                             self.style)
    def __eq__(self, other):
        return self.living_space_footage == other.living_space_footage

    def __lt__(self, other):
        return self.living_space_footage < other.living_space_footage

# another example @functools.total_ordering 
import functools
@functools.total_ordering 
class Card:
    __slots__ = ("rank", "suit")
    def __new__(cls, rank, suit):
        self = super().__new__(cls)
        self.rank = rank 
        self.suit = suit 
    
    def __eq__(self, other):
        return self.rank == other.rank 
    
    def __lt__(self, other):
        return self.rank < other.rank 


# explicit and implicit type checking 
# Two kinds of type checking: explicit and implicit. The explicit type
# checking uses isinstance(). The implicit type checking uses a try: block. There's
# a tiny conceptual advantage to using the try: block: it avoids repeating the name of
# a class. It's entirely possible that someone might want to invent a variation on a card
# that's compatible with this definition of BlackJackCard but not defined as a proper
# subclass. Using isinstance() might prevent an otherwise valid class from working
# correctly.

'''
mixed class comparison 
'''
# using isinstance
# example of comparing both against integer and against another object instance
def __eq__(self, other):
    if isinstance(other, int):
        return self.total() == other 
    try:
        return(self.cards == other.cards
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




##################################################
# Operator Overloading 
##################################################

# negation
__neg__

# plus
__pos__

# inverse
__invert__

def __abs__(self):
    return math.sqrt(sum(x*x for x in self))

def __neg__(self):
    return Vector(-x for x in self)

def __pos__(self):
    return Vector(self)

# overwrriding scalar multiplication
def __mul__(self, scalar):
    return Vector(n * scalar for n in self)

# implementing equal 
def __eq__(self, other):
    if isinstance(other, Vector):
        return (len(self)==len(other)) and 
                all(a==b for a, b in zip(self, other))
    else:
        return NotImplemented 

