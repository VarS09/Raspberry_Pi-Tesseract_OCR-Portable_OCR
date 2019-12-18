import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(27, gpio.IN, pull_up_down=gpio.PUD_DOWN)
gpio.add_event_detect(27, gpio.RISING, bouncetime=200)

#while (True):
#       print('Waiting for button to be clicked')
#       if gpio.event_detected(27):
#               print('Button Clicked !!')
while(True):
        if gpio.event_detected(27):
                print('Button Clicked!!')
                exit(0)

