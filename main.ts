/* Copyright (c) 2020 MTHS All rights reserved
 *
 * Created by: Jet Lu
 * Created on: Feb 2026
 * This program will display the temperature in kelvin.
*/
let temperature: number
let temperatureKelvin: number

//reset
basic.clearScreen()
basic.showIcon(IconNames.Happy)

// Temperature (in kelvin) will display when A is pressed
input.onButtonPressed(Button.A, function () {
    temperature = input.temperature()
    temperatureKelvin = Math.round(temperature + 273.15)
    basic.showString("The temperature is" + temperatureKelvin + " K")
    pause(1000)
    basic.clearScreen()
    basic.showIcon(IconNames.Happy)
})