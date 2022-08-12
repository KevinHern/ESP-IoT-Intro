# Microcontroller basic libraries
from machine import Pin, ADC

# Network Libraries
import socket, network

# Miscellaneous Libraries
from time import sleep

# Setting up parameters
ANALOG_PIN = 2
DIGITAL_PIN = 25
SAMPLE_TIME = 1

SERVER_IP = "---"
SERVER_PORT = 46000
ESP_TIMEOUT = 5

ssid = '---'
password = '---'

# Configuring ADC pin
analog_pin = ADC(Pin(ANALOG_PIN))
analog_pin.atten(ADC.ATTN_11DB)
analog_pin.width(ADC.WIDTH_12BIT)

# Configuring Digital pin
digital_pin = Pin(DIGITAL_PIN, Pin.IN)

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

while True:
    print("Measuring...")
    # Measure sensors of interest
    analog_value = 2 # analog_pin.read()
    digital_value = digital_pin.value()

    # Accumulate values and use a separator
    values_to_send = str(digital_value) + "-" + str(analog_value)

    try:
        # Creating socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Setting up a timeout: if its not possible to connect, we don't want to get stuck
        s.settimeout(ESP_TIMEOUT)
        
        # Creating connection to the ESP
        s.connect((SERVER_IP, SERVER_PORT))
        
        # Since we want to send text, we have to encode the text into bytes
        s.sendall(bytes(values_to_send, 'utf-8'))
        
        # CRUCIAL STEP: Release connection and resources
        s.close()

    except Exception as e:
        print(e)

        
    sleep(SAMPLE_TIME)
