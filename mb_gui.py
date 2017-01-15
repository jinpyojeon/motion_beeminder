#!/usr/bin/env python

import sys
import cv2
import time 

from PyQt4.QtGui import * 
from PyQt4.QtCore import * 
    
from motion_detection import *

a = QApplication(sys.argv)
camera = cv2.VideoCapture(0)
time.sleep(0.25)

w = QWidget()
w.resize(500, 300)
w.setWindowTitle("Motion Detection Beeminder")

w.show()

while True:
    (grabbed, frame) = camera.read()
    
    if not grabbed:
        break

    frame = display_motion(frame)

camera.release()
sys.exit(a.exec_())


