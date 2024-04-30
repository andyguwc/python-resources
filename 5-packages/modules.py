##################################################
#  Modules
##################################################

'''
module concepts
'''

# A module is a file containing Python definitions and statements intended for use in other Python programs. 
# There are many Python modules that come with Python as part of the standard library. 
# Providing additional functionality through modules allows you to only use the functionality you need when you need it, and it keeps your code cleaner.

# Namespace
# Functions imported as part of a module live in their own namespace. 
# A namespace is simply a space within which all names are distinct from each other. The same name can be reused in different namespaces but two objects can’t have the same name within a single namespace.
# globals() tell us all the objects in this namespace

# Type of modules
# - Pure library module: These are meant to be imported. They contain definitions of classes, functions, and perhaps some assignment statements to create a few global variables.
#   - Whole module: Some modules are designed to be imported as a whole, creating a module namespace that contains all of the items
#   - Item collection: Some modules are designed to have individual items imported instead of creating a module object
# - Main script modules: meant to be executed from the command line. Includ statements to do real work 
# - Conditional script modules: can be imported and run from the command line 

# Module vs Class
# The similarities between modules and classes mean that choosing between them
# is a design decision with trade-offs and alternatives. In most cases, the need for an
# instance of is the deciding factor. A module's singleton feature means that we'll use a
# module (or package) to contain class and function definitions that are expanded just
# once even if imported multiple times.

# loaded into memory and get referenced in the globals() dict

import math
mod_math = globals()['math'] # this returns the math module
mod_math.sqrt(2)
type(math) # module
id(math) # returns a memory address, import again and returns the same address

# sys modules
import sys
sys.modules # type(sys.modules) 
# this tells us whhere the module is located in memory
sys.modules["math"] # where the .py code is located <module 'math' from '/Users/tianyougu/.pyenv/versions/3.8.5/lib/python3.8/lib-dynload/math.cpython-38-darwin.so'>
id(sys.modules["math"])

f = math.__dict__["sqrt"]
f(2)

# ModuleType
import types
isinstance(math, types.ModuleType)

# Importing Modules
import random
# import random as rd

prob = random.random()
print(prob)

diceThrow = random.randrange(1,7) # lower bound included, but upper bound excluded
print(diceThrow)

# To avoid running executable statements in a script when it's imported as a module in another script, include these lines in an if __name__ == "__main__" block. 
# Or alternatively, include them in a function called main() and call this in the if main block.

if __name__ == "__main__":
    print("Testing function")

# third party libraries
# $ pip install package_name

'''
how importing works
'''
# python does import at run time
# different form compiled languagtes like C where modules are compiled and linked at compile time
# python uses a complex system to find and load modules.


# python path
sys.prefix
sys.exec_prefix

# python look for imports
# when importing a module, python search for the module in the paths containes in sys.path
sys.path

# ['', '/Users/tianyougu/.pyenv/versions/3.8.5/lib/python38.zip', '/Users/tianyougu/.pyenv/versions/3.8.5/lib/python3.8', '/Users/tianyougu/.pyenv/versions/3.8.5/lib/python3.8/lib-dynload', '/Users/tianyougu/.pyenv/versions/3.8.5/lib/python3.8/site-packages']

# how python imports a module from file
# - checks the sys.modules cache to see if the module has already been imported - if so it simply uses the reference in there, otherwise
# - creates a new module object(types.ModuleType)
# - loads the source code from file
# - adds an entry to sys.modules with name as key and the newly created module
# - compiles and executes the source code
# the compile function compiles source (text) into a code object
# the exec function is used to execute a code object. Optionally specify the dictionary used to store global symbols

# module finders
# BuiltinImporter finds built-ins
# FrozenImporter finds frozen modules
# PathFinder finds path-based modules

sys.meta_path # finds and loaders [<class '_frozen_importlib.BuiltinImporter'>, <class '_frozen_importlib.FrozenImporter'>, <class '_frozen_importlib_external.PathFinder'>]

# PathFinder
# finds file-based modules based on sys.path and package __path__
# the file must exist in a path specified in sys.path or in a path specified by package.__path__

'''
importlib
'''

# import programatically
# brings the code, compiles, executes it and puts the reference in sys module
mod_name = 'math'

import importlib

math = importlib.import_module(mod_name)
"math" in sys.modules # True

math2 = importlib.import_module(mod_name)
# id(math2) == id(math)
# 'math2' in globals()

# importer is basically finder and loader
import fractions
fractions.__spec__
# ModuleSpec(name='fractions', loader=<_frozen_importlib_external.SourceFileLoader object at 0x101c6c8e0>, origin='/Users/tianyougu/.pyenv/versions/3.8.5/lib/python3.8/fractions.py')
sys.meta_path # finds and loaders [<class '_frozen_importlib.BuiltinImporter'>, <class '_frozen_importlib.FrozenImporter'>, <class '_frozen_importlib_external.PathFinder'>]

# module properties
type(math) # module
math.__spec__
math.__name__ 
math.__package__ # packages
fractions.__file__ # file name, for standar libraries



import importlib.util
importlib.util.find_spec('enum') # ModuleSpec(name='enum', loader=<_frozen_importlib_external.SourceFileLoader object at 0x101d938e0>, origin='/Users/tianyougu/.pyenv/versions/3.8.5/lib/python3.8/enum.py')

# ext_module_path
sys.path.append(ext_module_path)
# can also import from zip files
sys.path.append("./common.zip")
import common

# then can find the spec of the module
importlib.util.find_spec('module2')



'''
import
'''
# in every case below, the math module was loaded into memory and referenced in sys.modules

# module1.py file
import math

# if math is not in sys.modules, load it and insert reference
# add symbol math to module1's global namespace referencing the same object

import math as r_math
# first check if math in sys.modules, if not load it and reference it
# add symbol r_math to module1's global namepsace referencing the same object

# import a function
from math import sqrt
# first check if math in sys.modules, if not load it and reference it
# add symbol sqrt to module1's global namespace referencing the math.sqrt function

from math import *
# add "all" symbols defined in math to module1's global namespace
# what "all" means can be defined by the module being imported

# avoid import * which can override names
from cmath import *
from math import * # sqrt overrides the sqrt from the previous module

# efficiency
# from an importing standpoint, needs to import the whole module regardless
# no such thing as partial import

'''
hierachical package of modules
'''
# to make a package structure, organize code and make sure every directory defines an __init__.py file 

# graphics/
#     __init__.py
#     primitive/
#         __init__.py
#         line.py
#         fill.py
#     formats/
#         __init__.py
#         png.py
#         jpg.py 

#  can perform the following import statements
import graphics.primitive.line
from graphics.primitive import line
import graphics.formats.jpg as jpg


# The purpose of the __init__.py files is to include optional initialization code
# that runs as different levels of a package are encountered. For example, if you have the
# statement import graphics, the file graphics/__init__.py will be imported and form
# the contents of the graphics namespace. 

# For an import such as import graphics.formats.jpg, the files graphics/__init__.py and graphics/formats/__init__.py will both be
# imported prior to the final import of the graphics/formats/jpg.py file.

# automaticlaly load submodules 
# graphics/formats/__init__.py
from . import jpg
from . import png 

# a user just needs to import a single graphics.formats instead of
# a separate import for graphics.formats.jpg and graphics.formats.png.

'''
controlling import of everything 
'''
# control the symbols exported from a module or package when using from module import *

# somemodule.py

def spam():
    pass 

def grok():
    pass 

blah = 42

# only import spam and grok 
# if __all__ is defined, then only the names explicitly listed will be exported.
__all__ = ['spam', 'grok']


'''
importing package submodules using relative names 
'''
mypackage/
    __init__.py
    A/
        __init__.py
        spam.py
        grok.py
    B/
        __init__.py
        bar.py

# mypackage/A/spam.py
from . import grok

# mypackage/A/spam.py
from ..B import bar

# relative imports only work for modules located inside a proper package
# won't work if parts of a package are exeucted directly as a script
python3 mypackage/A/spam.py # Relative imports fail
python3 -m mypackage.A.spam # Relative imports work


'''
splitting a module into multiple files 
'''

# mymodule.py

class A: 
    def spam(self):
        print('A.spam')

class B(A):
    def bar(self):
        print('B.bar')

# to split mymodule.py into two files, start by replacing mymodule.py with a directory called mymodule 
mymodule/
    __init__.py
    a.py
    b.py 

# a.py 
class A:
    def spam(self):
        print('A.spam')

# b.py 
from .a import A 

class B(A):
    def bar(self):
        print('B.bar')

# __init__.py
# finally in the __init__.py file, glue the two files together
from .a import A 
from .b import B 

import mymodule
a = mymodule.A()
a.spam()
b = mymodule.B()
b.bar()


'''
namespace package
'''
# special package designed for merging different directories of code together under a common namespace 
# this allows parts of a framework to be broken up into separately installed downloads 

# suppose you have different directories of code 
foo-package/
    spam/
        blah.py
bar-package/
    spam/
        grok.py 

# In these directories, the name spam is being used as a common namespace. Observe that
# there is no __init__.py file in either directory.

# if you add both foo-package and bar-package to the Python module path and try some imports:
import sys
sys.path.extend(['foo-package', 'bar-package'])
import spam.blah
import spam.grok


'''
reload modules
'''
import test

import importlib
importlib.reload(test) # reload an object
# the memory address stays the same, the content is mutated in memory


'''
adding directories to sys.path
'''
# if it's not located in a directory listed in sys.pth you can't import 
# to add new directories to sys.pth, first can add through the use of PYTHONPATH environment variable
# bash % env PYTHONPATH=/some/dir:/other/dir python3

# The second approach is to create a .pth file that lists the directories like this:
# # myapplication.pth
# /some/dir
# /other/dir
# This .pth file needs to be placed into one of Python’s site-packages directories, which are
# typically located at /usr/local/lib/python3.3/site-packages or ~/.local/lib/python3.3/sitepackages.
# On interpreter startup, the directories listed in the .pth file will be added to
# sys.path as long as they exist on the filesystem.


'''
make a file executable  
'''
# For some larger applications, we'll have one or more files that we mark as
# executable with the OS chmod +x command. We can put these executable
# files into Python's scripts directory with our setup.py installation. We run
# these applications with some_script.py at the command line.

# We mark the script executable with chmod +x some_script.py. Then, we include a
#! shebang line:
#!/usr/bin/env python3.3
# This line will direct the OS to use the named program to execute the script file. In this
# case, we used the /usr/bin/env program to locate the python3.3 program to run
# the script. The Python3.3 program will be given the script file as its input.
# Once the script file is marked executable—and includes the #! line—we can use
# some_script.py at the command line to run the script.


'''
__main__ 
'''

# when execute a program, the entry point module is renamed by python as __main__

if __name__ == "__main__":
    print("Module was executed directly")

# __main__.py file

# directory with the __main__.py can be executed

# can also exeucte a zip file
# python -m zilfile -c my-app __main__.py timing.py
# python my-app 




'''
locals() and globals()
'''
# The functions dir(), globals(), and locals() help with quick namespace introspection:
# - dir(object) returns a list of attributes that are accessible via the object
# - globals() returns a dictionary of the attributes currently in the global namespace, along with their values.
# - locals() returns a dictionary of the attributes in the current local namespace (e.g., within a function), along with their values.


# to avoid function to be called during module import 
# all module level code is executed immediately while imported
class Database:
    pass 

database = None

def initialize_database():
    global database
    database = Database()


