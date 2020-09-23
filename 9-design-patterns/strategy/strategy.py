##################################################
#  Strategy Pattern
##################################################

'''
Original Implementation (without using first class function)
'''

# The User code connecting to the strategy pattern simply needs to know that it is
# dealing with the Abstraction interface. The actual implementation chosen performs
# the same task, but in different ways; either way, the interface is identical.

# Define a family of algorithms, encapsulate each one, and make them interchangeable.
# Strategy lets the algorithm vary independently from clients that use it.


from abs import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer','name fidelity')

class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product 
        self.quantity = quantity
        self.price = price 

    def total(self):
        return self.price * self.quantity 

class Order: # the Context
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer 
        self.cart = list(cart)
        self.promotion = promotion 
    
    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total 

    def due(self):
        if self.promotion is None:
            discount = 0 
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount 
    
    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


class Promotion(ABC): # the Strategy: an abstract abse class 
    @abstractmethod
    def discount(self, order):
        """Return discount as a positive dollar amount"""

class FidelityPromo(Promotion): # a concrete strategy 
    """ discount for customer with fidelity points"""
    def discount(self, order):
        return order.total()*0.5 if order.customer.fidelity >=1000 else 0 
    
class BulkItemPromo(Promotion): # second concrete strategy 
    """discounts for each lineitem with 20 more units"""
    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >=20:
                discount+=item.total()*0.1
        return discount 

# joe = Customer('John Doe', 0)
# cart = [LineItem('banana', 4, .5),
#         LineItem('apple', 10, 1.5),
#         LineItem('watermellon', 5, 5.0)]
# Order(joe, cart, FidelityPromo())


'''
Refactoring Using Functions 
'''

# Refactoring Using functions as objects 
# replace concrete strategies with simple functions 
from collections import namedtuple 
Customer = namedtuple('Customer', 'name fidelity')

class LineItem:
    def __init__(self, prodcut, quantity, price):
        self.product = prodcut
        self.quantity = quantity
        self.price = price 
    
    def total(self):
        return self.price * self.quantity 
    
class Order: # the Context 
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer 
        self.cart = list(cart)
        self.promotion = promotion 
    
    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total 

    def due(self):
        if self.promotion is None:
            discount = 0 
        else:
            discount = self.promotion(self) # using the function. To compute a discount, just call the self.promotion() function.
        return self.total() - discount 

# To apply a discount strategy to an Order, just pass the promotion function as an
# argument.
Order(joe, cart, fidelity_promo)

# Find the best promos 
promos = [fidelity_promo, bulk_item_promo, large_order_promo]

def best_promo(order):
    """Select best discount available
    """
    return max(promo(order) for promo in promos)

def fidelity_promo(order):
    """5% discount for customers with 1000 or more fidelity points"""
    return order.total() * 0.05 if order.customer.fidelity > = 1000 else 0 

def bulk_item_promo(order):
    """10% discount for each LineItem with 20 or more units"""
    discount = 0 
    for item in order.cart:
        if item.quantity >=20: 
            discount += item.total * 0.1 
    return discount 

# Alternative using module
promos = [globals()[name] for name in globals()
            if name.endswith('_promo')
            and name != 'best_promo']
    
# globals()
# Return a dictionary representing the current global symbol table. This is always the
# dictionary of the current module (inside a function or method, this is the module
# where it is defined, not the module from which it is called).


# sample usage 
joe = Customer('John Doe', 0)
cart = [LineItem('banana',4,0.5), LineItem('apple', 10, 1.5)]
Order(joe, cart, fidelity_promo) # just pass the promotion function as an argument 

# more advanced usage 
# choose the best 
promos = [fidelity_promo, bulk_item_promo]
def best_promo(order):
    return max(promo(order) for promo in promos) # apply each of the functions from promos to the order and return max discount computed

# or use the globals() - dictionary of the current module 
promos = [globals()[name] for name in globals()
            if name.endswith('_promo')
            and name != 'best_promo']

def best_promo(order):
    """select best discount available
    """
    return max(promo(order) for promo in promos)



'''
another example shipping cost and order 
'''

# enscapsulate strategy as functions
class ShippingCost(object):
    def __init__(self, strategy):
        # takes in a strategy function
        self._strategy = strategy 
    
    def shipping_cost(self, order):
        # then leverages the specific implementation on the strategy object
        return self._strategy(order)

fedex_strategy = lambda order: 4.0
ups_strategy = lambda order: 3.0

cost_calculator = ShippingCost(fedex_strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 4.0

# context with strategy as part of the input
# enscapsulate strategy as functions
class ShippingCost(object):
    def __init__(self, strategy):
        # takes in a strategy object in the constructor
        self._strategy = strategy 
    
    def shipping_cost(self, order):
        # then leverages the specific implementation on the strategy object
        return self._strategy.calculation(order)
    
# the strategy ABC interface
from abc import ABCmeta, abstractclassmethod

class AbsStrategy(metaclass=ABCMeta)):
    @abstractclassmethod
    def calculate(self, order):
        """calculate shipping costs 
        """

# the concrete strategy / implementation 
class FedExStrategy(AbsStrategy):
    def calculate(self, order):
        return 3.00

class PostalStrategy(AbsStrategy):
    def calculate(self, order):
        return 5.00

# test 
order = Order()
strategy = FedExStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 3.0 



