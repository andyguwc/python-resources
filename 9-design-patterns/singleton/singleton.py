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
            cls._singleton = super(OneOnly, cls)
            __new__(cls, *args, **kwargs)
        return cls._singleton
# by overriding __new__, we first check if our singleton if our singleton instance has been created; if not, we create
# it using a super call. Thus, whenever we call the constructor on OneOnly, we always
# get the exact same instance
o1 = OneOnly()
o2 = OneOnly()
o1 == o2 

# can also let another class inherit the Singleton class 
class Singleton(object):
    _instances = {} # {cls: instance}
    def __new__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            instance = super().__new__(cls)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Logger(Singleton):
    log_file = None

    def __init__(self, path):
        if self.log_file is None:
            self.log_file = open(path, mode='w')
    
    def write_log(self, record):
        self.log_file.write(record)

    def close_log(self):
        self.log_file.close()
        self.log_file = None


class OneOnly(object):
    client = None

    @classmethod
    def create_client(cls, *args, **kwargs):
        return ElasticSearch(
            **settings.ELASTIC_CLIENT_KWARGS
        )

    def __new__(cls, *args, **kwargs):
        if cls.client is None:
            cls.client = cls.create_client()
        instance = super().__new__(cls)
        return instance

'''
example using metaclass - logging subsystem
'''
# only one instance to write
# metaclass controls the building of classes 

class MonoState(object):
    _state = {}

    # no matter how many instance you create
    # they all share the same state
    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls)
        self.__dict__ = cls._state
        return self


class Logger(MonoState):
    log_file = None

    def __init__(self, path):
        if self.log_file is None:
            self.log_file = open(path, mode='w')
    
    def write_log(self, log_record):
        now = str(datetime.datetime.now())
        record = '%s: %s\n' % (now, log_record)
        self.log_file.write(record)
    
    def close_log(self):
        self.log_file.close()
        self.log_file = None

