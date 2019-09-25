##################################################
#  Python Package Management with pip
##################################################

# find 
# install
# remove

# sys.path shows modules to import 
#  - list of directories searched for pacakges 
#  - first item: current directory('.')
#  - last item: site packages (third party)

# site.packages: location depends on OS, python version, installation procedure, will be somewhere inside python installation 

# installing pip 
# create, distribute and install packages 
# use pip with virtualenv 

# homebrew installs pip with python 

# unstall packages
# $ pip unstall requests

# list all installed packages 
# $ pip list 

# get info on a specific package 
# $ pip show requests

# search for a package 
# $ pip search query 

# save your project's dependencies in requirements.txt
# $ pip freeze > requirements.txt

# check what's in requirement.txt
#  $ cat requirements.txt

# install all packages listed in requirements.txt
# $ pip install -r requirements.txt





##################################################
#  Isolated Development Environments with Virtualenv
##################################################

# virtual env
# create isolated dependencies 
# good practice to create a virtual env everytime you starts
# don't install python packages globally - always work inside virtualenv


# $ sudo pip install virtualenv 

# make a virtual environments 
# $ mkdir .virtualenvs 
# $ cd .virtualenvs

# create projects with virtualenv myproject 
# $ virtualenv amaze 

# activate . myproject/bin/activate
# $ . amaze/bin/activate

# then should be in the environment and can install dependencies for that environment
# $ pip install pylint

# $ which python
# /Users/tianyougu/.virtualenvs/amaze/bin/python

# $ deactivate


# Virtualenv vs. Projects 
# keep virtual environments separate from your projets 
# projects:
#   - contain source code
#   - under version control 

# to switch projects, use below which switches both the dev environment and the project directory 
# $ workon anotherproject 

# list all current projects
# $ workon 

dev/
  project1/
.virtualenvs/
  project1/

# setting up virtualenv wrapper 
# $ pip install virtualenvwrapper 
# $ nano ~/.profile

# the wrapper knows where the project is and knows the 
# makes new virtual environment variable 
# $ mlvirtualenv 


# project from scratch 
# $ mkproject sample 


##################################################
#  Check Code Quality with Pylint
##################################################

# find common errors 
# follow code style guidelines 

# layout 

# documentation and naming 
# docstrings for all public modules, functions, classes and methods 

# Modules: short, lowercase names 
# Classes: CapitalizedNaming 
# Functions and methods: lowercase_with_underscores
# Constancts: ALL_CAPS
# Non-public names start with underscore 

# using pylint to check the code 
# $ pylint amaze 

# or use the GUI
# $ pylint-gui

# also check code duplication 

# very configurable

# running pylint 
# pylint package_or_module 

# generate a pylint config file
# pylint --generate-rcfile > pylintrc 



##################################################
#  Python Debugger 
##################################################
# interactive use
#  - Examining state of the program
#  - Stepping through execution 

# add below to the code to start interactive debugging function
import pdb
pdb.set_trace()

l # list current line of code 
n # next line of code
s # step into the next level function
h # provide documentation
w # print where we are 
c # continue normal program flow
b # set break point
r # return (out of this level)


##################################################
#  Document with Sphinx
##################################################

# docstrings and standards
# becomes the __doc__ special attribute 
""" """
# for methods specify the return value 

# Sphinx to generate HTML docs
# python documentation generator 
# used to generate official python docs 

# $ mkdir docs && cd docs 
# start sphinx 
# $ sphinx-quickstart
# restructured text 
# configuration stored in conf.py

# autodoc 





