#Here we are zomming the entire frame data to specific co-ordinates
#And we resize the frame 

import cv2
import numpy as np

cap=cv2.VideoCapture(0)

x1=int(input("Enter the first co-ordinate in X:"))
x2=int(input("Enter the second co-ordinate in X:"))
y1=int(input("Enter the first co-ordinate in Y:"))
y2=int(input("Enter the second co-ordinate in Y:"))

#put default value of x1=200,x2=400,y1=75,y2=360----> just to test



while True:
          _,frame=cap.read()
          T=frame.shape

          cv2.circle(frame,(x1,y1),5,(255,0,0),-1)

          cv2.circle(frame,(x2,y1),5,(255,0,0),-1)

          cv2.circle(frame,(x1,y2),5,(255,0,0),-1)
          
          cv2.circle(frame,(x2,y2),5,(255,0,0),-1)

          pts1=np.float32([[x1,y1],[x2,y1],[x1,y2],[x2,y2]])

          pts2=np.float32([[0,0],[T[1],0],[0,T[0]],[T[1],T[0]]])

          matrix=cv2.getPerspectiveTransform(pts1,pts2)

          result=cv2.warpPerspective(frame,matrix,( T[1],T[0]))

          cv2.imshow('frame',frame)
          cv2.imshow('result',result)
          key=cv2.waitKey(1)
          if key==ord('q'):
                    break
                    
cap.release()
cv2.destroyAllWindows()
