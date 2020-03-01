import socket                   # Import socket module

s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 9500                     # Reserve a port for your service.

s.connect((host, port))
s.send(b'Hello')                # Print Positive Response
#s.sendall(b'Not Hello')        # Print Negative response code used for testing
serverResponse = s.recv(1024)
serverResponseDecoded = serverResponse.decode()
print (serverResponseDecoded)



s.close()                       # Close the socket when done
