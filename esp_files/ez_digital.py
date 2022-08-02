# Microcontroller basic libraries
from machine import Pin

# Miscellaneous Libraries
import time

# Setting up parameters
RELE_PIN = 12
SLEEP_TIME = 1

# Configuring digital outputs
rele1 = Pin(RELE_PIN, Pin.OUT)

while True:
    rele1.on()
    time.sleep(SLEEP_TIME)
    rele1.off()
    time.sleep(SLEEP_TIME)
