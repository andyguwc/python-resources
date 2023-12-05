#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'
PORT = 65432

# socket.SOCK_STREAM uses TCP protocol
# The arguments passed to socket() specify the address family and socket type. AF_INET is the Internet address family for IPv4. SOCK_STREAM is the socket type for TCP, the protocol that will be used to transport our messages in the network.

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # bind() is used to associate the socket with a specific network interface and port number:

    s.bind((HOST, PORT))

    # Continuing with the server example, listen() enables a server to accept() connections. It makes it a “listening” socket:

    s.listen()

    # accept() blocks and waits for an incoming connection. When a client connects, it returns a new socket object representing the connection and a tuple holding the address of the client.

    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        # After getting the client socket object conn from accept(), an infinite while loop is used to loop over blocking calls to conn.recv(). This reads whatever data the client sends and echoes it back using conn.sendall().

        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)


