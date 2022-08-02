# Microcontroller basic libraries
from machine import Pin, PWM

# Testing out importing Libraries
from dummy_library import DummyClass

# Setting up parameters
PWM_PIN = 14
dummy = DummyClass()

# Setting up PWM pin. ALWAYS CHECK THE DATASHEET
pwm = PWM(Pin(PWM_PIN))

# Setting up PWM parameters
pwm.freq(dummy.freq)
pwm.duty(dummy.duty_cycle)
