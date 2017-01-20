#!/usr/bin/env python

import sys
import cv2
import time 

from PyQt4.QtGui import * 
from PyQt4.QtCore import * 
    
from motion_detection import *

def main():
    a = QApplication(sys.argv)
    w.setWindowTitle("Motion Detection Beeminder")

    w.resize(500, 300)
    
    capture = Capture()

    self.quit_button = QtGui.QPushButton('Quit', self)
    self.quit_button.clicked.connect(self.capture.quitCapture)

    w.show()

    sys.exit(a.exec_())

if __name__ == '__main__':
    main()
    
