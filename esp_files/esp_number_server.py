# Network related Libraries
import network, socket

# Setting up parameters
ESP_PORT = 45000
NUMBER_OF_CONNECTIONS = 1
ESP_BUFFER_BYTES = 1024

# Setting up parameters to connect to a local wi fi
ssid = '---'
password = '---'

# Configuring Wi Fi module
station = network.WLAN(network.STA_IF)
station.active(True)

# Attempting to connect to the Access Point
station.connect(ssid, password)

# Attempting connection
print("Attempting to connect to the Wi Fi...")
while not station.isconnected():
    pass
print('Connection successful')

# Once connected, retrieve network information (Host IP, network mask and others)
print(station.ifconfig())

# Create a Server that is set up to be in standby
print("Initializing Server...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Creating Server Socket
s.bind(('', ESP_PORT))  # Setting up port to listen to
s.listen(NUMBER_OF_CONNECTIONS)

print("Awaiting Connections...")

# Code to execute
while True:
    conn, address = s.accept()
    print('Got a connection from %s' % str(address))

    # Reading request by setting up a buffer
    request = conn.recv(ESP_BUFFER_BYTES)

    # Parsing Number Request
    number = int.from_bytes(request, "big")

    # Closing connection to save network resources for both the ESP and the machine
    conn.close()

    # Do some shenanigans here
    print(number)
