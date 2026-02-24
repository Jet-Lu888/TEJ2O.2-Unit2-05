"""
Created by: Jet Lu
Created on: Feb 2026
This module is a Micro:bit MicroPython program that will tell you the temperature.
"""

from microbit import *

# creating variables
temperature = 0
temperatureKelvin = 0

import time

# reset
display.clear
display.show(Image.HAPPY)
time.sleep(1000)

# temperature will display when A is pressed
while True:
    if button_a.is_pressed():
        temperature = input.temperature()
        temperatureKelvin = round(temperature + 273.15)
        print("The temperature is" + temperatureKelvin + " K")
        time.sleep(1000)
        display.clear  # reset
        display.show(Image.HAPPY)
