
##################################################
# Nesting Modules with Packages 
##################################################

# We can organize functionality into defined functions. 
# We can combine the defined functions and their related data into a class. 
# We can combine related classes into a module. 
# We can combine related modules into a package.

# A small application may be a single module. 
# A larger application will often be a package.
# As with module design, packages should be designed for reuse. 
# A larger application package should properly include a __main__ module.


'''
packages vs. modules 
'''
# Package vs. Module  
# - packages can contain other modules including other packages
# - packages are generally directories while modules are generally files 
# - package is a directory containing __init__.py

type(urllib) # urllib is a package
type(urllib.request) # request is a normal module 
from urllib import request # the submodule knows it's from the package 


# A file modu.py in the directory pack/ is imported with the statement import pack.modu. 
# The interpreter will look for an __init__.py file in pack and execute all of
# its top-level statements. Then it will look for a file named pack/modu.py and execute
# all of its top-level statements. After these operations, any variable, function, or class
# defined in modu.py is available in the pack.modu namespace.

# It is good practice, to leave an __init__.py empty 
# when the package’s modules and subpackages do not need to share any code


##################################################
# Implementing Packages  
##################################################

# A package is a directory containing __init__.py
# 1. first create root directory (needs to be on python.path)
# 2. then create __init__.py this file can be empty and its own presence suffices this to a package

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
# Importing Modules & Packages
##################################################

'''
locating modules
'''
#  - python checks sys.path (list of directories python searches for modules)
#  - searched in order in import
#  - first match provides module
#  - importError when there is no match 

# '' searches for modules in the current directory
import sys
sys.path.append('not_searched') # add new entry using append method, now modules in this directory can be imported
sys.path.extend(['path1','path2'])

# another way is to use PYTHONPATH environment variable 
# PYTHONPATH is environment variable listing paths added to sys.path
# $ export PYTHONPATH=not_searched

'''
absolute vs. relative imports 
'''
# absolute imports
from reader.reader import Reader

# relative imports
# generally avoid it 
from .reader import Reader # imports which use a relative path to modules in the same package 

'''
__all__ (from modu import *)
'''
# control the behavior: from module import*
# limiting what names to export in a module when people use import *
from pprint import pprint 
pprint(locals())

# add to __init__.py
__all__ = ['bz2_opener', 'gzip_opener'] # list of strings for the names in module

# only the attributes in foo.__all__ will be imported from foo
from foo import *
# if __all__ isn't present in foo, then only public attributes, without _, are imported


'''
nested packages
'''
import very.deep.module as modu # so it's less verbose 


##################################################
# Namespace Pacakges & Executable Packages
##################################################

'''
namespace packages
'''
# i.e. packages split across multiple directories 
# have no __init__.py to avoid complex initialization problems 
# nothing will be executed while being imported

sys.path.extend(['path1','path2'])

# importing namespace packages (pep 420)
# 1. python scans all entries in sys.path
# 2. if a matching directory with __init__.py is found, a normal package is loaded
# 3. if foo.py is found, then it is loaded
# 4. otherwise, all matching directories in sys.path are considered part of the namespace package


'''
executable directories
'''
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
    # __main__.py (optional if want to make this an executable)
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

'''
1. creating a source dist 
'''
# packing with setuptools 
# add setup.py

# you have to manually list every subdirectory that makes up the packages source code. 
# A common mistake is to only list the top-level directory of a
# package and to forget to include package subcomponents. 
# This is why the specification for packages in setup.py includes 
# the list packages=['projectname', 'projectname.utils'].

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

# another example https://github.com/gleitz/howdoi/blob/master/setup.py#L63-L67

from setuptools import setup, find_packages

setup(
    packages=find_packages() # use the 
    entry_points={
        # run the command_line_runner function from howdoi folder's howdoi file
        'console_scripts': [
            'howdoi = howdoi.howdoi:command_line_runner',
        ]
    },
)

# inside the virtual env
# $ python setup.py sdist
# will produce a dist folder 
# This will create a dist sub-directory in your project, and will wrap-up all of your project’s source code files into a distribution file

# upload to PiPy



'''
2. make sure including the dependencies and data 
'''
# distribute as standalone executable

# install dependencies 
# install_requires: 

# include or exclude other pythons
# MANIFEST.in: 
# include *.txt
# recursive-include examples *
# recursive-include Doc *
# When running the sdist command, a file named MANIFEST will be generated which contains a complete list of all files included.

# sample project by Python Packaging Authority 
# https://github.com/pypa/sampleproject

'''
3. register and upload to PyPi
'''

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

'''
personal PyPI
'''

# host a simple HTTP server, running from the directory containing the packages to be installed 
# |--- archive/
#     |--- MyPackage/
#         |--- MyPackage.tar.gz

# $ cd archive
# $ python3 -m SimpleHTTPServer 9000

'''
s3 hosted PyPI
'''
# Another option for a personal PyPI server is to host on Amazon’s Simple Storage Service,
# Amazon S3. You must first have an Amazon Web Service (AWS) account with
# an S3 bucket. Be sure to follow the bucket naming rules—you’ll be allowed to create a
# bucket that breaks the naming rules, but you won’t be able to access it. To use your
# bucket, first create a virtual environment on your own machine and install all of your
# requirements from PyPI or another source. Then install pip2pi:
# $ pip install git+https://github.com/wolever/pip2pi.git
# And follow the pip2pi README file for the pip2tgz and dir2pi commands. Either
# you’ll do:
# $ pip2tgz packages/ YourPackage+
# or these two commands:
# $ pip2tgz packages/ -r requirements.txt
# $ dir2pi packages/
# Now, upload your files. Use a client like Cyberduck to sync the entire packages folder
# to your S3 bucket. Make sure you upload packages/simple/index.html as well as all
# new files and directories.
# By default, when you upload new files to the S3 bucket, they will have user-only permissions.
# If you get HTTP 403 when trying to install a package, make sure you’ve set
# the permissions correctly: use the Amazon web console to set the READ permission of
# the files to EVERYONE. Your team will now be able to install your package with:
# $ pip install \
# --index-url=http://your-s3-bucket/packages/simple/ \
# YourPackage+

'''
version controls for Pip
'''
# Pull code directly from a version control system
# $ pip install git+git://git.myproject.org/MyProject#egg=MyProject
# https://pip.pypa.io/en/stable/reference/pip_install/#vcs-support


'''
freezing the code
'''
# create a standalone executable bundle you can distribute to end user who do not have Python isntalled on their computer


##################################################
# Full Project Examples
##################################################

'''
good examples
'''
# HowDoI
# https://github.com/gleitz/howdoi/blob/master/setup.py
# HowDoI’s setup.py, above the howdoi/ directory, is a good example setup module
# because in addition to normal package installation, it also installs an executable

# Also handles compatibility 

try:
    from urllib.parse import quote as url_quote
except ImportError:
    from urllib import quote as url_quote

try:
    from urllib import getproxies
except ImportError:
    from urllib.request import getproxies

if sys.version < '3':
    import codecs
    def u(x):
        return codecs.unicode_escape_decode(x)[0]
else:
    def u(x):
        return x

# Other examples 
# https://github.com/realpython
# https://www.reddit.com/r/Python/comments/1ls7vq/best_written_projects_on_python_github/
# https://github.com/fogleman/Minecraft
# https://github.com/Pylons/pyramid/tree/master/src/pyramid
# https://github.com/ytdl-org/youtube-dl


'''
pip install
'''
# pip install git+https://github.com/gleitz/howdoi.git#egg=howdoi


##################################################
# Setuptools
##################################################

# https://setuptools.readthedocs.io/en/latest/setuptools.html#installing-setuptools
# example https://github.com/jakubroztocil/httpie

# Basic Use
# For basic use of setuptools, just import things from setuptools instead of the distutils. Here’s a minimal setup script using setuptools:

from setuptools import setup, find_packages
setup(
    name="HelloWorld",
    version="0.1",
    packages=find_packages(),
)

# Dependencies
setup(
    name="Project",
    ...
    install_requires=[
        "enum34;python_version<'3.4'",
        "pywin32 >= 1.0;platform_system=='Windows'"
    ]
)

# Automatic Script Creation
# https://setuptools.readthedocs.io/en/latest/setuptools.html#automatic-script-creation

setup(
    # other arguments here...
    entry_points={
        "console_scripts": [
            "foo = my_package.some_module:main_func",
            "bar = other_module:some_func",
        ],
        "gui_scripts": [
            "baz = my_package_gui:start_func",
        ]
    }
)

# invoke via myproject or python -m myproject

# can be achieved by create a __main__.py file which contains a main() function that takes no arguments, 
# and also a special passage to determine code to run:
# https://chriswarrick.com/blog/2014/09/15/python-apps-the-right-way-entry_points-and-scripts/

import sys

def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    print("This is the main routine.")
    print("It should do something interesting.")

    # Do argument parsing here (eg. with argparse) and anything else
    # you want your project to do.

if __name__ == "__main__":
    main()

# then ajust setup.py accordingly
from setuptools import setup

setup(name='my_project',
      version='0.1.0',
      packages=['my_project'],
      entry_points={
          'console_scripts': [
              'my_project = my_project.__main__:main'
          ]
      },
)



# guide on installation

# latest release
# Current user
pip install --upgrade --user streamlink
# System wide
sudo pip install --upgrade streamlink

# development version (pip)
# Current user
pip install --upgrade --user git+https://github.com/streamlink/streamlink.git
# System wide
sudo pip install --upgrade git+https://github.com/streamlink/streamlink.git

# development version (git)
# Current user
git clone https://github.com/streamlink/streamlink.git
cd streamlink
python setup.py install --user

# System wide
git clone https://github.com/streamlink/streamlink.git
cd streamlink
sudo python setup.py install




# https://streamlink.github.io/install.html#source-code

Virtual environment
Another method of installing Streamlink in a non-system-wide way is using virtualenv, which creates a user owned Python environment instead.

# Create a new environment
virtualenv ~/myenv

# Activate the environment
source ~/myenv/bin/activate

# Install Streamlink in the environment
pip install --upgrade streamlink

# Use Streamlink in the environment
streamlink ...

# Deactivate the environment
deactivate

# Use Streamlink without activating the environment
~/myenv/bin/streamlink ...


##################################################
# Complex Examples
##################################################

# more complex example https://github.com/jakubroztocil/httpie/blob/master/setup.py

# This is purely the result of trial and error.

import sys
import codecs

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

import httpie


class PyTest(TestCommand):
    # `$ python setup.py test' simply installs minimal requirements
    # and runs the tests with no fancy stuff like parallel execution.
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = [
            '--doctest-modules', '--verbose',
            './httpie', './tests'
        ]
        self.test_suite = True

    def run_tests(self):
        import pytest
        sys.exit(pytest.main(self.test_args))


tests_require = [
    # Pytest needs to come last.
    # https://bitbucket.org/pypa/setuptools/issue/196/
    'pytest-httpbin',
    'pytest',
    'mock',
]


install_requires = [
    'requests>=2.22.0',
    'Pygments>=2.5.2',
]


# Conditional dependencies:

# sdist
if 'bdist_wheel' not in sys.argv:
    try:
        # noinspection PyUnresolvedReferences
        import argparse
    except ImportError:
        install_requires.append('argparse>=1.2.1')

    if 'win32' in str(sys.platform).lower():
        # Terminal colors for Windows
        install_requires.append('colorama>=0.2.4')


# bdist_wheel
extras_require = {
    # https://wheel.readthedocs.io/en/latest/#defining-conditional-dependencies
    'python_version == "3.0" or python_version == "3.1"': ['argparse>=1.2.1'],
    ':sys_platform == "win32"': ['colorama>=0.2.4'],
}


def long_description():
    with codecs.open('README.rst', encoding='utf8') as f:
        return f.read()


setup(
    name='httpie',
    version=httpie.__version__,
    description=httpie.__doc__.strip(),
    long_description=long_description(),
    url='https://httpie.org/',
    download_url='https://github.com/jakubroztocil/httpie',
    author=httpie.__author__,
    author_email='jakub@roztocil.co',
    license=httpie.__licence__,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'http = httpie.__main__:main', # the main function of httpie.__main__.py
            'https = httpie.__main__:main',
        ],
    },
    extras_require=extras_require,
    install_requires=install_requires,
    tests_require=tests_require,
    cmdclass={'test': PyTest},
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development',
        'Topic :: System :: Networking',
        'Topic :: Terminals',
        'Topic :: Text Processing',
        'Topic :: Utilities'
    ],
)

