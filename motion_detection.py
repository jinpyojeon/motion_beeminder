#!/usr/bin/env python

# for motion detection
import datetime
import imutils
import time
import cv2

import cv
 
from PyQt4 import QtCore

class Motion():

    def __init__(self):
        self.motion_duration = 0
        self.last_detected = time.time()
    
    def update_duration(self, time):
        if self.last_detected < time.time() - 10:
            self.motion_duration +=  time.time() - self.last_detected
            self.last_detected = time.time()
    
    def reset_duration(self):
        self.last_detecte = time.time()
        self.motion_duration = 0


class Capture():
    def __init__(self):
        self.c = cv2.VideoCapture(0)

    def startCapture(self):
        self.capturing = True
        cap = self.c
        while(self.capturing):
            ret, frame = cap.read()
            frame = imutils.resize(frame, width=500)
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                gray = cv2.GaussianBlur(gray, (21, 21), 0)
                frameDelta = cv2.absdiff(frame, gray)
                thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
                thresh = cv2.dilate(thresh, None, iterations=2)
                (cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                for c in cnts:
                    if cv.contourArea(c) < 2500: # Minimum pixels for motion detection
                        continue
                    (x, y, w, h) = cv2.boundingRect(c)
                    cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    text = "Motion Detected"
                if text: 
                    cv2.putText(frame, "Room Status:{}".format(text), (10,20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            cv2.imshow("Capture", frame)

        cv2.destroyAllWindows()

    def quitCapture(self):
        self.capturing = False
        cap = self.c
        cv2.destroyAllWindows()
        cap.release()
        QtCore.QCoreApplication.quit()
