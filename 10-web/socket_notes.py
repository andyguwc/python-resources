##################################################
# Socket
##################################################

'''
socket basics
'''
# https://pymotw.com/3/socket/addressing.html

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


def get_constants(prefix):
    return {
        getattr(socket, n) : next
        for n in dir(socket)
    }


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

# Sockets can be configured to act as a server and listen for incoming messages, or connect to other applications as a client. After both ends of a TCP/IP socket are connected, communication is bi-directional.

# create a TCP/IP socket

import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to the port
server_address = ('localhost', 10000)
socke.bind(server_address)

# listen for incoming connections
sock.listen(1)

while True:
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


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
