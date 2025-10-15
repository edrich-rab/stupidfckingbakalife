#!/usr/bin/python
# button_count.py
# Description: When you press the button, counter goes up
# Author:  Edrich Rabanes

import gpiozero as GPIO

# Pins definitions
btn_pin = GPIO.Button(4)

def button_count():
    counter = 0
    while True:
        if btn_pin.is_pressed():
            counter += 1
            print(counter)

button_count()