# USE TRACKBAR IN MAIN FRAME TO VARY THE PIXEL VALUES
#This program shows 5 thresholding methods but the user can control the right pixel using trackbar.


import cv2
import numpy as np

def nothing(x):
          pass

cap=cv2.VideoCapture(0)

cv2.namedWindow('frame')

cv2.createTrackbar('amplifier','frame',0,255,nothing)


while True:

          value=cv2.getTrackbarPos('amplifier','frame')
          
          
          _,frame=cap.read()
          gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
          _,bin_thresh=cv2.threshold(gray,value,255,cv2.THRESH_BINARY)
          _,bin_thresh_inv=cv2.threshold(gray,value,255,cv2.THRESH_BINARY_INV)
          _,trunc_thresh=cv2.threshold(gray,value,255,cv2.THRESH_TRUNC)
          _,to_zeros_thresh=cv2.threshold(gray,value,255,cv2.THRESH_TOZERO)
          _,mask_thresh=cv2.threshold(gray,value,255,cv2.THRESH_MASK)
          
          
      

          cv2.imshow('frame',frame)
          cv2.imshow('binary thresh',bin_thresh)
          cv2.imshow('binary thresh inverse',bin_thresh_inv)
          cv2.imshow('truncate thresh',trunc_thresh)
          cv2.imshow('to zeros thresh',to_zeros_thresh)
          cv2.imshow('mask thresh',mask_thresh)
          key=cv2.waitKey(1)
          if key==ord('q'):
                    break
                    
cap.release()
cv2.destroyAllWindows()
