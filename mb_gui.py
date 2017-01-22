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
	w = QImage()
	w.setWindowTitle("Motion Detection Beeminder")

	w.resize(500, 300)
	
	camera = Capture()
	camera.startCapture()

	convert_cv_image(camera.current_image)

	self.quit_button = QtGui.QPushButton('Quit', self)
	self.quit_button.clicked.connect(self.capture.quitCapture)

	w.show()
	w.update()

	sys.exit(a.exec_())

if __name__ == '__main__':
	main()
	
