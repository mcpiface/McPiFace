import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(26,GPIO.IN, pull_up_down=GPIO.PUD_UP)

def button_pressed_callback(self):
    print 'Button Pressed!'

    # Change to Green LED to indicate the button was pressed
    print "GREEN LED on"
    GPIO.output(20,GPIO.HIGH)
    GPIO.output(21,GPIO.LOW)
    time.sleep(2)
    # And go back to red.
    print "RED LED on"
    GPIO.output(20,GPIO.LOW)
    GPIO.output(21,GPIO.HIGH)


# Add event handling for the button
GPIO.add_event_detect(26, GPIO.FALLING)
GPIO.add_event_callback(26, button_pressed_callback)

# Red LED on whilst we wait for the button to be pressed.
print "RED LED on"
GPIO.output(21,GPIO.HIGH)
GPIO.output(20,GPIO.LOW)

# Sleep whilst we wait for the button to be pressed.
time.sleep(60)	



