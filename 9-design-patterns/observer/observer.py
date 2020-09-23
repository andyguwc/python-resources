##################################################
#  Observer Pattern
##################################################

# The observer pattern is useful for state monitoring and event handling situations.
# This pattern allows a given object to be monitored by an unknown and dynamic
# group of "observer" objects. Also known as dependents pattern and publish-subscribe pattern 

# Whenever a value on the core object changes, it lets all the observer objects know
# that a change has occurred, by calling an update() method. Each observer may
# be responsible for different tasks whenever the core object changes; the core object
# doesn't know or care what those tasks are, and the observers don't typically know
# or care what other observers are doing.

# The observer pattern detaches the code being observed from the code doing the
# observing. If we were not using this pattern, we would have had to put code in each of
# the properties to handle the different cases that might come up; logging to the console,
# updating a database or file, and so on. The code for each of these tasks would all be
# mixed in with the observed object.

'''
structure
'''
# a subject - with attach, detach and notify methods 
# many observers to obtain updates - each observer having the update method
# observers can also get/set state
# when a subject's state changes, it lopps through the attached observers and calls each update method
# when called, the update() method calls the get state method from the subject

# essentially defines a one to many relationship notify the many when the one changes

'''
example - many observers creating serialized copy 
'''
# redundant backup - write a core object that maintains certain values
# then have one or more observers create serialized copies of that object 

# core object
class Inventory:
    def __init__(self):
        self.observers = []
        self._product = None
        self._quantity = 0
    
    def attach(self, observer):
        self.observers.append(observer)
    
    @property
    def product(self):
        return self._product
    
    # when the property is set, call the _update_observers on itself
    @product.setter 
    def product(self, value):
        self._product = value 
        self._update_observers()
    
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter 
    def quantity(self, value):
        self._quantity = value 
        # for any update let the observer know
        self._update_observers()
    
    # loop through each observer and call it
    def _update_observers(self):
        for observer in self.observers:
            observer()


class ConsoleObserver:
    def __init__(self, inventory):
        self.inventory = inventory 
    
    def __call__(self):
        print(self.inventory.product)
        print(self.inventory.quantity)

# i = Inventory()
# c = ConsoleObserver(i)
# i.attach(c)
# i.product = "Widget"

'''
another example - dashboard consuming changes from KPI Data 
'''
# Observer pattern - when the state of one changes, its dependents are notified
# Also known as dependents pattern or publish-subscribe pattern

# Use ABCs for subject and observer
# build concrete classes using the ABCs
# Use two observers

from abc import abstractmethod, ABCMeta

# abstract observer
class AbsObserver(metaclass=ABCMeta):
    @abstractmethod 
    def update(self, value):
        pass 

    # context manager 
    def __enter__(self):
        return self 
    
    @abstractmethod
    def __exit__(self, exc_type, exc_value, traceback):
        pass

# abstract subject
# publisher
class AbsSubject(metaclass=ABCMeta):
    _observers = set()
    
    # add new observer
    def attach(self, observer):
        if not isinstance(observer, AbsObserver):
            raise TypeError('Observer not derived from AbsObserver')
        self._observers |= {observer}
    
    # remove observer from the set
    def detach(self, observer):
        self._observers -= {observer}
    
    # for each observer, invoke the update method
    def notify(self, value=None):
        for observer in self._observers:
            if value is None:
                observer.update()
            else:
                observer.update(value)

    # context manager 
    # clearing the set of observers 
    @abstractmethod
    def __exit__(self, exc_type, exc_value, traceback):
        self._observers.clear()


# KPI class (subject)
class KPI(AbsSubject):
    _open_tickets = -1
    _closed_tickets = -1 
    _new_tickets = -1

    # defines properties for the values to be tracked
    @property 
    def open_tickets(self):
        return self._open_ticket
    
    @property
    def closed_tickets(self):
        return self._closed_tickets

    @property 
    def new_tickets(self):
        return self._new_tickets

    def set_kpis(self, open_tickets, closed_tickets, new_tickets):
        self._open_tickets = open_tickets
        self._closed_tickets = closed_tickets
        self._new_tickets = new_tickets
        # notify method is called 
        self.notify()


# observer
class CurrentKPI(AbsObserver):
    open_tickets = -1
    closed_tickets = -1 
    new_tickets = -1 

    def __init__(self, kpis):
        # take a reference of the subject/publisher
        self._kpis = kpis
        kpis.attach(self)
    
    # implement the update method
    # observer can get/set state
    def update(self):
        self.open_tickets = self._kpis.open_tickets
        self.closed_tickets = self._kpis.closed_tickets
        self.new_tickets = self._kpis.new_tickets
        self.display()

    def display(self):
        print('Current open tickets: {}'.format(self.open_tickets))
        print('New tickets closed: {}'.format(self.new_tickets))

    def __exit__(self, exc_type, exc_value, traceback):
        self._kpis.detach(self)


# this ensures after exit the observers are no longer notified
# observers will detach themselves - no dangling relationships
with KPIs() as kpis:
    with CurrentKPI(kpis):
        kpis.set_kpis(25,10,5)

