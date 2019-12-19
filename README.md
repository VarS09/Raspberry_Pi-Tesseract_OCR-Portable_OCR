# Portable Optical Character Recognizer (POCR) using Raspberry Pi & Tesseract OCR
In this project we build a hand-held device that is capable of performing optical character recognition on limited text (labels, number plates, etc).
The picture clicked by the hand-held device undergoes on-device image processing and OCR in sequential manner. The generated result can then be pushed to a cloud, shown on a screen or sent as a message depending 
on the requirement. The device's functionality can be enhanced and the aforementioned required functionality can be added by tweaking and augmenting the generalized code present in the repository.
## Hardware Requirements
* Raspberry Pi (any model is fine [zero w, 2, 3 etc])
* Compatible Raspberry Pi Camera
* Push button
## Software Requirements
* Raspbian OS
* [OpenCV](https://opencv.org/)
* [Tesseract OCR](https://opensource.google/projects/tesseract)
## Getting Started
Firstly we need to setup Raspbian OS on Raspberry Pi, this can be done via a [headless setup](https://www.tomshardware.com/reviews/raspberry-pi-headless-setup-how-to,6028.html)
or the traditional HDMI method. We then need to install OpenCV python library and Tesseract C++ engine and its python wrapper [pytesseract](https://pypi.org/project/pytesseract/).
The dependencies for these softwares to run should be first installed. The commands to install the dependencies are as follows:

`sudo apt-get install libatlas-base-dev`

`sudo apt-get install libcblas-dev`

`sudo apt-get install libhdf5-dev`

`sudo apt-get install libhdf5-serial-dev`

`sudo apt-get install libjasper-dev`

`sudo apt-get install libqtgui4`

`sudo apt-get install libqt4-test`

Then install OpenCV using the standard command: `pip install opencv-python` (pip command should be used according to the python version)

Now we need to install the Tesseract OCR engine using the command: `sudo apt-get install tesseract-ocr`. If successfully installed, we can check its version using the command `tesseract -v`

To make use of the installed Tesseract OCR engine in our code, we need to install its python wrapper using the command: `pip install pytesseract`

## Interfacing the Raspberry pi camera
This is simple enough, we just have to insert the camera module ribbon cable into the raspberry pi's camera module port. We can check whether it has been detected or not using the command: `vcgencmd get_camera`

## Running the scripts
The repository holds scripts for each individual step through which we can get an understanding of the process of on-device image processing and OCR. The consolidated code is also present and this can be configured to run whenever we click the push button. This would initiate the process by taking a picture and then give out the text result extracted/recognized from the image captured.
The process the captured image undergoes is as follows:

### Original Image

![Oriinal Image](https://user-images.githubusercontent.com/34755328/71176231-68ac2000-228f-11ea-87d0-6b7d8deea933.jpg)

The original image is then processed to improve the efficiency of the OCR performed by the Tesseract OCR engine.

### Grayscale Image

![Grayscale image](https://user-images.githubusercontent.com/34755328/71176342-a9a43480-228f-11ea-9649-cff98ff306ba.PNG)

The grayscale image is then binarized with each pixel either at a value of 1(255 intensity) or 0.

### Binarized Image

![Binarized image](https://user-images.githubusercontent.com/34755328/71176739-86c65000-2290-11ea-846f-a93d8ed6b6f6.PNG)

The binarized image is then dilated to reinforce the exiting data and as an attempt to recover the data lost during binarizing.

### Dilated Image

![Dilated Image](https://user-images.githubusercontent.com/34755328/71177386-e7a25800-2291-11ea-87e3-7fa889db7c6e.PNG)

The OCR is then performed on this image.

The efficiency of the portable hand-held OCR is just feasible and its accuracy can be further improved by enhancing both the hardware and software.

