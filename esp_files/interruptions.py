# Microcontroller basic libraries
from machine import Pin

# Miscellaneous libraries
from time import sleep

# Setting up parameters
button_inter = Pin(25, Pin.IN)
counter = 0


# Create Interruption function handler
def interruption_handler(pin):
    print("Interruption triggered!")
    global counter
    counter += 1


# Defining how the interruption is triggered: Either IRQ_RISING or IRQ_FALLING
# Also, don't forget to pass the function handler
button_inter.irq(trigger=Pin.IRQ_RISING, handler=interruption_handler)

# Do stuff
while True:
    print("Doing stuff... Also counter is at " + str(counter))
    sleep(1)
