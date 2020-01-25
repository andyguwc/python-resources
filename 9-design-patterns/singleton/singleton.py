##################################################
#  Singleton
##################################################

# The basic idea behind the singleton pattern is to allow exactly one instance of a
# certain object to exist. Typically, this object is a sort of manager class

# In most programming environments, singletons are enforced by making the
# constructor private (so no one can create additional instances of it), and then providing
# a static method to retrieve the single instance. This method creates a new instance the
# first time it is called, and then returns that same instance each time it is called again.

'''
structure
'''
# ensure class has only one instance
# control access to limited resource 



'''
singleton implementation 
'''

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

# can also let another class inherit the Singleton class 

'''
metaclass implementation 
'''
# metaclass controls the building of classes 

class Singleton(type):
    # contains mapping between class and instances
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance 
        return cls._instances[cls]

# inherit Singleton as the metaclass 
class Logger(metaclass=Singleton):
    pass 

