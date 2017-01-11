#!/usr/bin/env python

# for Gui
import sys
from PyQt4.QtGui import * 
from PyQt4.QtCore import * 

# for motion detection
import datetime
import imutils
import time
import cv2

class QProgBr(QProgressBar):
    value = 0

    @pyqtSlot()
    def increaseValue(progressBar):
        progressBar.setValue(progressBar.value)
        if ()
        progressBar.value = progressBar.value + 1


a = QApplication(sys.argv)
camera = cv2.VideoCapture(0)
time.sleep(0.25)

w = QWidget()
w.resize(500, 300)
w.setWindowTitle("Motion Detection Beeminder")

bar = QProgBar(w)
bar.resize(320, 50)
bar.setValue(720)

timer = QTimer()
bar.connect(timer.SIGNAL("timeout()")).bar.SLOT("increaseValue()"))
timer.start(5000)

w.show()


while True:
    (grabbed, frame) = camera.read()
    frame = detect_motion(frame)


camera.release()
sys.exit(a.exec_())


