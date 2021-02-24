
##################################################
# Serialization
##################################################

# A persistent object is one that has been written to some storage medium. 
# The object can be retrieved from storage and used in a Python application. 
# Perhaps the object was represented in JSON and written to the filesystem. 
# Perhaps an object-relational mapping (ORM) layer has represented the object as rows in SQL tables to store the object in a database

# We'll need to separate persistence from other features such as the core processing of our application and the presentation of data to users.

'''
serializaiton
'''
# Data serialization is the concept of converting structured data into a format that
# allows it to be shared or stored—retaining the information necessary to reconstruct
# the object in memory at the receiving end of the transmission (or upon read from
# storage).

# To make a Python object persistent, we must convert it to bytes and write the bytes to a file. 
# We'll call this serialization; it is also called marshaling, deflating or encoding

# serialization representations
# JSON, YAML, pickle, CSV, XML

# We define an object's instance variables to properly show the dynamic
# state of the object. We use class-level attributes for information that objects of that
# class will share. If we can persist only the dynamic state of an object—separated from
# the class and the web of references that are part of the class definition—that would
# be a workable solution to serialization and persistence.


# dump(object, file) dump the given object to the file 
# dumps(object) will dump an object, returning a string representation
# load(file) will load an object from the given file, returning the constructed object
# loads(string) load an object from string representation, returning the constructed object 

# defining classes to support persistence 

class Post:
    def __init__(self, date, title, rst_text, tags):
        self.date = date
        self.title = title 
        self.rst_text = rst_text 
        self.tags = tags 
    
    def as_dict(self):
        return dict(
            date = str(self.date),
            title=self.title,
            underline= "-"*len(self.title),
            rst_text= self.rst_text,
            tag_text= " ".join(self.tags),
        )


##################################################
# JSON
##################################################
'''
JSON
'''

# Python JSON
# dict object
# list, tuple array
# str string
# int, float number
# True true
# False false
# None 

# print with formatting 
import json
print( json.dumps(travel.as_dict(), indent=4) )

'''
supporting JSON in classes
'''

# For encoding our objects into JSON, we need to provide a function that will reduce our objects to Python primitive types. This is called a default
# function; it provides a default encoding for an object of an unknown class.

# To decode our objects from JSON, we need to provide a function that will transform
# a dictionary of Python primitive types back into an object of the proper class. This is
# called the object hook function; it's used to transform dict to an object of a customized class.

# for class hinting, provide 
# __class__ key that names the target class
# The __args__ key will provide a sequence of positional argument values
# A __kw__ key will provide a dictionary of keyword argument values

# encode
def blog_encode(object):
    if isinstance(object, datetime.dateitime):
        return dict(
            __class__ = "datetime.datetime",
            __args__ = [],
            __kw__ = dict(
                year = object.year,
                month = object.month, 
                day = object.day, 
                hour = object.hours,
                minute = object.minute, 
                second = object.second 
            )
        )
    
    elif isinstance(object, Post):
        return dict(
            __class__= "Post",
            __args__= [],
            __kw__= dict(
            date= object.date,
            title= object.title,
            rst_text= object.rst_text,
            tags= object.tags,
            )
        )
    elif isinstance(object, Blog):
        return dict(
            __class__= "Blog",
            __args__= [
            object.title,
            object.entries,
            ],
            __kw__= {}
        )
    else:
        return json.JSONEncoder.default(o)


# then we can encode as follows
travel = Blog("travel")

travel.append(
    Post(
        ...
    )
)

text = json.dumps(travel, indent=4, default=blog_encode) 


class Contact:
    def __init__(self, first, last):
        self.first = first 
        self.last = last 
    
    @property 
    def full_name(self):
        return ("{}{}".format(self.first, self.last))

# create a custom encoder 
# The default method basically checks to see what kind of object we're trying to
# serialize; if it's a contact, we convert it to a dictionary manually; otherwise, we let
# the parent class handle serialization (by assuming that it is a basic type, which json
# knows how to handle).

import json 
class ContactEncoder(json.JSONEncoder):
    def default(self, obj):
        if instance(obj, Contact):
            return {'is_contact': True, 
                    'first': obj.first,
                    'last': obj.last, 
                    'full': obj.full_name}
        return super().default(obj)

# for decoding, write a function that accepts a dictionary and checks the existen of the is_contact to decide whether to convert to a contact
def decode_contact(dic):
    if dic.get('is_contact'):
        return Contact(dic['first'], dic['last'])
    else:
        return dic 

data = ('{"is_contact": true, "last": "smith","full": "john smith", "first": "john"}')
c = json.loads(data, object_hook=decode_contact)


# decode
# The JSON decoder "object hook" is a function that's invoked for each dict to see if
# it represents a customized object. If dict isn't recognized by the hook function, then
# it's just a dictionary and should be returned without modification.

def blog_decode(some_dict):
    if set(some_dict.keys()) == set(["__class__", "__args__", "__kw__"]):
        class = eval(some_dict['__class__'])
        return class_(*some_dict['__args__'], **some_dict['__kw__'] )
    else:
        return some_dict

# do the decoding
blog_data = json.loads(text, object_hook=blog_decode)


# writing json to a file 
with open("temp.json", "w", encoding="UTF-8") as target:
    json.dump( travel3, target, separators=(',', ':'), default=blog_j2_encode)


##################################################
# YAML
##################################################

# Technically, then, we can prepare YAML data using the json module. However, the
# json module cannot be used to de-serialize more sophisticated YAML data.

# Benefit: PyYAML implementation has a deep level of integration with Python that allows us to very simply create
# YAML encodings of Python objects.



import yaml
text= yaml.dump(travel2)
print( text )

with open("some_destination.yaml", "w", encoding="UTF-8") as target:
    yaml.dump( some_collection, target )

# when reading files
with open("some_source.yaml", "r", encoding="UTF-8") as source:
    objects= yaml.load( source )


##################################################
# Pickle
##################################################


'''
pickle basics
'''
# https://pymotw.com/3/pickle/index.html
# The pickle module implements an algorithm for turning an arbitrary Python object into a series of bytes. This process is also called serializing the object. The byte stream representing the object can then be transmitted or stored, and later reconstructed to create a new object with the same characteristics.

# The documentation for pickle makes clear that it offers no security guarantees. In fact, unpickling data can execute arbitrary code. Be careful using pickle for inter-process communication or data storage, and do not trust data that cannot be verified as secure.


import pickle

data = [{'a': 'A', 'b': 2, 'c': 3.0}]

data_string = pickle.dumps(data)
print('PICKLE: {!r}'.format(data_string))

data2 = pickle.loads(data_string)

# native format to make objects persistent 

# The pickle module can transform a complex object into a byte stream and it can transform the byte stream into an object with the same internal structure.


import pickle 

# The dump method accepts an object to be written and a file-like object to write the serialized bytes to.
with open("travel_blog.p", "wb") as target:
    pickle.dump(travel, target)

# The load method does exactly the opposite; it reads a serialized object from a file-like object. 
with open("travel_blog.p", "rb") as source:
    copy = pickle.load(source)


sample_dict = { 'Alice': 89, 'Bob': 72, 'Charles': 87 }
# use dumps to convert the object to a serialized string 
serial_data = pickle.dumps(sample_dict)

# use loads to de-serialize an object 
received_data = pickle.loads(serial_data)


'''
pickle and file like streams
'''
# write a pickled object to stream and load from it

import io
import pickle

class SimpleObject:

    def __init__(self, name):
        self.name = name
        self.name_backwards = name[::-1]
        return

data = []
data.append(SimpleObject('pickle'))
data.append(SimpleObject('preserve'))
data.append(SimpleObject('last'))

# simulate a file
out_s = io.BytesIO()

# write to the stream
for o in data:
    print('WRITING : {} ({})'.format(o.name, o.name_backwards))
    pickle.dump(o, out_s)
    out_s.flush()

# setup a readable stream
in_s = io.BytesIO(out_s.getvalue())

while True:
    try:
        o = pickle.load(in_s)
    except EOFError:
        break
    else:
        print('READ    : {} ({})'.format(
            o.name, o.name_backwards))

'''
pickle objects
'''

# note for reconstructing an object from a pickled file / stream, need to make sure the file has the object Class

# unpickable objects
# file handles, database connections,and other objects with runtime state that depends on OS or another process may not be saved in a meaningful way






# designing a class for reliable pickle processin
# The __init__() method of a class is not actually used to unpickle an object. The
# __init__() method is bypassed by using __new__() and setting the pickled values
# into the object's __dict__ directly.

# This distinction matters when our class definition includes some processing in __init__(). For example, if __init__() opens external
# files, creates some part of a GUI interface, or performs some external update to a
# database, then this will not be performed during unpickling.

# A class that relies on processing during __init__() has to make special
# arrangements to be sure that this initial processing will happen properly. There are
# two things we can do:
# • Avoid eager startup processing in __init__(). Instead, do one-time
# initialization processing. For example, if there are external file operations,
# these must be deferred until required.
# • Define the __getstate__() and __setstate__() methods that can be used
# by pickle to preserve the state and restore the state. The __setstate__()
# method can then invoke the same method that __init__() invokes to
# perform a one-time initialization processing in ordinary Python code.

class Hand:
    def __init__( self, dealer_card, *cards ):
        self.dealer_card= dealer_card
        self.cards= list(cards)
        # processing during __init__ stage
        for c in self.cards:
        audit_log.info( "Initial %s", c )

    def append(self, card):
        self.cards.append(card)
        audit_log.info("Hit %s", card)
    
    def __str__(self):
        cards= ", ".join( map(str,self.cards) )
        return "{self.dealer_card} | {cards}".format( self=self,cards=cards )

    def __getstate__(self):
        return self.__dict__
    
    def __setstate__(self, state):
        self.__dict__.update(state)
        for c in self.cards:
            audit_log.info( "Initial (unpickle) %s", c )


##################################################
# Storing and Retrieving Objects via Shelve
##################################################

# The shelve module defines a mapping-like container in which we can store objects.
# Each stored object is pickled and written to a file. We can also unpickle and retrieve
# any object from the file. The shelve module relies on the dbm module to save and
# retrieve objects.



##################################################
# Config Files
##################################################

# Use cases for configuration file 
#  - A person needs to edit a configuration file 
#  - A piece of software will read a configuration file and make use of the options / arguments to tailor its behavior
#  - Another use to save a configuration back to a file after an application has updated it 


# • Default values
# • Device names, which may overlap with the filesystem's location
# • Filesystem locations and search paths
# • Limits and boundaries
# • Message templates and data format specifications
# • Message text, possibly translated for internationalization
# • Network names, addresses, and port numbers
# • Optional behaviors
# • Security keys, tokens, usernames, passwords
# • Value domains

'''
Application configuration design patterns
'''

# • Global property map: A global object will contain all of the configuration
# parameters. This can be either a map of name:value pairs, or a big
# namespace object of attribute values. This may follow a Singleton design
# pattern to ensure that only one instance exists.

# • Object Construction: Instead of a single object, we'll define a kind of Factory
# or collection of Factories that use the configuration data to build the objects
# of the application. In this case, the configuration information is used once
# when a program is started and never again. The configuration information
# isn't kept around as a global object

# We might have a module named configuration.py. In that file, we can have a
# definition like the following:
# settings= dict()
# Now, the application can use configuration.settings as a global repository for all
# of the application's settings. A function or class can parse the configuration file, loading
# this dictionary with the configuration values that the application will then use.

'''
implementing a configuration hierarchy 
'''
# • The application's installation directory: In effect, these are analogous to base
# class definitions. There are two subchoices here. Smaller applications can be
# installed in Python's library structure; an initialization file too can be installed
# there. Larger applications will often have their own username that owns one
# or more installation directory trees.

# • A system-wide configuration directory: This is often present in /etc. This
# can be transformed into C:\etc on Windows. Alternatives include the value
# of os.environ['WINDIR'] or os.environ['ALLUSERSPROFILE'].

# • The current user's home directory: We can generally use os.path.
# expanduser() to translate ~/ into the user's home directory. For Windows,
# Python will properly use the %HOMEDRIVE% and %HOMEPATH% environment
# variables.

# • The current working directory: The directory is usually known as ./,
# although os.path.curdir is more portable.

# • A file named in the command-line parameters: This is an explicitly named
# file and no further processing should be done to the name.

'''
using py files
'''
# Using Python gives us a number of design considerations. We have two overall
# strategies to use Python as the configuration file:
# • A top-level script: In this case, the configuration file is simply the top-most main program
# • An exec() import: In this case, our configuration file provides parameter values that are collected into module global variables

# We can design a top-level script file that looks like the following code:
from simulator import *
def simulate_SomeStrategy_Flat():
    dealer_rule= Hit17()
    split_rule= NoReSplitAces()
    table= Table( decks=6, limit=50, dealer=dealer_rule, split=split_rule, payout=(3,2) )
    player_rule= SomeStrategy()
    betting_rule= Flat()
    player= Player( play=player_rule, betting=betting_rule, rounds=100, stake=50 )
    simulate( table, player, "p2_c13_simulation3.dat", 100 )
if __name__ == "__main__":
    simulate_SomeStrategy_Flat()
# This shows us our various configuration parameters that are used to create and
# initialize objects. We've simply written the configuration parameters directly into the
# code. We've factored out the processing into a separate function, simulate().


# configuration via class definitions

# The difficulty that we sometimes have with top-level script configuration is the
# lack of handy default values. To provide defaults, we can use ordinary class
# inheritance.
# define Default_App with a default configuration

def make_config( ):
    config= types.SimpleNamespace()
    # set the default values
    config.some_option = default_value
    return config

# The make_config() function would build a default configuration through a
# sequence of assignment statements. An application can then set only the
# interesting override values:
# config= make_config()
# config.some_option = another_value
# simulate_c( config )

'''
using python with exec() for the configuration
'''

with open("config.py") as py_file:
    code= compile(py_file.read(), 'config.py', 'exec')
config= {}
exec( code, globals(), config )
simulate( config['table'], config['player'],
    config['outputfile'], config['samples'])


'''
storing configuration in JSON or YAML 
'''

# config.json
{
    "table":{
        "dealer":"Hit17",
        "split":"NoResplitAces",
        "decks":6,
        "limit":50,
        "payout":[3,2]
    },
    "player":{
        "play":"SomeStrategy",
        "betting":"Flat",
        "rounds":100,
        "stake":50
    },
}

import json 
config = json.load("config.json")

# this allow us to use config['table']['dealer'] to look up the specific class to be used 


