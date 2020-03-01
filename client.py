import socket                           # Import socket module

sServer = socket.socket()               # Create a socket object
host = socket.gethostname()             # Get local machine name
port = 9500                             # Reserve a port for your service.

sCA = socket.socket()                   # Create a socket object
host = socket.gethostname()             # Get local machine name
port = 9502                             # Reserve a port for your service.

sServer.connect((host, port))
sServer.send(b'Hello')                  # Print Positive Response
#sServer.sendall(b'Not Hello')          # Print Negative response code used for testing
serverResponse = sServer.recv(1024)
serverResponseDecoded = serverResponse.decode()
print (serverResponseDecoded)



sServer.close()                         # Close the socket when done
