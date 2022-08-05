# Network Libraries
import socket

# Setting up parameters
SERVER_PORT = 46000
NUMBER_OF_CONNECTIONS = 1
BUFFER_BYTES = 1024

# Create Socket
s = socket.socket()
s.bind(('', SERVER_PORT))
s.listen(NUMBER_OF_CONNECTIONS)

print("Socket created")

# Obtaining network IP
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
print("IP Address: {}".format(local_ip))

while True:
    print("Awaiting Connections...")
    conn, address = s.accept()
    print('Got a connection from %s' % str(address))

    # Reading request by setting up a buffer
    request = conn.recv(BUFFER_BYTES)

    # Parsing values Request
    values = request.decode("utf-8").split("-")

    # Closing connection to save network resources for both the ESP and the machine
    conn.close()

    # Do some shenanigans here
    print(values)