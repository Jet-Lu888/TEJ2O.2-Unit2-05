"""
Created by: Jet Lu
Created on: Feb 2026
This module is a Micro:bit MicroPython program that will tell you the temperature.
"""

from microbit import *

# creating variables
temperatureCelsius = 0
temperatureKelvin = 0

# reset
display.clear()
display.show(Image.HAPPY)
sleep(1000)


# temperature will display when A is pressed
while True:
    if button_a.is_pressed():
        temperatureCelsius = temperature()
        temperatureKelvin = round(temperatureCelsius + 273.15)
        display.scroll("The temperature is" + str(temperatureKelvin) + " K")
        sleep(1000)
        display.clear()  # reset
        display.show(Image.HAPPY)
