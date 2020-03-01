import socket                                   # Import socket module

serverCASocket = socket.socket()                       # Create a socket object for the server
host = socket.gethostname()                     # Get local machine name
port = 9501                                     # Reserve a port for your service.
serverCASocket.bind((host, port))                      # Bind to the port
serverCASocket.listen(5)                               # Now wait for server connection.

sClient = socket.socket()                       # Create a socket object for the client
host = socket.gethostname()                     # Get local machine name
port = 9502                                     # Reserve a port for your service.
sClient.bind((host, port))                      # Bind to the port
sClient.listen(5)                               # Now wait for client connection.


while True:
    s, addr = serverCASocket.accept()                  # Establish connection with server.
    print('CA got server connection from', addr)
    
    serverNameMessage = s.recv(1024)
    serverNameDecoded = serverNameMessage.decode()
    print('Received Name of Server: ', serverNameDecoded)
    s.send('Name Received'.encode())
    serverPublicKey = s.recv(1024)
    serverPublicKeyDecoded = serverPublicKey.decode()
    print('Recieved Public Key: ', serverPublicKeyDecoded)
    
    c, addr = sClient.accept()                  # Establish connection with client.
    print('CA got client connection from', addr)

    c.send(serverNameMessage)
    clientResponse = c.recv(1024)
    clientResponseDecoded = clientResponse.decode()
    if clientResponseDecoded == 'Name Received':
        print('confirmation of Name received from client')         #send Server Name and Public Key to CA
    else:
        c.send('Goodbye'.encode())
    clientServerName = c.recv(1024)
    clientServerNameDecoded = clientServerName.decode()
    if serverNameDecoded == clientServerNameDecoded:
        c.send(serverPublicKeyDecoded.encode('utf-8'))         #send Server Name and Public Key to CA
    else:
        c.send('ERROR: Server Names Do Not Match!!!'.encode())
    

serverCASocket.close()                         # Close the socket when done

'''
while True:
    c, addr = sClient.accept()                  # Establish connection with client.
    print('Got connection from', addr)

    c.send(serverNameMessage)
    c.send(serverPublicKey)
    
    #clientMessage = c.recv(1024)
    #clientMessageDecoded = clientMessage.decode()
'''
sClient.close()                                 # Close the socket when done
