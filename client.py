import socket                           # Import socket module

sCA = socket.socket()                       # Create a socket object
host = socket.gethostname()                 # Get local machine name
port = 9502                                 # Reserve a port for your service.
sCA.connect((host, port))

serverClientSocket = socket.socket()       # Create a socket object
host = socket.gethostname()                 # Get local machine name
port = 9500                                 # Reserve a port for your service.
#serverClientSocket.connect((host, port))

#sCA.connect((host, port))
caServerName = sCA.recv(1024)
caServerNameDecoded = caServerName.decode()
print ('Received Server Name from CA: ',caServerNameDecoded)
sCA.send('Name Received'.encode())
#caPublicKey = sCA.recv(1024)
#caPublicKeyDecoded = caPublicKey.decode()
#print (caPublicKeyDecoded)

serverClientSocket.connect((host, port))
serverName = serverClientSocket.recv(1024)
serverNameDecoded = serverName.decode() #Receive and Decode Server Name
print('Name received from server: ',serverNameDecoded)
if serverNameDecoded == caServerNameDecoded:
    print('Server Name and Name from CA match!')
else:
    print('ERROR: Server name does NOT match name from CA!!! \n GOODBYE!')
sCA.send(serverNameDecoded.encode('utf-8'))

caPublicKey = sCA.recv(1024)
caPublicKeyDecoded = caPublicKey.decode()
print ('Public Key received from CA: ', caPublicKeyDecoded)

#Cipher
sessionCipherKey = 'Session Cipher Key'
cipherkey1 = caPublicKeyDecoded[0]
cipherKey2 = caPublicKeyDecoded[1]
cipherKey3 = caPublicKeyDecoded[2]
cipherKey4 = caPublicKeyDecoded[3]
cipherKey5 = caPublicKeyDecoded[4]
cipherKey6 = caPublicKeyDecoded[5]
cipherList = [cipherkey1, cipherKey2, cipherKey3, sessionCipherKey, cipherKey4, cipherKey5, cipherKey6]
cipherName = ''.join(cipherList)
print('Here is the cipher\'d session key: ', cipherName)
serverClientSocket.send(cipherName.encode('utf-8'))

expectedResponseCipherKey = 'session cipher key acknowledgement'
expectedResponseCipherList = [cipherkey1, cipherKey2, cipherKey3, expectedResponseCipherKey, cipherKey4, cipherKey5, cipherKey6]
expectedResponseCipher = ''.join(expectedResponseCipherList)

print('CLient expected response cipher: ', expectedResponseCipher)

serverCipherResponse = serverClientSocket.recv(1024)
serverCipherResponseDecoded = serverCipherResponse.decode()
print('Server Acknowledgement Cipher received: ',serverCipherResponseDecoded)

if serverCipherResponseDecoded == expectedResponseCipher:
    serverClientSocket.send(b'Hello')                      # Print Positive Response
    #serverClientSocket.sendall(b'Not Hello')              # Print Negative response code used for testing

    serverResponse = serverClientSocket.recv(1024)

    serverResponseDecoded = serverResponse.decode()
    print (serverResponseDecoded)
else:
    print('Server Cipher did not match!!')

sCA.close()                         # Close the socket when done
serverClientSocket.close()                         # Close the socket when done
