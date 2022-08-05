# Microcontroller basic libraries
from machine import Pin, ADC

# Miscellaneous Libraries
from time import sleep

# Setting up parameters
PHOTO_PIN = 2
SAMPLE_TIME = 1

# Configuring ADC pin
photoresistor = ADC(Pin(PHOTO_PIN))

# Configuring ADC Pin properties
photoresistor.atten(ADC.ATTN_11DB)  # Sensibility of the meassure
'''
Options for different Full Range Voltage:

ADC.ATTN_0DB: Voltage 1.2V
ADC.ATTN_2_5DB: Voltage 1.5V
ADC.ATTN_6DB: Voltage 2.0V
ADC.ATTN_11DB: Voltage 3.3V
'''

photoresistor.width(ADC.WIDTH_12BIT)

'''
An ESP ADC has a default resolution of 12 bits. There is a way to change it:

ADC.width(bit), where bit can be either of these options:

ADC.WIDTH_9BIT: range 0 to 511
ADC.WIDTH_10BIT: range 0 to 1023
ADC.WIDTH_11BIT: range 0 to 2047
ADC.WIDTH_12BIT: range 0 to 4095
'''

while True:
    photo_value = photoresistor.read()
    print(photo_value)
    sleep(SAMPLE_TIME)
