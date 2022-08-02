# Libraries
import socket

# Setting up parameters
ESP_PORT = 45000
ESP_TIMEOUT = 5

# Getting parameters
ESP_IP = input("ESP IP address: ")

# Setting up a socket
'''
    Normally, in IoT sometimes you have to do low level socket programming. That means, no friendly
    GET or POST requests, but rather raw socket connection.
    Steps:
    1. Set the host's IP and PORT numbers
    2. Create a socket connection
    3. Convert what you need to send to bytes
    4. On the other end, decode what is received in bytes and transform it into the correct information type
'''

while True:
    # Getting some input
    number_to_send = int(input("Enter number: "))
    print("Input received (hex): " + hex(number_to_send))

    print('About to create connection to ESP')

    try:
        # Creating socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Setting up a timeout: if its not possible to connect, we don't want to get stuck
            s.settimeout(ESP_TIMEOUT)

            # Creating connection to the ESP
            s.connect((ESP_IP, ESP_PORT))
            print('Connected to ESP')

            # Sending information
            print("Sending information")

            # Since we want to send a number, the best way is to transform it into hex to its readable for
            # us developers
            s.sendall(number_to_send.to_bytes(4, 'big'))

            # CRUCIAL STEP: Release connection and resources
            s.close()

            print("Information sent")
    except ValueError:
        print("Couldn't convert the input to a number")

    except Exception as e:
        print("An error occurred")

