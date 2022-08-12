# Microcontroller basic libraries
from machine import Pin, PWM

# Testing out importing Libraries
'''
    To make this work as intended, utilize Ampy to manipulate files over your ESP.
    The steps to accomplish that are as follow:
    1. Open command prompt and make sure you are in the same directory as the 'dummy_library.py'
    2. Write the file 'dummy_library.py' onto de ESP using the command:
    ampy -pCOMzz put dummy_library.py
    3. Run this file
'''
from dummy_library import DummyClass

# Setting up parameters
PWM_PIN = 14
dummy = DummyClass()

# Setting up PWM pin. ALWAYS CHECK THE DATASHEET
pwm = PWM(Pin(PWM_PIN))

# Setting up PWM parameters
pwm.freq(dummy.freq)
pwm.duty(dummy.duty_cycle)
