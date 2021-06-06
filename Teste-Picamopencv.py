import numpy as np
import pandas as pd
import cv2 as cv
import imutils
from collections import OrderedDict
from picamera.array import PiRGBArray
from picamera import PiCamera
import picamera
import time
import datetime

#Counting function
def Contagem(x, LineX):
    DistAbs = abs(x - LineX)
    #time.sleep(1) #intervalo entre checagens (debouncing simplificado)

    if DistAbs <= 3:
        return 1
    else:
        return 0

#setting up PiCamera
camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 5
rawCapture = PiRGBArray (camera, size=(320, 240))

contador = 0
lastcount = 0
start = time.time()
d = pd.DataFrame (columns=['timestamp', 'tipo'])

time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    
    cap = frame.array
    
    belt = cap[48:240, 100:220] #Cropping the video
    gray_belt = cv.cvtColor(belt, cv.COLOR_BGR2GRAY)
    _, threshold = cv.threshold(gray_belt, 140, 255, cv.THRESH_BINARY)
    now = time.time() - start #Seconds since it starts
    intervalo = now - lastcount #Checking interval between counted objects in seconds
    
    #Creating counting lane
    LineX = 180
    cv.line(cap, (LineX,30), (LineX,180), (0, 200, 0), 3) #Talvez esse tenha interface grafica
    
    # Display the resulting frame
    cv.imshow('cap', cap)
    cv.imshow('gb', gray_belt)
    cv.imshow('belt', belt)
    
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
