#!/usr/bin/env python

# for motion detection
import datetime
import imutils
import time
import cv2

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
        self.capture = cv2.VideoCapture(0)
        self.is_capturing = True

    def startCapture(self):
        capture = self.capture
        
        while(self.is_capturing):
            prev_frame = cv2.cvtColor(capture.read()[1], cv2.COLOR_RGB2GRAY)
            next_frame = cv2.cvtColor(capture.read()[1], cv2.COLOR_RGB2GRAY)

            frameDelta = cv2.absdiff(prev_frame, next_frame)

            text = "Motion Detected"
            cv2.putText(frameDelta, "Room Status:{}".format(text), (10,20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            
            self.current_image = frameDelta

        cv2.destroyAllWindows()

    def quitCapture(self):
        self.is_capturing = False
        cv2.destroyAllWindows()
        capture.release()
        QtCore.QCoreApplication.quit()
