##################################################
# References
##################################################

'''
Copy
'''
# Copies are shallow by default 
# easiest way to copy a list (or any built-in mutable collections) is to use the built-in constructor for the type itself
l1 = [3, [55, 44], (7, 8, 9)]
l2 = list(l1)
l2 == l1 # True 
l2 is l1 # False 

# Using the constructor or [:] produces a shallow copy (i.e., the outermost
# container is duplicated, but the copy is filled with references to the same items held by
# the original container). 


'''
Deep copy
'''
# https://pymotw.com/3/copy/index.html

# Working with shallow copies is not always a problem, but sometimes you need to make deep copies (i.e., duplicates that do not share references of embedded objects). 
# The copy module provides the deepcopy and copy functions that return deep and shallow copies of arbitrary objects

# >>> import copy
# >>> bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
# >>> bus2 = copy.copy(bus1) # shallow copy
# >>> bus3 = copy.deepcopy(bus1) # deep copy
# >>> id(bus1), id(bus2), id(bus3)
# (4301498296, 4301499416, 4301499752)
# >>> bus1.drop('Bill')
# >>> bus2.passengers 
# ['Alice', 'Claire', 'David'] # if bus1 changes, so does bus2
# >>> id(bus1.passengers), id(bus2.passengers), id(bus3.passengers)
# (4302658568, 4302658568, 4302657800)
# >>> bus3.passengers
# ['Alice', 'Bill', 'Claire', 'David']


'''
Function Parameters as References
'''

# Call by sharing means that each formal parameter of the function gets a copy of each reference in the arguments. In other words,
# the parameters inside the function become aliases of the actual arguments

# The result of this scheme is that a function may change any mutable object passed as a
# parameter, but it cannot change the identity of those objects

# example: a function may change any mutable object it receives
def f(a, b):
    a += b
    return a 

a = [1,2]
b = [3,4]
f(a, b)
# >>> a, b
# ([1, 2, 3, 4], [3, 4]) # the list is changed


# Don't use mutable types as parameter defaults 
# The problem is that each default value is evaluated when the function is defined—i.e., usually when the module is loaded—and the
# default values become attributes of the function object. So if a default value is a mutable
# object, and you change it, the change will affect every future call of the function.

# instead use None as default 

def __init__(self, names=None):
    if names is None:
        self.names = []
    else:
        self.names = list(names)

##################################################
#  Weakref
##################################################

'''
weakref module
'''
# https://pymotw.com/3/weakref/index.html

# The weakref module supports weak references to objects. A normal reference increments the reference count on the object and prevents it from being garbage collected. This outcome is not always desirable, especially when a circular reference might be present or when a cache of objects should be deleted when memory is needed. A weak reference is a handle to an object that does not keep it from being cleaned up automatically.

# The presence of references is what keeps an object alive in memory. When the reference count of an object reaches zero, the garbage collector disposes of it. But sometimes it is useful to have a reference to an object that does not keep it around longer than necessary.

# A common use case is a cache
# Weak references are useful in caching applications because you don’t want the cached objects to be kept alive just because they are referenced by the cache.


'''
circular reference
'''

# here parent and child classes have circular reference
# they both contain references to each other

class Parent:
    def __init__(self, *children):
        self.children = list(children)
        for child in self.children:
            child.parent = self

    def __del__(self):
        print(f"Removing {(self.__class__, id(self))}")
    

class Child:
    def __init__(self):
        print(f"Removing {self.__class__, }")


import weakref
class Parent:
    def __init__(self, *children):
        self.children = list(children)
        for child in self.children:
            child.parent = weakref.ref(self)
    
    def __del__(self):
        print(f"Removing {(self.__class__, id(self))}")


'''
Cache
'''

