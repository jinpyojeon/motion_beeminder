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

camera = cv2.VideoCapture(0)
time.sleep(0.25)

a = QApplication(sys.argv)

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

firstFrame = None
while True:
        (grabbed, frame) = camera.read()

        if not grabbed:
            break

        frame = imutils.resize(frame, width=500)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        if firstFrame is None:
            firstFrame = gray
            continue

        frameDelta = cv2.absdiff(firstFrame, gray)
        thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]

        thresh = cv2.dilate(thresh, None, iterations=2)
        (cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for c in cnts:
            (x, y, w, h) = cv2.boundingRect(c)
            cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            text = "Motion Detected"
        

        sys.exit(a.exec_())
