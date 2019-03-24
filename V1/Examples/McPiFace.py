#!/usr/bin/python

# This example shows how to use the McPiFace front panel
# to show a Pi temperature indicator (red/green -> hot/cold)
# and to use the button to shutdown the Pi.

# To install into rc.local and run in the background use:
# $ sudo su
# echo "~pi/McPiFace/V1/Examples/McPiFace.py &" >> /etc/rc.local

# Note: Check your rc.local file to ensure the exit 0 line is after the above McPiFace.py launcher
# Give appropriate permissions
# chmod +x /home/pi/McPiFace/V1/Examples/McPiFace.py
#
# If a library / module not globally installed try:
# sudo -H -u pi /usr/bin/python3 /home/pi/McPiFace/V1/Examples/McPiFace.py


import RPi.GPIO as GPIO
import time
import os

print 'Starting McPiFace front panel monitor'

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GreenLedGpio = 20
RedLedGpio = 21
ButtonGpio = 26

# Warning temperature - when the LED goes red.
# Raspbian set to 80C to show the temperature warning.
pi_temperature_warning = 80
keep_running = True

# These are our GPIO 
GPIO.setup(GreenLedGpio,GPIO.OUT)
GPIO.setup(RedLedGpio,GPIO.OUT)
GPIO.setup(ButtonGpio,GPIO.IN, pull_up_down=GPIO.PUD_UP)

def button_pressed_callback(self):
    print 'Button Pressed! Shutting down. BYE!'
    GPIO.output(GreenLedGpio,GPIO.LOW)
    GPIO.output(RedLedGpio,GPIO.LOW)
    os.system('sudo shutdown now') # shutdown
    #os.system('sudo shutdown -r now') # reboot
    keep_running = False

def read_pi_temperature():
    temperature = os.popen("vcgencmd measure_temp").readline()
    temperature = temperature.replace("temp=","")
    temperature = temperature.replace("'C","")
    return float(temperature)

def check_pi_temperature():
    #print 'Checking Pi Temperature'
    temperature = read_pi_temperature()
    #print 'Pi Temperature {}'.format(temperature)
    if temperature > pi_temperature_warning:
        GPIO.output(RedLedGpio,GPIO.HIGH)
        GPIO.output(GreenLedGpio,GPIO.LOW)
    else:
        GPIO.output(RedLedGpio,GPIO.LOW)
        GPIO.output(GreenLedGpio,GPIO.HIGH)

# Both LEDs on when starting up
GPIO.output(RedLedGpio,GPIO.HIGH)
GPIO.output(GreenLedGpio,GPIO.HIGH)
time.sleep(1)	

# Add event handling for the button
GPIO.add_event_detect(ButtonGpio, GPIO.FALLING)
GPIO.add_event_callback(ButtonGpio, button_pressed_callback)

# Loop forever monitoring the Pi.
while keep_running:
    check_pi_temperature()
    # Delay for a second between checks.
    time.sleep(1)	

# Clean up and exit when keep_running is reset.
GPIO.cleanup()