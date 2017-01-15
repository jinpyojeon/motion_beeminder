#!/usr/bin/env python

# for motion detection
import datetime
import imutils
import time
import cv2

def display_motion(frame):

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

    return frame
