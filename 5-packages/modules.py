##################################################
#  Modules
##################################################

# A module is a file containing Python definitions and statements intended for use in other Python programs. 
# There are many Python modules that come with Python as part of the standard library. 
# Providing additional functionality through modules allows you to only use the functionality you need when you need it, and it keeps your code cleaner.

# Namespace
# Functions imported as part of a module live in their own namespace. 
# A namespace is simply a space within which all names are distinct from each other. The same name can be reused in different namespaces but two objects can’t have the same name within a single namespace.

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


# virual environments
pip install virtualenv

virtualenv <env_name>
virtualenv --python=python2.7 

# executables
pip install pyinstaller
pyinstall main.py # which creates the exe file 
cd ./dist/main 
./main.exe

pyinstaller --onefile ./main.py



# documenting using docstrings
def test_func(a):
    """Fetch a list.
    Args:
        url: the url 
    Returns: a list 
    """

help(test_func)


