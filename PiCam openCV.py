import numpy as np
import pandas as pd
import cv2 as cv
from picamera.array import PiRGBArray
from picamera import PiCamera
import picamera
import time


camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 5
rawCapture = PiRGBArray (camera, size=(320, 240))

time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    
    cap = frame.array
    
    # Display the resulting frame
    cv.imshow('frame', cap)
    
    
    rawCapture.truncate(0)
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv.destroyAllWindows()
