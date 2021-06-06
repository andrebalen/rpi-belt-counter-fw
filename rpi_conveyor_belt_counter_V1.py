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
start = time.time()  #Set a starting time 
d = pd.DataFrame (columns=['timestamp', 'tipo']) #Creating a DataFrame 'd' to save timestamps of counted objects

time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    
    cap = frame.array
    
    #Cutting the video and setting threshold
    _, video = cap.read() 
    belt = video[359:648, 587:1080]
    gray_belt = cv.cvtColor(belt, cv.COLOR_BGR2GRAY)
    _, threshold = cv.threshold(gray_belt, 140, 255, cv.THRESH_BINARY)
    now = time.time() - start #Seconds since it starts
    intervalo = now - lastcount #Checking interval between counted objects in seconds
    
    #Creating counting lane
    LineX = 700
    cv.line(frame, (LineX,300), (LineX,600), (0, 200, 0), 3) #Talvez esse tenha interface grafica
    
    
    #Detecting objects 
    contours, hierarchy = cv.findContours(threshold, cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE) 
    for cnt in contours:
        #Calculating the area of rectangle and spliting
        area = cv.contourArea(cnt)
        #Counting one object
        if 8500> area > 5000:
            #Creating the bounding rectangle
            (f, l, w, h) = cv.boundingRect(cnt)
            x = 587 + f
            y = 359 + l
            cv.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 3)
            cv.putText(frame, str(area), (x, y), 1, 1, (0, 255, 0))
            
        
            #Central Point
            CenterX = int((x+x+w)/2)
            CenterY = int((y+y+h)/2)
            CentralPoint = (CenterX, CenterY)
            cv.circle(frame, CentralPoint, 1, (0, 255, 0), 5)
            
            #Counting
            
            if (Contagem(CenterX,LineX) and (intervalo > 0.5)): # Applying counting fuction and Debouncing count
                lastcount = now #reset lastcount
                contador += 1 
                hora = time.time() #Saving timestamp
                datahora = time.gmtime(hora)
                d = d.append ({'timestamp' : datahora}, ignore_index=True) #input timestamp on dataset
        
        #Counting objects together
        elif area > 8500:
            #Creating the bounding rectangle
            #Criando o contorno (sacos agrupados)
            (f, l, w, h) = cv.boundingRect(cnt)
            t = int(w/2)
            x = 587 + f
            y = 359 + l
            rec1 = cv.rectangle(frame, (x,y), (x+t, y+h), (255,0,0), 3)
            rec2 = cv.rectangle(frame, (x+t,y), (x+t+t, y+h), (0,255,0), 3)
            cv.putText(frame, str(area), (x, y), 1, 1, (0, 255, 0))
           
            #Central Point
            CenterX1 = int((x-t+x+w)/2)
            CenterY1 = int((y+y+h)/2)
            CentralPoint1 = (CenterX1, CenterY1)
            CenterX2 = int((x+t+x+w)/2)
            CenterY2 = int((y+y+h)/2)
            CentralPoint2 = (CenterX2, CenterY2)
            cv.circle(frame, CentralPoint1, 1, (0, 255, 0), 5)
            cv.circle(frame, CentralPoint2, 1, (0, 255, 0), 5)
                
            #Counting
            if (Contagem(CenterX1,LineX) and (intervalo > 0.5)): # tentando reduzir o numero de contagens repetidas 
                contador += 1
                lastcount = now
                hora = time.time()
                datahora = time.gmtime(hora)
                d = d.append ({'timestamp' : datahora}, ignore_index=True)
                
            if (Contagem(CenterX2,LineX) and (intervalo > 0.5)): # tentando reduzir o numero de contagens repetidas
                contador += 1
                lastcount = now
                hora = time.time()
                datahora = time.gmtime(hora)
                d = d.append ({'timestamp' : datahora}, ignore_index=True)
      
    
    #Mostrando Videos
    # Display the resulting frame
    cv.putText(frame, "Contagem: {}".format(str(contador)), (10, 40), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 50, 1), 2)
    cv.putText(frame, "Tempo: {}".format(str(now)), (10, 80), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 50, 1), 2)
    cv.putText(frame, "Intervalo: {}".format(str(intervalo)), (10, 120), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 50, 1), 2)
    cv.putText(frame, "timestamp: {}".format(str(lastcount)), (10, 150), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 50, 1), 2)
    cv.imshow("video",video)
    cv.imshow("belt", belt)
    cv.imshow("belt gray", gray_belt)
    cv.imshow("threshold", threshold)
    
    
    
    
    
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
