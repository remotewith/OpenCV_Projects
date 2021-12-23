#This Program can find HSV value of any object that we want
#We here use Trackbar so all the 6 values of HSV can be varied by user and it can find the most appropriate combination for it's object



import cv2
import numpy as np

def nothing(x):
          pass

cap=cv2.VideoCapture(0)

cv2.namedWindow('mask_hsv')

cv2.createTrackbar('Lower_H','mask_hsv',0,179,nothing)
cv2.createTrackbar('Lower_S','mask_hsv',0,255,nothing)
cv2.createTrackbar('Lower_V','mask_hsv',0,255,nothing)
cv2.createTrackbar('Upper_H','mask_hsv',179,179,nothing)
cv2.createTrackbar('Upper_S','mask_hsv',255,255,nothing)
cv2.createTrackbar('Upper_V','mask_hsv',255,255,nothing)


while True:
          
          _,frame=cap.read()
          hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
          
          L_H=cv2.getTrackbarPos('Lower_H','mask_hsv')
          L_S=cv2.getTrackbarPos('Lower_S','mask_hsv')
          L_V=cv2.getTrackbarPos('Lower_V','mask_hsv')
          U_H=cv2.getTrackbarPos('Upper_H','mask_hsv')
          U_S=cv2.getTrackbarPos('Upper_S','mask_hsv')
          U_V=cv2.getTrackbarPos('Upper_V','mask_hsv')

          
          
          lower=np.array([L_H,L_S,L_V])
          upper=np.array([U_H,U_S,U_V])

          mask=cv2.inRange(hsv,lower,upper)

          cv2.imshow('frame',hsv)
          cv2.imshow('mask_hsv',mask)
          key=cv2.waitKey(1)
          if key==ord('q'):
                    break
                    
cap.release()
cv2.destroyAllWindows()
