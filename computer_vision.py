import cv2
import numpy as np
try:
        from PIL import Image
except ImportError:
        import Image
import pytesseract

path='/home/pi/Downloads/test.jpeg'
img=cv2.imread(path)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow('Original Image',img)
#cv2.imshow('Gray Scale Image', gray_img)
inv_gray_img = cv2.bitwise_not(gray_img)
#cv2.imshow('Inverted gray scale image',inv_gray_img)
(thresh, im_bw1) = cv2.threshold(gray_img, 128, 255, cv2.THRESH_BINARY | cv2.TH$
(thresh, im_bw2) = cv2.threshold(inv_gray_img, 128, 255, cv2.THRESH_BINARY | cv$
#cv2.imshow('Binarized gs', im_bw1)
#cv2.imshow('Binarized inv_gs', im_bw2)
kernel = np.ones((5,5), np.uint8)
img_dilate = cv2.dilate(im_bw1, kernel, iterations=1)
img_dilate2 = cv2.dilate(im_bw2, kernel, iterations=1)
cv2.imshow('Dilate img1', img_dilate)
cv2.imshow('Dilate img2', img_dilate2)
print(pytesseract.image_to_string(Image.open(img_dilate)))
print(pytesseract.image_to_string(Image.open(img_dilate2)))
cv2.waitKey(0)
cv2.destroyAllWindows()