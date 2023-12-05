##################################################
# Socket
##################################################

'''
socket basics
'''
# https://pymotw.com/3/socket/addressing.html
# https://realpython.com/python-sockets/
# # https://github.com/realpython/materials/tree/master/python-sockets-tutorial

# A socket is one endpoint of a communication channel used by programs to pass data back and forth locally or across the Internet. 
# Sockets have two primary properties controlling the way they send data: the address family controls the OSI network layer protocol used and the socket type controls the transport layer protocol.

# The socket type is usually either SOCK_DGRAM for message-oriented datagram transport or SOCK_STREAM for stream-oriented transport. Datagram sockets are most often associated with UDP, the user datagram protocol. They provide unreliable delivery of individual messages. Stream-oriented sockets are associated with TCP, transmission control protocol. They provide byte streams between the client and server, ensuring message delivery or failure notification through timeout management, retransmission, and other features.


import socket
print(socket.gethostname())

# convert name of server to its numerical address

import socket

HOSTS = [
    'apu',
    'www.python.org',
]

for host in HOSTS:
    try:
        print('{}: {}'.format(host, socket.gethostbyname(host)))
    except socket.error as msg:
        print('{}: {}'.format(host, msg))



# Finding service info
# Many applications can run on the same host, listening on a single IP address, but only one socket at a time can use a port at that address. The combination of IP address, protocol, and port number uniquely identify a communication channel and ensure that messages sent through a socket arrive at the correct destination.



'''
getaddrinfo
'''

# getaddrinfo() converts the basic address of a service into a list of tuples with all of the information necessary to make a connection. The contents of each tuple will vary, containing different network families or protocols.

# takes several arguments for filtering the result list
def get_constants(prefix):
    return {
        getattr(socket, n): n
        for n in dir(socket)
        if n.startswith(prefix)
    }

# unpack the response tuple
for response in socket.getaddrinfo('www.python.org', 'http'):
    family, socktype, proto, canonname, sockaddr = response


'''
TCP / IP Client and Server
'''

# https://pymotw.com/3/socket/tcp.html
# Sockets can be configured to act as a server and listen for incoming messages, or connect to other applications as a client. After both ends of a TCP/IP socket are connected, communication is bi-directional.


# server program
import socket
import sys

# create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to the port
server_address = ('localhost', 10000)
socke.bind(server_address)

# listen for incoming connections
sock.listen(1)

while True:
    # establish a connection
    connection, client_address = socket.accept()
    try:
        print('connection from', client_address)
    
    # receive the data in small chuncks and retransmit it
    while True:
        data = connection.recv(16)
        if data:
            # send data back to client
            connection.sendall(data)
        else:
            print('no data from', client_address)
            break
    finally:
        # cleanup the connection
        connection.close()

# client program
# instead of binding to a port and listening, it uses connect() to attach the scoket directly to the remote address
import socket

# create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
sock.connect(server_address)

try:
    # Send data
    message = b'This is the message.  It will be repeated.'
    print('sending {!r}'.format(message))
    sock.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('received {!r}'.format(data))

finally:
    print('closing socket')
    sock.close()

'''
UDP
'''

# The user datagram protocol (UDP) works differently from TCP/IP. Where TCP is a stream oriented protocol, ensuring that all of the data is transmitted in the right order, UDP is a message oriented protocol. UDP does not require a long-lived connection, so setting up a UDP socket is a little simpler. On the other hand, UDP messages must fit within a single datagram (for IPv4, that means they can only hold 65,507 bytes because the 65,535 byte packet also includes header information) and delivery is not guaranteed as it is with TCP.


'''
Sending Binary Data
'''
import binascii
import socket
import struct
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
sock.connect(server_address)

# This client program encodes an integer, a string of two characters, and a floating point value into a sequence of bytes that can be passed to the socket for transmission.

values = (1, b'ab', 2.7)
packer = struct.Struct('I 2s f')
packed_data = packer.pack(*values)

try:
    # Send data
    print('sending {!r}'.format(binascii.hexlify(packed_data)))
    sock.sendall(packed_data)
finally:
    print('closing socket')
    sock.close()

# server uses the same packer to unpack

import binascii
import socket
import struct
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
sock.bind(server_address)
sock.listen(1)

unpacker = struct.Struct('I 2s f')

while True:
    print('\nwaiting for a connection')
    connection, client_address = sock.accept()
    try:
        data = connection.recv(unpacker.size)
        print('received {!r}'.format(binascii.hexlify(data)))

        unpacked_data = unpacker.unpack(data)
        print('unpacked:', unpacked_data)

    finally:
        connection.close()



'''
Non blocking communications and timeouts
'''
# By default, a socket is configured so that sending or receiving data blocks, stopping program execution until the socket is ready. Calls to send() wait for buffer space to be available for the outgoing data, and calls to recv() wait for the other program to send data that can be read. This form of I/O operation is easy to understand, but can lead to inefficient operation and even deadlocks, if both programs end up waiting for the other to send or receive data.




'''
selectors
'''
# The APIs in selectors are event-based, similar to poll() from select. There are several implementations and the module automatically sets the alias DefaultSelector to refer to the most efficient one for the current system configuration.

# A selector object provides methods for specifying what events to look for on a socket, and then lets the caller wait for events in a platform-independent way. Registering interest in an event creates a SelectorKey, which holds the socket, information about the events of interest, and optional application data. The owner of the selector calls its select() method to learn about events. The return value is a sequence of key objects and a bitmask indicating what events have occurred. A program using a selector should repeatedly call select(), then handle the events appropriately.


