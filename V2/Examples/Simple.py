import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(26,GPIO.IN, pull_up_down=GPIO.PUD_UP)

print "Button Input:"
print GPIO.input(26)

print "GREEN LED on"
GPIO.output(20,GPIO.HIGH)
time.sleep(2)

print "RED LED on"
GPIO.output(21,GPIO.HIGH)
time.sleep(2)

print "LEDs off"
GPIO.output(20,GPIO.LOW)
GPIO.output(21,GPIO.LOW)

print "Button Input:"
print GPIO.input(26)
