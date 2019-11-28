##################################################
# Nesting Modules with Packages 
##################################################

# We have a deep hierarchy of packaging techniques. We can simply organize the
# functionality into defined functions. We can combine the defined functions and
# their related data into a class. We can combine related classes into a module. We can
# combine related modules into a package.

# A small application may be a single module. A larger application will often be a
# package. As with module design, packages should be designed for reuse. A larger
# application package should properly include a __main__ module.


# import modules 
# import x
# from x import y
# from x import y as z 

# main block to distinguish module execution from module import 
# only executes main when we know we are running the module as a script 
# and run this when it's imported 
import sys 

def main():
    """The main function of the program."""
    return 0

if __name__ == '__main__':
    sys.exit(main())




# Package vs. Module  
# can contain other modules including other packages
type(urllib) # urllib is a package
type(urllib.request) # request is a normal module 

# packages are generally directories (urllib.__path__) 
# modules are generally files 

from urllib import request # the submodule knows it's from the package 


# Locating Modules 
#  - python checks sys.path (list of directories python searches for modules)
#  - searched in order in import
#  - first match provides module
#  - importError when there is no match 

# '' searches for modules in the current directory
import sys
sys.path.append('not_searched') # add new entry using append method, now modules in this directory can be imported
sys.path.extend(['path1','path2'])

# another way is to use PYTHONPATH environment variable 
# $ export PYTHONPATH=not_searched



##################################################
# Implementing Packages  
##################################################

# A package is a directory containing __init__.py
# 1. first create root directory (needs to be on python.path)
# 2. then create __init__.py this file can be empty and its own presence suffices this to a package


# Sub package 
path_entry/ # sys.path

- my_package/ # package root
    - __init__.py # package init file. Executed when the package is imported
    - compressed/
        __init__.py # sub packages which are implemented with init

import demo_reader.compressed_reader.gzipped # import subpackages 

# absolute imports
from reader.reader import Reader

# relative imports
# generally avoid it 
from .reader import Reader # imports which use a relative path to modules in the same package 

# control the behavior: from module import*
# limiting what names to export in a module when people use import *
from pprint import pprint 
pprint(locals())
__all__ = ['bz2_opener', 'gzip_opener'] # list of strings for the names in module

# only the attributes in foo.__all__ will be imported from foo
from foo import *
# if __all__ isn't present in foo, then only public attributes, without _, are imported

# A package is a collection of modules in a folder. The name of the package is the name of the folder. All we need to
# do to tell Python that a folder is a package is place a (normally empty) file in the folder
# named __init__.py. If we forget this file, we won't be able to import modules from that folder.

parent_directory/
    main.py
    ecommerce/
        __init__.py
        database.py
        products.py
        payments/
            __init__.py
            square.py
            stripe.py


##################################################
# Namespace Pacakges & Executable Packages
##################################################

# i.e. packages split across multiple directories 
# have no __init__.py to avoid complex initialization problems 

sys.path.extend(['path1','path2'])

# importing namespace packages (pep 420)
# 1. python scans all entries in sys.path
# 2. if a matching directory with __init__.py is found, a normal package is loaded
# 3. if foo.py is found, then it is loaded
# 4. otherwise, all matching directories in sys.path are considered part of the namespace package


# executable directories
# directories containing an entry point for python execution
# when __main__.py is executed, the parent directory is automatically added to sys.path
# $ python multi-reader-program
- multi-reader-program 
    - demo_reader
        - compressed 
            - __init__.py 
            - bzipped.py
        - util 
            - __init__.py
            - write.py
        - __init__.py 
        - multireader.py
    __main__.py

# similarly if using __main__.py in packages, then python will execute with python -m package 
# __init__ vs. __main__ 
# __init__.py can execute any code it likes on import but only a package with __main__.py can be executed

# executable zip file
# zip file containing an etry point for execution 


##################################################
# Layout / Project Structure 
##################################################

# recommended project structure
project_name/ # project root - not the package 
    README.rst # overview documentation
    docs/ # project documentation 
    src/ # actual package/production code; the /src directory ensures tat you develop against installed versions of your packages
        package_name/
            __init__.py 
            more_source.py 
            subpackage1/
                __init__.py 
    tests/ # all tests for the project; separating tests from production code 
        test_code.py 
    setup.py 

# Implementing extensions / plugins with namespace packages 
# core package designates subpackages as extension points 
# scan subpackages at runtime to discover plugins

# first create the various plugin packages
- core/
- bz2-plugin/
- gz-plugin/
# then add those to the python path 
# $ export PYTHONPATH=core:bz2-plugin:gz-plugin

# or can define extension or opener 


##################################################
# Package Distribution 
##################################################
# distribution packages
#  - archive of package contents
#  - easy to install 
#  - various formats (zip, tarball, etc.)

# source and built distributions
# built package 
#  - placed directly into installation directory 
#  - build results are included in the package 
#  - can be platform specific 
# recommended format wheel 

# source package
#  - contains everything needed to build the package
#  - cannot be placed directly into installation directory 
#  - necessary to build the package before installing it 

# publish to python package index 
# use wheel to create distribution xx.whl
# use twine to upload 

# create new virtual environment 


##################################################
# Packaging & Distributing Code 
##################################################

# 1. creating a source dist 
# packing with setuptools 
# add setup.py

# you have to manually list every subdirectory that makes up the packages source code. A common mistake is to only list the top-level directory of a
# package and to forget to include package subcomponents. This is why the specification
# for packages in setup.py includes the list packages=['projectname', 'projectname.utils'].

from setuptools import setup 

setup(name='amaze',
      version='0.1',
      description='maze operation',
      author='aa',
      author_email='a@a.com',
      packages=['amaze','amaze.demo'],    
      entry_points={
          'console_scripts': [
              'amaze_demo=amaze.demo.tkdemo:main',
          ],
      },
)

# inside the virtual env
# will produce a dist folder 
# $ python setup.py sdist

# upload to PiPy

# 2. make sure including the dependencies and data 
# distribute as standalone executable

# install dependencies 
# install_requires: 

# include or exclude other pythons
# MANIFEST.in: 
# include *.txt
# recursive-include examples *
# recursive-include Doc *

# sample project by Python Packaging Authority 
# https://github.com/pypa/sampleproject

# 3. register and upload to PyPi
# $ python setup.py register 
# $ python setup.py sdist upload 

# distributing executables 
# Automatic script creatoin 
# Py2exe (windows executable)
# Py2app (for MacOS)
# PyInstaller (support multiple)

# example structure 
projectname/
    README.txt 
    Doc/
        documentation.txt 
    projectname/
        __init__.py
        foo.py
        bar.py
        utils/
            __init__.py 
            spam.py 
            grok.py 
    examples/
        helloworld.py 


