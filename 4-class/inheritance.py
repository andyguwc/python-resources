##################################################
#  Inheritance 
##################################################

'''
initialize
'''
# subclasses will want to initialize base classes
# base class initializer will only be called automatically if subclass initializer is undefined
# use super() to call base class __init__()


'''
super()
'''
# given a MRO and class C, super() gives you an object which resolves methods using only 
# part of the MRO which comes after C

# instance method
# super() is same as super(class-of-method, self)

# class method 
# super() is same as super(class-of-method, class) which is typically method of the base class


# use the super() function 
# specify just the differences in the new inherited class

class HighSchoolStudent(Student):
    school_name = 'new high school'

    def get_name(self):
        original_value = super().get_name()

# class SubClass(BaseClass)
# base class __init__() is not called if overwritten, unless define init as super().__init__()

# super() used to call method on base class

class SimpleList:
    def __init__(self, items):
        self._items = items
    
    def add(self, item):
        self._items.append(item)
    
    def __getitem__(self, index):
        return self._items[index]
    
    def sort(self):
        self._items.sort()
    
    def __len__(self):
        return len(self._items)
    
    def __repr__(self):
        return "Simplelist({!r})".format(self._items)

# handling the __init__() method to make sure the superclasses are property intialized 
class SortedList(SimpleList):
    def __init__(self, items=()):
        # call SimpleList initializer
        super().__init__(items)
        self.sort()
    
    def add(self, item):
        # calling super here 
        super().add(item)
        self.sort()
    
    def __repr__(self):
        return "SortedList({!r})".format(list(self))

'''
object base class
'''
# every class
class X:
    pass
X.__class__ # <class 'type'> class is an object of the class named type
X.__class__.__base__ # <class 'object'> base class is named object



'''
cross reference attributes between super and sub class 
'''
# superclass and subclass can access attributes from each other 
# typical polymorphic design. Each subclass provides a unique
# implementation of the _points() method. All the subclasses have identical methods and attributes. 
# Objects of these three subclasses can be used interchangeably in an application

class Card: 
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


'''
polymorphism
'''
# different behaviors happen depending on which subclass is being used, without having to explicitly know what the subclass actually is.
# use objects of different types through a common interface
# determined at the time of use

# Polymorphism is a way for multiple classes in a hierarchy to implement their own unique
# versions of a method. This allows many classes to fulfill the same interface or abstract
# base class while providing different functionality 

# checka valid extension was given upon initialization. Note the __init__ method in the parent class is able to access
# the ext class variable from different subclasses. That's polymorphism at work. If the filename doesn't end with the correct name, it raises an exception. 
# The fact that AudioFile doesn't actually store a reference to the ext variable doesn't stop it from being able to access it on the subclass.

class AudioFile:
    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception("Invalid file format")
        self.filename = filename

class MP3File(AudioFile):
    ext = "mp3"
    def play(self):
        print("playing {} as mp3".format(self.filename))

'''
duck typing
'''

# Polymorphism is one of the most important reasons to use inheritance in many
# object-oriented contexts. Because any objects that supply the correct interface can
# be used interchangeably in Python, it reduces the need for polymorphic common
# superclasses. Inheritance can still be useful for sharing code but, if all that is being
# shared is the public interface, duck typing is all that is required. This reduced need
# for inheritance also reduces the need for multiple inheritance; often, when multiple
# inheritance appears to be a valid solution, we can just use duck typing to mimic one
# of the multiple superclasses.

# Duck typing in Python allows us to use any object that provides the required behavior
# without forcing it to be a subclass. The dynamic nature of Python makes this trivial.
# The following example does not extend AudioFile, but it can be interacted with in
# Python using the exact same interface:
class FlacFile:
    def __init__(self, filename):
        if not filename.endswith(".flac"):
        raise Exception("Invalid file format")
        self.filename = filename
    
    def play(self):
        print("playing {} as flac".format(self.filename))


# Another useful feature of duck typing is that the duck-typed object only needs to
# provide those methods and attributes that are actually being accessed. For example,
# if we needed to create a fake file object to read data from, we can create a new object
# that has a read() method; we don't have to override the write method if the code
# that is going to interact with the object will only be reading from the file. More
# succinctly, duck typing doesn't need to provide the entire interface of an object that
# is available, it only needs to fulfill the interface that is actually accessed.


'''
Delegate Attribute Access
'''
# want an instance to delegate attribute access to an internally held instance 
# as an alternative to inheritance or in order to implement a proxy

class A: 
    def spam(self, x):
        pass 

    def foo(self):
        pass 

class B: 
    def __init__(self):
        self._a = A()
    
    def spam(self, x):
        # delegate to the internal self._a instance 
        return self._a.spam(x)

    def foo(self)
        return self._a.foo()
    
    def bar(self):
        pass 

# if having a lot of attributes to delegate, define the __getattr__()

class A: 
    def spam(self, x):
        pass

    def foo(self):
        pass 

class B: 
    def __init__(self):
        self._a = A()

    def bar(self):
        pass 

    # expose all of the methods defined on class A 
    def __getattr__(self, name):
        return getattr(self._a, name)

# The __getattr__() method is kind of like a catch-all for attribute lookup. It’s a method
# that gets called if code tries to access an attribute that doesn’t exist.


'''
strategy object initilization
'''

# create strategy objects 
# raise an exception for methods that must be implemented by a subclass
class BettingStrategy:
    def bet( self ):
        raise NotImplementedError( "No bet method" )
    def record_win( self ):
        pass
    def record_loss( self ):
        pass

class Flat(BettingStrategy):
    def bet( self ):
        return 1

# subclass must overrride the basic bet() method 


##################################################
#  Multiple Inheritance 
##################################################


# define class with more than one base class 
class SubClass(Base1, Base2):
    pass
# subclass inherit methods of all bases 
# if a class defines no intializer, then only the init from the first base class is called
# __bases__ a tuple of base classes 

# We can use multiple inheritance in a disciplined way to create cross-cutting aspects. 
# We'll consider a base class plus mixin class definitions to introduce features. Often, we'll use the mixin classes to build cross-cutting aspects.
# if a class has multiple base classes and defines no intializer, then only the initializer of the first base class is automatically called

# best practice
# use multiple inheritance only for mix-in utility 
# If you find yourself desiring the convenience and encapsulation that comes with multiple
# inheritance, consider writing a mix-in instead. A mix-in is a small class that only defines a
# set of additional methods that a class should provide. Mix-in classes don’t define their
# own instance attributes nor require their __init__ constructor to be called.


'''
method resolution order 
'''
# An object's class will define a Method Resolution Order (MRO).
# This defines how base classes are searched to locate an attribute or method name.
# The MRO works its way up the inheritance hierarchy; this means that subclass
# names override superclass names. This implementation method search meets our
# expectation for what inheritance means.

bool.__mro__
# (<class 'bool'>, <class 'int'>, <class 'object'>)

# super()
# given a MRO and class C, super() gives you an object which resolves methods using only part of the MRO which comes after C


'''
initialization
'''

# distinguish interface inheritance from implementation inheritance
# inheritance of interface creates a subtype, implying a "is-a" relationship
# inheritance of implementation avoids code duplication by reuse 

# making interfaces explicit with ABCs
# if a class is designed to define an interface, it should be an explicit ABC (i.e. subclass abc.ABC)

# We've changed all arguments to keyword arguments by giving them an empty
# string as a default value. We've also ensured that a **kwargs parameter is included
# to capture any additional parameters that our particular method doesn't know what
# to do with. It passes these parameters up to the next class with the super call.

class Contact:
    all_contacts = []
    def __init__(self, name='', email='', **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        self.all_contacts.append(self)


class AddressHolder:
def __init__(self, street='', city='', state='', code='',**kwargs):
    super().__init__(**kwargs)
    self.street = street
    self.city = city
    self.state = state
    self.code = code


class Friend(Contact, AddressHolder):
    def __init__(self, phone='', **kwargs):
        super().__init__(**kwargs)
        self.phone = phone

##################################################
# Mixins 
##################################################

# when defining a class, the following sources of attributes and methods 
# the class statement 
# the decorators applied to the class definition
# the mixin classes with the base class that is given last 

'''
cross cutting scenarios
'''
# Logging: We often need to have logging features implemented consistently
# in many classes. We want to be sure the loggers are named consistently and
# logging events follow the class structure in a consistent manner.

# Auditability: A variation of the logging theme is to provide an audit trail
# that shows each transformation of a mutable object. In many commerceoriented
# applications, the transactions are business records that represent
# bills or payments.

# Security: Our applications will often have security aspects that pervade
# each HTTP request and each piece of content downloaded by the website.
# The idea is to confirm that each request involves an authenticated user
# who is authorized to make the request.


# to support that, python offers 
# Decorators: With a decorator, we can establish a consistent aspect
# implementation at one of two simple join points in a function. We can
# perform the aspect's processing before or after the existing function. We
# can't easily locate join points inside the code of a function. It's easiest for
# decorators to transform a function or method by wrapping it with additional
# functionality.

# Mixins: With a mixin, we can define a class that exists outside a single
# class hierarchy. The mixin class can be used with other classes to provide
# a consistent implementation of a cross-cutting aspect. For this to work, the
# mixin API must be used by the classes that it is mixed into. Generally, mixin
# classes are considered abstract since they can't be meaningfully instantiated.

'''
mixin examples
'''
# example using MailSender mixin to send emails 
class MailSender:
    def send_mail(self, message):
    print("Sending mail to " + self.email)
    # Add e-mail logic here

class EmailableContact(Contact, MailSender):
    pass

# e = EmailableContact("John Smith", "jsmith@example.net")
# e.send_mail("Hello, test e-mail here")


# context manager 
import contextlib.ContextDecorator 

class TestDeck(ContextDecorator, Deck):
    def __init__(self, size=1, seed=0):
        super().__init__(size=size)
        self.seed=seed

    def _init_shuffle(self):
        pass 
    
    def __enter__(self):
        self.rng.seed(self.seed, version=1)
        self.rng.shuffle(self)
        return self 
    
    def __exit__(self, exc_type, exc_value, traceback):
        pass 

# using the contextmanager decorator 
# make objects/functions capable of use in with statements by using the contextlib built in modle 
# example - elevate the log level of a function temporarily by using a context manager
@contextmanager 
def debug_logging(level):
    logger = logging.getLogger()
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield logger 
    finally:
        logger.setLevel(old_level)

# The yield expression is the point at which the with block’s contents will execute. Any
# exceptions that happen in the with block will be re-raised by the yield expression for
# you to catch in the helper function

# usage 
with log_level(logging.DEBUG, 'my-log') as logger:
    logger.debug('This is my message')
    logging.debug('This will not print')


'''
monkey patching
'''
# changing a class or module at runtime without touching the source code 
# for example replace or add methods (using functions as attributes) at run time 
def set_card(deck, position, card):
    deck._cards[position] = card 

FrenchDeck.__setitem__ = set_card 
shuffle(deck)

# The trick is that set_card knows that the deck object has an attribute named _cards,
# and _cards must be a mutable sequence. The set_card function is then attached to the
# FrenchDeck class as the __setitem__ special method



##################################################
#  Interfaces
##################################################

'''
informal interfaces
'''
# https://realpython.com/python-interface/#informal-interfaces

# only defines the abtract interfaces
class InformalParserInterface:
    def load_data_source(self, path, file_name):
        pass

    def extract_text(self, full_file_name):
        pass

# As you can see, InformalParserInterface looks identical to a standard Python class. You rely on duck typing to inform users that this is an interface and should be used accordingly.

class PdfParser(InformalParserInterface):
    def load_data_source(self, path, file_name):
        print("concrete implementations")

    def extract_text(self, full_file_name):
        print("concrete")



'''
informal interfaces using metaclasses
'''
# Ideally, you would want issubclass(EmlParser, InformalParserInterface) to return False when the implementing class doesn’t define all of the interface’s abstract methods. To do this, you’ll create a metaclass called ParserMeta.

# you’ll be overriding two dunder methods:
# .__instancecheck__()
# .__subclasscheck__()


class ParserMeta(type):
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))
    
    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and 
                callable(subclass.load_data_source) and 
                hasattr(subclass, 'extract_text') and 
                callable(subclass.extract_text))


class UpdatedInformalParserInterface(metaclass=ParserMeta):
    """This interface is used for concrete classes to inherit from.
    There is no need to define the ParserMeta methods as any class
    as they are implicitly made available via .__subclasscheck__().
    """
    pass

# by using a mtaclass, you don't need to explicitly define the subclasses

class PdfParserNew:
    def load_data_source(self, path, file_name):
        pass

    def extract_text(self, full_file_path):
        pass


'''
formal interfaces using abc.ABCMeta
'''

# Rather than create your own metaclass, you’ll use abc.ABCMeta as the metaclass. Then, you’ll overwrite .__subclasshook__() in place of .__instancecheck__() and .__subclasscheck__(), as it creates a more reliable implementation of these dunder methods.

import abc

class FormParserInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'load_data_source') and 
                callable(subclass.load_data_source) and 
                hasattr(subclass, 'extract_text') and 
                callable(subclass.extract_text))


class PdfParserNew:
    def load_data_source(self, path, file_Name):
        pass

    def extract_text(full_file_path):
        pass


issubclass(PdfParserNew, FormParserInterface) # True









