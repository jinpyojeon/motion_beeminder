#!/usr/bin/env python

import sys
import cv2
import time 

from PyQt4.QtGui import * 
from PyQt4.QtCore import * 
	
from motion_detection import *

def convert_cv_image(cv_image):
    height, width, byteValue = cv_image.shape
    byteValue = byteValue * width
	
    cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB, cv_image)
    mq_image = QImage(cv_image, width, height, byteValue, QImage.Format_RGB888)
    return mq_image

def main():

	app = QApplication(sys.argv)
	
	image = QImage()


	camera = Capture()
	camera.startCapture()

	image.load(convert_cv_image(camera.current_image))

	label = QLabel()


	label.setPixmap(convertFromImage(image))
	
	# app.resize(500, 300)
	
	
	# self.quit_button = QtGui.QPushButton('Quit', self)
	# self.quit_button.clicked.connect(self.capture.quitCapture)

	label.show()
	# .update()

	sys.exit()

if __name__ == '__main__':
	main()
	
