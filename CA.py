import socket                                   # Import socket module

sServer = socket.socket()                       # Create a socket object for the server
host = socket.gethostname()                     # Get local machine name
port = 9501                                     # Reserve a port for your service.
sServer.bind((host, port))                      # Bind to the port

sClient = socket.socket()                       # Create a socket object for the client
host = socket.gethostname()                     # Get local machine name
port = 9502                                     # Reserve a port for your service.
sServer.bind((host, port))                      # Bind to the port
