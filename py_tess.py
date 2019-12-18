import cv2
import numpy as np
import pytesseract
import matplotlib.pyplot as plt
image='/home/pi/test_tesseract/first_test.jpeg'
img=cv2.imread(image)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
inv_gray_img = cv2.bitwise_not(gray_img)
(thresh, im_bw1) = cv2.threshold(gray_img, 128, 255, cv2.THRESH_BINARY | cv2.TH$
#(thresh, im_bw2) = cv2.threshold(inv_gray_img, 128, 255, cv2.THRESH_BINARY | c$
kernel = np.ones((5,5), np.uint8)
img_dilate = cv2.dilate(im_bw1, kernel, iterations=1)
cv2.imshow('original image',img)
cv2.imshow('image',img_dilate)
cv2.waitKey(0)
cv2.destroyAllWindows()
#img_dilate2 = cv2.dilate(im_bw2, kernel, iterations=1)
#target = pytesseract.image_to_string(img_dilate, lang='eng', config='--psm 10 $
#print(target)
