#!/usr/bin/python                               # This is server.py file

import socket                                   # Import socket module

serverName = 'serverBot2000'                      # Server Name for CA
publicKey = 'pyServ'                              # Server Public Key

sessionCipherKey = 'Session Cipher Key'
cipherkey1 = publicKey[0]
cipherKey2 = publicKey[1]
cipherKey3 = publicKey[2]
cipherKey4 = publicKey[3]
cipherKey5 = publicKey[4]
cipherKey6 = publicKey[5]
cipherList = [cipherkey1, cipherKey2, cipherKey3, sessionCipherKey, cipherKey4, cipherKey5, cipherKey6]
serverCipherName = ''.join(cipherList)
responseCipherKey = 'session cipher key acknowledgement'
responseCipherList = [cipherkey1, cipherKey2, cipherKey3, responseCipherKey, cipherKey4, cipherKey5, cipherKey6]
responseCipher = ''.join(responseCipherList)

sCA = socket.socket()                           # Create a socket object for the CA
host = socket.gethostname()                     # Get local machine name
port = 9501                                     # Reserve a port for your service.
sCA.connect((host, port))   

sClient = socket.socket()                       # Create a socket object for client
host = socket.gethostname()                     # Get local machine name
port = 9500                                     # Reserve a port for your service.
sClient.bind((host, port))                      # Bind to the port 

#sCA.connect((host, port))
sCA.send(serverName.encode('utf-8'))
caResponse = sCA.recv(1024)
caResponseDecoded = caResponse.decode()
if caResponseDecoded == 'Name Received':
    sCA.send(publicKey.encode('utf-8'))         #send Server Name and Public Key to CA
else:
    sCA.send('Goodbye'.encode())

sCA.close()                                       # Close the connection

sClient.listen(5)                               # Now wait for client connection.
while True:
    c, addr = sClient.accept()                  # Establish connection with client.
    print('Server got connection from Client:', addr)

    c.send(serverName.encode('utf-8'))
    
    clientCipherMessage = c.recv(1024)
    clientCipherMessageDecoded = clientCipherMessage.decode()
    if clientCipherMessageDecoded == serverCipherName:
        print('Ciphers Match on server!')
        print('Sending Acknowledgment Cipher: ', responseCipher)
        c.send(responseCipher.encode('utf-8'))
    else:
        print('Ciphers DO NOT MATCH!! GOODBYE!!')
        break

    clientMessage = c.recv(1024)
    clientMessageDecoded = clientMessage.decode()       
    if clientMessageDecoded == 'Hello':
        c.send('Hi'.encode())
    else:
        c.send('Goodbye'.encode())

c.close()                                       # Close the connection

