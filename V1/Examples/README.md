# Example Python Scripts

The scripts in this folder are examples of how you might configure or use the LEDs and button on the McPiFace with a Raspberry Pi.


## Raspberry Pi Setup

The examples assume you've got python development environment installed on your Pi. Please follow http://raspberry.io/projects/view/reading-and-writing-from-gpio-ports-from-python/ if not.

## Connections

The samples assume the front panel connector is wired as follows: 

Black: Pin 39 GND
Red: Pin 40 (BCM 21)
Green: Pin 38 (BCM 20)
Blue (or Yellow): Pin 37 (BCM 26)

See https://pinout.xyz/ for Raspberry Pi header pinout.


## Simple.py

This example reads the button input, lights the green then red LEDs, switches off the LEDs and reads the button a second time.

## ButtonCallback.py

Demonstrates using a callback function to handle the button

## WaitForButton

Demonstrates reading the button status.


## McPiFace.py

This is the main script to run for the McPiFace LED/buttons. 

It will set the LEDs to red/green based on the Pi's temperature. Going red at 80C. Change:

pi_temperature_warning = 80

to a different value to change the LED indication.


Pressing the button will cause the Pi to shutdown. Swap the comment # over to switch between shutdown and reboot.

os.system('sudo shutdown now') # shutdown
#os.system('sudo shutdown -r now') # reboot



## Other examples:

### On Off switch from The Mag Pi Magazine 

Note the switch is wired to GPIO 21, not 26 as used by McPiFace, so you'll need to change the code.

https://www.raspberrypi.org/magpi/off-switch-raspberry-pi/