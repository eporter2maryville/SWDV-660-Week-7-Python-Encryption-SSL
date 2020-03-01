#!/usr/bin/python                               # This is server.py file

import socket                                   # Import socket module

sCA = socket.socket()                           # Create a socket object for the CA
host = socket.gethostname()                     # Get local machine name
port = 9501                                     # Reserve a port for your service.  

sClient = socket.socket()                       # Create a socket object for client
host = socket.gethostname()                     # Get local machine name
port = 9500                                     # Reserve a port for your service.
sClient.bind((host, port))                      # Bind to the port  

sClient.listen(5)                               # Now wait for client connection.
while True:
    c, addr = sClient.accept()                  # Establish connection with client.
    print('Got connection from', addr)
    
    clientMessage = c.recv(1024)
    clientMessageDecoded = clientMessage.decode()       
    if clientMessageDecoded == 'Hello':
        c.send('Hi'.encode())
    else:
        c.send('Goodbye'.encode())

c.close()                                       # Close the connection
