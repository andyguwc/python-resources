
##################################################
# XML RPC
##################################################

'''
XML-RPC Client
'''
# https://pymotw.com/3/xmlrpc.client/index.html

# The simplest way to connect a client to a server is to instantiate a ServerProxy object, giving it the URI of the server. For example, the demo server runs on port 9000 of localhost.

# xmlrpc_server.py

from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.client import Binary
import datetime


class ExampleService:

    def ping(self):
        """Simple function to respond when called
        to demonstrate connectivity.
        """
        return True

    def now(self):
        """Returns the server current date and time."""
        return datetime.datetime.now()

    def show_type(self, arg):
        """Illustrates how types are passed in and out of
        server methods.

        Accepts one argument of any type.

        Returns a tuple with string representation of the value,
        the name of the type, and the value itself.

        """
        return (str(arg), str(type(arg)), arg)

    def raises_exception(self, msg):
        "Always raises a RuntimeError with the message passed in"
        raise RuntimeError(msg)

    def send_back_binary(self, bin):
        """Accepts single Binary argument, and unpacks and
        repacks it to return it."""
        data = bin.data
        print('send_back_binary({!r})'.format(data))
        response = Binary(data)
        return response


if __name__ == '__main__':
    server = SimpleXMLRPCServer(('localhost', 9000),
                                logRequests=True,
                                allow_none=True)
    server.register_introspection_functions()
    server.register_multicall_functions()

    server.register_instance(ExampleService())

    try:
        print('Use Control-C to exit')
        server.serve_forever()
    except KeyboardInterrupt:
        print('Exiting')


# xmlrpc_ServerProxy.py

import xmlrpc.client

server = xmlrpc.client.ServerProxy('http://localhost:9000', allow_none=False)

print('Ping:', server.ping())


'''
XML_RPC Server
'''
# https://pymotw.com/3/xmlrpc.server/index.html