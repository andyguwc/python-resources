################################################
# Error Checking and Exception Handling
################################################

'''
explicit vs. implicit checking
'''

class Card: 
    def __init__(self, rank, suit):
        self.rank = rank 
        self.suit = suit 
    
    # explicit checking here
    def __lt__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self.rank < other.rank 
    
    # implicit using try: except
    
    def __le__(self, other):
        try: 
            return self.rank <= other.rank
        except AttributeError:
            raise NotImplemented
        
class Table:
    def __init__(self):
        self.deck = Deck()
    
    def get_hand(self):
        try: 
            self.hand = Hand(d.pop(), d.pop())
        except IndexError:
            self.deck = Deck()
            return self.get_hand()

