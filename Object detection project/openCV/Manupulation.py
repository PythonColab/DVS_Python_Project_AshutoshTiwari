import cv2

import numpy as np
import matplotlib.pyplot as plt



cap = cv2.VideoCapture(0)

vw=cv2.videoWriter_fourcc(*'XVID')   
out=cv2.videoWriter('Output.avi',vw,20.0,(640,480))
 
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    out.write(frame)
 
    cv2.imshow('frame',frame)
    cv2.imshow('Another frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

out.release()

cv2.destroyAllWindows()



    

