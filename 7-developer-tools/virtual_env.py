
##################################################
# Properly Installing Python
##################################################
# Python that ships with OS X is good for learning not stable for releases
# Need Cpython release 

# First install Homebrew
$ BREW_URI=https://raw.githubusercontent.com/Homebrew/install/master/install
$ ruby -e "$(curl -fsSL ${BREW_URI})"

# Then insert the homebres directory at the top of the PATH environment variable (~/.profile or ~/.bash_profile)
export PATH=/usr/local/bin:/usr/local/sbin:$PATH

# Then isntall Python along with pip and setuptools
$ brew install python3

# Upgrade Pip
$ pip install --upgrade pip


'''
pyenv
'''
# managed multiple python versions 
# https://realpython.com/intro-to-pyenv/
# https://github.com/pyenv/pyenv
# https://opensource.com/article/20/4/pyenv

$ brew install pyenv 

$ echo 'PATH=$(pyenv root)/shims:$PATH' >> ~/.zshrc
# or use pyenv init commands


# System python comes installed on the operating systems 
# $ which python
# /usr/bin/python

# install python version 
$ pyenv install 3.6.8 

$ pyenv install -v 3.7.2

# choose python version
$ pyenv gloabl 3.6.8
$ pyenv versions 

# remove python 
$ ls ~/.pyenv/versions/
$ rm -rf ~/.pyenv/versions/2.7.15



##################################################
# Virtual Env
##################################################

# virtual env
# create isolated dependencies
# it creates a folder containing all the necesary executables to use the packages that a Python project would need
# good practice to create a virtual env everytime you starts
# don't install python packages globally - always work inside virtualenv
# https://realpython.com/python-virtual-environments-a-primer/


'''
virtualenv 
'''
# $ sudo pip3 install virtualenv 
# $ mkdir sample && cd sample
# $ python3 -m virtualenv venv 
# $ python3 -m venv venv (a better approach to use the venv from standar lib)
# $ source venv/bin/activate 
# $ deactivate

# This created the following 
# ├── bin
# │   ├── activate
# │   ├── activate.csh
# │   ├── activate.fish
# │   ├── easy_install
# │   ├── easy_install-3.5
# │   ├── pip
# │   ├── pip3
# │   ├── pip3.5
# │   ├── python -> python3.5
# │   ├── python3 -> python3.5
# │   └── python3.5 -> /Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5
# ├── include
# ├── lib
# │   └── python3.5
# │       └── site-packages
# └── pyvenv.cfg

# bin: files that interact with the virtual environment
# lib: python version along with a site-packages folder where dependencies are installed

# $ echo $PATH
# the virtual environment’s bin directory is now at the beginning of the path
# That means it’s the first directory searched when running an executable on the command line. 
# Thus, the shell uses our virtual environment’s instance of Python instead of the system-wide version.


'''
virtualenvwrapper 
'''
# wrapper around virtualenv which better organizes the virtual environments
# and makes it easier to switch between environments
# downside is the user must acquire these scripts to completely duplicate the environment on another machine

# https://python-guide-kr.readthedocs.io/ko/latest/dev/virtualenvs.html
# https://virtualenvwrapper.readthedocs.io/en/latest/

# setting up virtualenv wrapper 
# $ pip install virtualenvwrapper 

# output the location of virtualenvwrapper.sh
# $ which virtualenvwrapper.sh

# add to the shell's start file (bash looks up ~/.bash_profile then ~/.profile)
# $ nano ~/.bash_profile and add the following

# export WORKON_HOME=$HOME/.envs 
# export PROJECT_HOME=$HOME/dev 
# source /usr/local/bin/virtualenvwrapper.sh

# then reload the startup file 
# $ source ~/.bash_profile
# $ echo $WORKON_HOME
# $ echo $PROJECT_HOME

# project from scratch 
# $ mkproject sample (simplifies creating the directory and then mkvirtualenv sample)
# $ workon sample 

# other commands 
# $ mkvirtualenv
# $ deactivate
# $ rmvirtualenv sample

'''
add a path to virtualenv
'''
# if already using virtualenvwrapper 
# add2virtualenv directory1 directory2 …
# https://stackoverflow.com/questions/10738919/how-do-i-add-a-path-to-pythonpath-in-virtualenv


'''
setting an environment varible in virtualenv
'''
# https://stackoverflow.com/questions/9554087/setting-an-environment-variable-in-virtualenv
# if already using virtualenvwrapper 

# $ workon sample 

# this file is run after activation
# $ cat $VIRTUAL_ENV/bin/postactivate

# add the environment variables to this file 
# export DJANGO_DEBUG=True
# export S3_KEY=mykey
# export S3_SECRET=mysecret

# $ echo $DJANGO_DEBUG

# If you want to keep this configuration in your project directory, simply create a symlink from your project directory to $VIRTUAL_ENV/bin/postactivate.

# $ rm $VIRTUAL_ENV/bin/postactivate
# $ ln -s .env/postactivate $VIRTUAL_ENV/bin/postactivate

# Remember that this wont clean up after itself. When you deactivate the virtualenv, the environment variable will persist. To clean up symmetrically you can add to $VIRTUAL_ENV/bin/predeactivate.

# $ cat $VIRTUAL_ENV/bin/predeactivate
# unset DJANGO_DEBUG

# $ deactivate
# $ echo $DJANGO_DEBUG


# another approach using python-dotenv
# to get environment variables from .env
# https://pybit.es/persistent-environment-variables.html
