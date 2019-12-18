import RPi.GPIO as gpio
from time import sleep
from picamera import PiCamera
import cv2
import numpy as np
import pytesseract

gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(27, gpio.IN, pull_up_down=gpio.PUD_DOWN)
gpio.add_event_detect(27, gpio.RISING, bouncetime=200)
kernel = np.ones((5,5), np.uint8)

while(True):
        if gpio.event_detected(27):
                camera = PiCamera()
                camera.start_preview()
                sleep(5)
                camera.capture('/home/pi/test_tesseract/first_test.jpeg')
                camera.stop_preview
                print('Image Captured')
                image='/home/pi/test_tesseract/first_test.jpeg'
                img=cv2.imread(image)
                gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                inv_gray_img = cv2.bitwise_not(gray_img)
                (thresh, im_bw1) = cv2.threshold(gray_img, 128, 255, cv2.THRESH$
                img_dilate = cv2.dilate(im_bw1, kernel, iterations=1)
                target = pytesseract.image_to_string(img_dilate, lang='eng', co$
                print(target)
                exit(0)