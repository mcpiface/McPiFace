import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(26,GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Red LED on whilst we wait for the button to be pressed.
print "RED LED on"
GPIO.output(21,GPIO.HIGH)
GPIO.output(20,GPIO.LOW)
time.sleep(2)

# The button defaults to high
# and goes low when pressed.
while GPIO.input(26):
	time.sleep(1)	

print "Button Pressed!"

# Change to Green LED to indicate the button was pressed
print "GREEN LED on"
GPIO.output(20,GPIO.HIGH)
GPIO.output(21,GPIO.LOW)