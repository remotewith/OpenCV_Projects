#contours are the boundary of an object to make them on the object we detect the edges and draw lines
#we here use basic thresholding on a gray frame


import cv2
import numpy as np

cap=cv2.VideoCapture(0)


while True:
          _,frame=cap.read()
          gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
          _,mask=cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
          

          contour,_=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
          #this would return 3 values first and last is not needed and this gives contours around the white obj
          #print(contours)
          cv2.drawContours(frame,contour,-1,(255,255,0),2)
          #-1 draws all the contours then comes color and thickness
          
         
          cv2.imshow('frame',frame)
          cv2.imshow('mask',mask)
          key=cv2.waitKey(1)
          if key==27:
                    break
                    
cap.release()
cv2.destroyAllWindows()
