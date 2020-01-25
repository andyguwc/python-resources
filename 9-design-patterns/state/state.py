##################################################
#  State Pattern
##################################################


'''
structure
'''
# state pattern is similar to strategy pattern, but purpose is different 
# the goal is to represent state transfer systems. An object can be in a specific state 
# and certain actions may drive it to a different state 

# To make this work, we need a manager, or context class that provides an interface
# for switching states. Internally, this class contains a pointer to the current state; each
# state knows what other states it is allowed to be in and will transition to those states
# depending on actions invoked upon it.

# So we have two types of classes, the context class and multiple state classes. The
# context class maintains the current state, and forwards actions to the state classes.
# The state classes are typically hidden from any other objects that are calling the
# context; it acts like a black box that happens to perform state management internally.

# Brute force implementation - In the class has a state attribute, which is set to beginning state, at every action/transition, 
# check if the action is legal given the state and set the updated state. But this is in flexible if we need to add one more state


'''
example - a XML Parser
'''
# the context class 

class Parser: 
    def __init__(self, parse_string):
        self.parse_string = parse_string 
        self.root = None
        self.current_node = None 

        self.state = FirstTag()
    
    def process(self, remaining_string):
        # important method which accepts remaining string and passes to current state 
        remaining = self.state.process(remaining_string, self)
        if remaining:
            self.process(remaining)
    
    def start(self):
        self.process(self.parse_string)

class ChildNode:
    def process(self, remaining_string, parser):
        stripped = remaining_string.strip()
        if stripped.startswith("</"):
            parse.state = CloseTag()
        elif stripped.startswith("<"):
            parser.state = OpenTag()
        else:
            parser.state = TextNode()
        return stripped

# State vs. Strategy
# While the two patterns have identical structures, they solve completely different
# problems. The strategy pattern is used to choose an algorithm at runtime; generally,
# only one of those algorithms is going to be chosen for a particular use case. The state
# pattern, on the other hand is designed to allow switching between different states
# dynamically, as some process evolves. In code, the primary difference is that the
# strategy pattern is not typically aware of other strategy objects. In the state pattern,
# either the state or the context needs to know which other states that it can switch to.


'''
example - shopping cart
'''

# create a context
# create state classes which handle transitions 

class AbsState(metaclass=ABCMeta):
    # each concrete state must implement the items 
    def __init__(self, context):
        self._cart = context 
    
    @abstractmethod 
    def add_item(self):
        pass 
    
    @abstractmethod 
    def remove_item(self):
        pass 
   
    @abstractmethod 
    def checkout(self):
        pass 
    
    @abstractmethod 
    def pay(self):
        pass 

    @abstractmethod 
    def empty_cart(self):
        pass 

# empty state
class Empty(AbsState):
    def add_item(self):
        self._cart.items +=1 
        print("you added the first item")
        # sets the state for the context 
        self._cart.state = self._cart.not_empty 
    
    def remove_item(self):
        print("empty, can't remove")

    def checkout(self):
        print("empty, can't checkout")

    def pay(self):
        print("empty, can't pay")

    def empty_cart(self):
        print("empty")

class NotEmpty(AbsState):
    def add_item(self):
        self._cart.items +=1 
        print("you have %s items in your car" % self._cart.items)
    
    def remove_item(self):
        self._cart.items -=1 
        if self._cart.items:
            print("you have %s items in your cart" % self._cart.items)
    
    def checkout(self):
        print("done shopping, check out")
        self._cart.state = self._cart.check_out
    
    def pay(self):
        print("go to checkout to pay")

    def empty_cart(self):
        print("go to checkout to pay")

class CheckOut(AbsState):
    pass 


class PaidFor(AbsState):
    pass 


# context manager 
class ShoppingCart:
    def __init__(self):
        self.empty = Empty(self)
        self.not_empty = NotEmpty(self)
        self.check_out = AtCheckOut(self)
        self.paid_for = PaidFor(self)

        self.items = 0 
        self.state = self.empty 
    
    def add_item(self):
        self.state.add_item()

    def remove_item(self):
        self.state.remove_item()
    
    def checkout(self):
        self.state.checkout()


# main program
cart = ShoppingCart()
cart.add_item()
cart.remove_item()
cart.checkout()
# ...


