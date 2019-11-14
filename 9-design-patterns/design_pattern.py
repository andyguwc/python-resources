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
# Example Order uses Promotion and we can implement variations of Promotions objects

# Context
# Provides a service by delegating some computation to interchangeable components
# that implement alternative algorithms. In the ecommerce example, the context is
# an Order, which is configured to apply a promotional discount according to one of
# several algorithms.

# Strategy
# The interface common to the components that implement the different algorithms.
# In our example, this role is played by an abstract class called Promotion.

# Concrete Strategy
# One of the concrete subclasses of Strategy. FidelityPromo, BulkPromo, and Large
# OrderPromo are the three concrete strategies implemented.

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

def fidelity_promo(order):
    """5% discount for customers with 1000 or more fidelity points"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0

# To apply a discount strategy to an Order, just pass the promotion function as an
# argument.
Order(joe, cart, fidelity_promo)

# Find the best promos 
promos = [fidelity_promo, bulk_item_promo, large_order_promo]

def best_promo(order):
    """Select best discount available
    """
    return max(promo(order) for promo in promos)

# Alternative using module
promos = [globals()[name] for name in globals()
            if name.endswith('_promo')
            and name != 'best_promo']
    
# globals()
# Return a dictionary representing the current global symbol table. This is always the
# dictionary of the current module (inside a function or method, this is the module
# where it is defined, not the module from which it is called).


from collectoins import namedtuple 

Customer = namedtuple('Customer', 'name fidelity')

class LinteItem:

    def __init__(self, product, quantity, price):
        self.product = product 
        self.quantity = quantity 
        self.price = price 
    
    def total(self):
        return self.price * self.quantity 
    
class Order: 

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
            discount = self.promotion(self)
        return self.total() - discount 
    
    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


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
promos = [globals()[name] for namein globals()
            if name.endswith('_promo')
            and name != 'best_promo']

def best_promo(order):
    """select best discount available
    """
    return max(promo(order) for promo in promos)


##################################################
#  Command Pattern
##################################################

# The goal of Command is to decouple an object that invokes an operation (the Invoker)
# from the provider object that implements it (the Receiver). In the example from Design
# Patterns, each invoker is a menu item in a graphical application, and the receivers are
# the document being edited or the application itself.

# Example: Each command may have a different receiver: the object that
# implements the action. For PasteCommand, the receiver is the Document. For Open‐
# Command, the receiver is the application.

# The Invoker is configured with a concrete command and calls its execute method to operate it.

# Building a list from the commands arguments ensures that it is iterable and keeps
# a local copy of the command references in each MacroCommand instance.
# When an instance of MacroCommand is invoked, each command in self.commands is called in sequence.

# Instead of giving the Invoker a Command instance, we can simply give it a function.
# Instead of calling command.execute(), the Invoker can just call command(). The Macro
# Command can be implemented with a class implementing __call__. Instances of Macro
# Command would be callables, each holding a list of functions for future invocation

class MacroCommand:
    """A command that executes a list of commands"""
    def __init__(self, commands):
        self.commands = list(commands)
    
    def __call__(self):
        for command in self.commands:
            command()

# Example the windows GUI
# example of invoker objects: keyboard, button click
# actions which occur (Exit, Save, etc.) are implementations of CommandInterface

# implement a simple command pattern that provides commands for Save and Exit actions 

# first a receiver class 
import sys 

class Window: 
    def exit(self):
        sys.exit(0)
    
class Document: 
    def __init__(self, filename):
        self.filename = filename
        self.contents = "This file cannot be modified"
    def save(self):
        with open(self.filename, 'w') as file:
            file.write(self.contents)

# invoker class 
# model toolbar, menu, etc. 

class ToolbarButton:
    def __init__(self, name, iconname):
        self.name = name
        self.iconname = iconname 
    
    def click(self):
        # calling command
        # command attribute to be set afterwards
        self.command.execute()

class MenuItem:
    def __init__(self, menu_name, menuitem_name):
        self.menu = menu_name
        self.item = menuitem_name
    
    def click(self):
        # calling command
        self.command.execute()

class SaveCommand:
    def __init__(self, document):
        self.document = document
    def execute(self):
        self.document.save()

window = Window()
document = Document("a_document.txt")
save = SaveCommand(document)
exit = ExitCommand(window)

save_button = ToolbarButton('save', 'save.png')
save_button.command = save
save_keystroke = KeyboardShortcut("s", "ctrl")
save_keystroke.command = save
exit_menu = MenuItem("File", "Exit")
exit_menu.command = exit


# a more python way of command pattern 
import sys
class Window: 
    def exit(self):
        sys.exit(0)
    
class MenuItem:
    def click(self):
        self.command()

window = Window()
menu_item = MenuItem()
menu_item.command = window.exit 



################################################
# Factory Pattern
################################################
# https://realpython.com/factory-method-python/

# Factory Method is a design pattern that creates objects with a common interface.

# The ._get_serializer() method is the creator component. 
# The creator decides which concrete implementation to use.

class SongSerializer:
    def serialize(self, song, format):
        serializer = get_serializer(format)
        return serializer(song)


def get_serializer(format):
    if format == 'JSON':
        return _serialize_to_json
    elif format == 'XML':
        return _serialize_to_xml
    else:
        raise ValueError(format)


def _serialize_to_json(song):
    payload = {
        'id': song.song_id,
        'title': song.title,
        'artist': song.artist
    }
    return json.dumps(payload)


def _serialize_to_xml(song):
    song_element = et.Element('song', attrib={'id': song.song_id})
    title = et.SubElement(song_element, 'title')
    title.text = song.title
    artist = et.SubElement(song_element, 'artist')
    artist.text = song.artist
    return et.tostring(song_element, encoding='unicode')


##################################################
#  Abstract Factory Pattern
##################################################

# The abstract factory pattern is normally used when we have multiple possible
# implementations of a system that depend on some configuration or platform issue.
# The calling code requests an object from the abstract factory, not knowing exactly
# what class of object will be returned. The underlying implementation returned may
# depend on a variety of factors, such as current locale, operating system, or local
# configuration

# Common examples of the abstract factory pattern include code for
# operating-system independent toolkits, database backends, and country-specific
# formatters or calculators. An operating-system-independent GUI toolkit might use an
# abstract factory pattern that returns a set of WinForm widgets under Windows, Cocoa
# widgets under Mac, GTK widgets under Gnome, and QT widgets under KDE.

class FranceDateFormatter:
    def format_date():
        pass  

class USADateFormatter:
    def format_date():
        pass 

class FranceCurrencyFormatter:
    def format_currency():
        pass 

class USACurrencyFormatter:
    def format_currency():
        pass 

# formatter factories 
class USAFormatterFactory:
    def create_date_formatter(self):
        return USADateFormatter()
    def create_currency_formatter(self):
        return USACurrencyFormatter()

class FranceFormatterFactory:
    def create_date_formatter(self):
        return FranceDateFormatter()
    def create_currency_formatter(self):
        return FranceCurrencyFormatter()

factory_map = {
    "US": USAFormatterFactory,
    "FR": FranceFormatterFactory,
}

formatter_factory = factory_map.get(country_code)()


##################################################
#  Decorator Pattern
##################################################

# The decorator pattern allows us to "wrap" an object that provides core functionality with other objects that alter this functionality. Any object that uses the decorated object will interact with it in exactly the same way as if it were undecorated (that is, the interface of the decorated object is identical to that of the core object).
# There are two primary uses of the decorator pattern:
# - Enhancing the response of a component as it sends data to a second component
# - Supporting multiple optional behaviors

# Here, Core and all the decorators implement a specific Interface. The decorators
# maintain a reference to another instance of that Interface via composition. When
# called, the decorator does some added processing before or after calling its wrapped
# interface. The wrapped object may be another decorator, or the core functionality.
# While multiple decorators may wrap each other, the object in the "center" of all
# those decorators provides the core functionality.


# Faced with a choice between decorators and inheritance
# only use decorators if we need to modify the object dynamically 

# Decorator example 

import socket
def respond(client):
    response = input("Enter a value: ")
    client.send(bytes(response, 'utf8'))
    client.close()

# create decorators to customize the socket behavior without having to extend or modify the socket itself
class LogSocket:
    def __init__(self, socket):
        self.socket = socket
    
    def send(self, data):
        print("Sending {0} to {1}".format(
            data, self.socket.getpeername()[0]))
        self.socket.send(data)

    def close(self):
        self.socket.close()

# this class decorates a socket object and presents the send and close interface to client sockets 
# a better decorator would also implement (all of the remaining socket methods)

# alternatives
#  - monkey patching
#  - multi inheritance
#  - function decorators 

# usage
# respond(LogSocket(client))

# another decorator
import gzip 
from io import BytestIO

class GzipSocket:
    def __init__(self, socket):
        self.socket = socket
    
    def send(self, data):
        buf = BytesIO()
        zipfile = gzip.GzipFile(fileobj=buf, mode="w")
        zipfile.write(data)
        zipfile.close()
        self.socket.send(buf.getvalue())
    def close(self):
        self.socket.close()
    
# now we can write code that dynamically switches between the decorators when responding 
client, addr = server.accpet()
if log_send:
    client = LoggingSocket(client)
if client.getpeername()[0] in compress_hosts:
    client = GzipSocket(client)
respond(client)


##################################################
#  Observer Pattern
##################################################

# The observer pattern is useful for state monitoring and event handling situations.
# This pattern allows a given object to be monitored by an unknown and dynamic
# group of "observer" objects.

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


# example 
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

##################################################
#  State Pattern
##################################################

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

# example a XML Parser

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

##################################################
#  Singleton
##################################################

# The basic idea behind the singleton pattern is to allow exactly one instance of a
# certain object to exist. Typically, this object is a sort of manager class

# In most programming environments, singletons are enforced by making the
# constructor private (so no one can create additional instances of it), and then providing
# a static method to retrieve the single instance. This method creates a new instance the
# first time it is called, and then returns that same instance each time it is called again.

# singleton implementation 
# use the __new__ class method to ensure only one instance is ever created
class OneOnly:
    _singleton = None 
    def __new__(cls, *args, **kwargs):
        if not cls._singleton:
            cls._singleton = super(OneOnly, cls).
            __new__(cls, *args, **kwargs)
        return cls._singleton
# by overriding __new__, we first check if our singleton if our singleton instance has been created; if not, we create
# it using a super call. Thus, whenever we call the constructor on OneOnly, we always
# get the exact same instance
o1 = OneOnly()
o2 = OneOnly()
o1 == o2 


##################################################
#  Template Pattern
##################################################

# It is designed for situations where we have several
# different tasks to accomplish that have some, but not all, steps in common. The
# common steps are implemented in a base class, and the distinct steps are overridden
# in subclasses to provide custom behavior. In some ways, it's like a generalized
# strategy pattern, except similar sections of the algorithms are shared using a base class.

# example 
# connect to SQLite database get results and format the results.
# The common steps are connecting and outputing which we can put into a template pattern 

class QueryTemplate:
    def connect(self):
        self.conn = sqlite3.connect("sales.db")

    # this method is outside of template and needs subclass to override 
    def construct_query(self):
        raise NotImplementedError()

    def do_query(self):
        results = self.conn.execute(self.query)
        self.results = results.fetchall()

    def format_results(self):
        output = []
        for row in self.results:
            row =[str(i) for i in row]
            output.append(", ".join(row))
        self.formatted_results = "\n".join(output)
    
    def output_results(self):
        raise NotImplementedError()
    
    # this method calls all steps
    def process_format(self):
        self.connect()
        self.construct_query()
        self.do_query()
        self.format_results()
        self.output_results()


# concete class 
import datetime
class NewVehiclesQuery(QueryTemplate):
    def construct_query(self):
    self.query = "select * from Sales where new='true'"
    def output_results(self):
    print(self.formatted_results)

##################################################
#  Adapter Pattern
##################################################
# adapters allow two pre-existing objects to work together even if interfaces are not compatible
# The adapter object's sole purpose is to perform this translation job. 
# Adapting may entail a variety of tasks, such as converting arguments to a different format, rearranging the order of arguments, calling a differently named method, or supplying default arguments.
# Map between two interfaces

# example, we have a preexisting class which takes a string date in the format "YYYY-MM-DD"
class AgeCalculator:
    def __init__(self, birthday):
        self.year, self.month, self.day = (
            int(x) for x in birthday.split('-'))
    
    def calculate_age(self, date):
        year, month, day = (
            int(x) for x in date.split('-'))
        age = year - self.year
        if (month,day) < (self.month,self.day):
            age -= 1
        return age
    
# rewrite the class to accept datetime objects 
# whenever we want to calculate the age on a datetime.date object, we could call
# datetime.date.strftime('%Y-%m-%d') to convert it to the proper format
# write an adapter that allows a normal date to be plugged into a normal AgeCalculator class 
import datetime
class DateAgeAdapter:
    def _str_date(self, date):
        return date.strftime("%Y-%m-%d")
    
    def __init__(self, birthday):
        birthday = self._str_date(birthday)
        self.calculator = AgeCalculator(birthday)
    
    def get_age(self, date):
        date = self._str_date(date)
        return self.calculator.calculate_age(date)
    

##################################################
#  Facade Pattern
##################################################

# The facade pattern is designed to provide a simple interface to a complex system of
# components. For complex tasks, we may need to interact with these objects directly,
# but there is often a "typical" usage for the system for which these complicated
# interactions aren't necessary.
# The facade pattern allows us to define a new object that encapsulates this typical usage of the system
# facade is like an adapter, difference is facade is trying to abstract a simpler interface out of a complex one while adapater is mapping one to another 

# example write a email tool 
# the underlying python libraries are very complex 
# facade performs two tasks - 1) sending an email to a specific address 2) checking the inbox on a connection
import smtplib 
import imaplib 

class EmailFacade:
    def __init__(self, host, username, password):
        self.host = host 
        self.username = username 
        self.password = password 
    
    # send_email method formats the email and sends it using smtplib
    def send_email(self, to_email, subject, message):
        if not "@" in self.username:
            from_email = "{0}@{1}".format(
                self.username, self.host)
        else:
            from_email = self.username

        message = ("From: {0}\r\n"
                "To: {1}\r\n"
                "Subject: {2}\r\n\r\n{3}").format(
                from_email,
                to_email,
                subject,
                message)
        smtp = smtplib.SMTP(self.host)
        smtp.login(self.username, self.password)
        smtp.sendmail(from_email, [to_email], message)

    def get_inbox(self):
        mailbox = imaplib.IMAP4(self.host)
        mailbox.login(bytes(self.username, 'utf8'),
            bytes(self.password, 'utf8'))
        mailbox.select()
        x, data = mailbox.search(None, 'ALL')
        messages = []
        for num in data[0].split():
            x, message = mailbox.fetch(num, '(RFC822)')
            messages.append(message[0][1])
        return messages 


##################################################
#  Flyweight Pattern
##################################################

# The flyweight pattern basically ensures that objects that share a state can use the
# same memory for that shared state. It is often implemented only after a program
# has demonstrated memory problems. It may make sense to design an optimal
# configuration from the beginning in some situations, but bear in mind that
# premature optimization is the most effective way to create a program that is too
# complicated to maintain.

# Each Flyweight has no specific state; any time it needs to perform an operation on
# SpecificState, that state needs to be passed into the Flyweight by the calling code.
# Traditionally, the factory that returns a flyweight is a separate object; its purpose
# is to return a flyweight for a given key identifying that flyweight.

# example car model factory

import weakref 

class CarModel:
    _models = weakref.WeakValueDictionary()

    # whenver we construct a new flyweight with a given name, 
    # first look at the name in the weak referenced dictionary 
    # (if exists, return the model, if not create a new one)

    def __new__(cls, model_name, *args, **kwargs):
        model = cls._models.get(model_name)
        if not model: 
            model = super().__new__(cls)
            cls._models[model_name] = model 
        return model 
    
    def __init__(self, model_name, air=False, tilt=False,
        cruise_control=False, power_locks=False,
        alloy_wheels=False, usb_charger=False):
        # only intialized object the first time it is called 
        if not hasattr(self, "initted"):
            self.model_name = model_name
            self.air = air
            self.tilt = tilt
            self.cruise_control = cruise_control
            self.power_locks = power_locks
            self.alloy_wheels = alloy_wheels
            self.usb_charger = usb_charger
            self.initted=True
        

##################################################
#  Composite Pattern
##################################################

# The composite pattern allows complex tree-like structures to be built from simple
# components. These components, called composite objects, are able to behave sort
# of like a container and sort of like a variable depending on whether they have child
# components. Composite objects are container objects, where the content may actually
# be another composite object.

# example use composite object to represent folders and leaf nodes to represent normal firles

# abstract away the similar operations in File and Folder 

class Component:
    def __init__(self, name):
        self.name = name 
    
    def move(self, new_path):
        new_folder = get_path(new_path)
        del self.parent.children[self.name]
        new_folder.children[self.name] = self 
        self.parent = new_folder
    
    def delete(self):
        del self.parent.children[self.name]
    
class Folder(Component):
    def __init__(self, name):
        super().__init__(name)
        self.children = {}
    def add_child(self, child):
        child.parent = self 
        self.children[child.name]

    def copy(self, new_path):
        pass

class File(Component):
    def __init__(self, name, contents):
        super().__init__(name)
        self.contents = contents
    def copy(self, new_path):
        pass

root = Folder('')
def get_path(path):
    names = path.split('/')[1:]
    node = root
    for name in names:
        node = node.children[name]
    return node 

# >>> folder1 = Folder('folder1')
# >>> folder2 = Folder('folder2')
# >>> root.add_child(folder1)
# >>> root.add_child(folder2)
# >>> folder11 = Folder('folder11')
# >>> folder1.add_child(folder11)

