##################################################
#  Decorator Pattern
##################################################

'''
structure
'''

# The decorator pattern allows us to "wrap" an object that provides core functionality with other objects that alter this functionality.
# Any object that uses the decorated object will interact with it in exactly the same way as if it were undecorated (that is, the interface of the decorated object is identical to that of the core object).
# There are two primary uses of the decorator pattern:
# - Enhancing the response of a component as it sends data to a second component
# - Supporting multiple optional behaviors

# Here, Core and all the decorators implement a specific Interface. The decorators
# maintain a reference to another instance of that Interface via composition. When
# called, the decorator does some added processing before or after calling its wrapped
# interface. The wrapped object may be another decorator, or the core functionality.
# While multiple decorators may wrap each other, the object in the "center" of all
# those decorators provides the core functionality.

# Faced with a choice between decorators and inheritance
# only use decorators if we need to modify the object dynamically 
# Also known as the wrapper pattern 

'''
decorator example - add log functionality
'''

import socket
def respond(client):
    response = input("Enter a value: ")
    client.send(bytes(response, 'utf8'))
    client.close()

# create decorators to customize the socket behavior without having to extend or modify the socket itself
class LogSocket:
    def __init__(self, socket):
        self.socket = socket
    
    def send(self, data):
        print("Sending {0} to {1}".format(
            data, self.socket.getpeername()[0]))
        self.socket.send(data)

    def close(self):
        self.socket.close()

# this class decorates a socket object and presents the send and close interface to client sockets 
# a better decorator would also implement (all of the remaining socket methods)

# alternatives
#  - monkey patching
#  - multi inheritance
#  - function decorators 

# usage
# respond(LogSocket(client))

'''
decorator example - add gzip functionality 
'''
# another decorator
import gzip 
from io import BytestIO

class GzipSocket:
    def __init__(self, socket):
        self.socket = socket
    
    def send(self, data):
        buf = BytesIO()
        zipfile = gzip.GzipFile(fileobj=buf, mode="w")
        zipfile.write(data)
        zipfile.close()
        self.socket.send(buf.getvalue())
    
    def close(self):
        self.socket.close()
    
# now we can write code that dynamically switches between the decorators when responding 
client, addr = server.accpet()
if log_send:
    client = LoggingSocket(client)
if client.getpeername()[0] in compress_hosts:
    client = GzipSocket(client)
respond(client)


'''
example - car dealership with models and many kinds of options
'''
# abstract base class 
class AbsCar(metaclass=ABCMeta):
    @abstractproperty
    def description(self):
        pass 
    
    @abstractproperty
    def cost(self):
        pass 

# economy car concrete class 
class Economy(AbsCar):
    @property 
    def description(self):
        return 'Economy'
    
    @property 
    def cost(self):
        return 1200

# abstract decorator 
class AbsDecorator(AbsCar):
    def __init__(self, car):
        self._car = car 
    
    @property 
    def car(self):
        return self._car 

# concrete decorator 

class V6(AbsDecorator):
    @property 
    def description(self):
        return self.car.description + ', V6'
    
    @property 
    def cost(self):
        return self.car.cost + 1200 


