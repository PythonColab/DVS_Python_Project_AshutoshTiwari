# -*- coding: utf-8 -*-
"""
Created on Wed May  9 06:48:37 2018

@author: Ashutosh
"""

import cv2
import matplotlib.pyplot as plt
img=cv2.imread('E:\\Games\\Internship\\python\\Object detection project\\openCV\\ashu.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#cv2.imWrite('Ash.png',img)


"""plt.imshow(img,cmap='grey',interpolation='bicubic')
plt.plot([50,100],[80,100],'c',linewidth=5)
plt.show()"""





#--------------creating shapes

import cv2
import matplotlib.pyplot as plt
import numpy as np
img=cv2.imread('E:\\Games\\Internship\\python\\Object detection project\\openCV\\ashu.jpg',cv2.IMREAD_COLOR)

cv2.line(img,(0,0),(150,150),(255,0,0),15)# on image,where line starts,line end,color of line,line width
cv2.rectangle(img,(15,25),(150,100),(0,255,0),5) #top left cordinate,bottom right cordinate
cv2.circle(img,(120,60),40,(0,0,255),2)#center,radius,color,fill or not(negative will fill the circle)

#polygon2
pts=np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
#pts=pts.reshape([-1,1,2])
cv2.polylines(img,[pts],True,(0,255,255),3) #points,connect the last point to first or dont want to,color,width

#writing something
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Ashutosh',(30,50),font,1,(255,255,100),3,cv2.LINE_AA)#text,start point,font,size of text,color,Thickness of text

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()




#---------image operation-------------

#mostly everry analysis is done on the gray images it will be shown colored and taken everything in grey and operation is performed after that the suoerimposing of colored image is done

import cv2
import matplotlib.pyplot as plt
img=cv2.imread('E:\\Games\\Internship\\python\\Object detection project\\openCV\\ashu.jpg',cv2.IMREAD_COLOR)

px=img[55,55] #color value for that pixel
print(px)

img[55,55]=[255,255,255] #we can change the color of the particular pixel
print(px)


#other characterstics
print(img.shape)
print(img.size)
print(img.dtype)

roi=img[100:150,100:150]#region of the image(ROI)-dub image of a image
print(roi) #gives the numpy array which contain all pixel value of that ROI

img[100:150,100:150]=[255,255,255] # the region become big white square

#take ROI and copy and paste ant other position
myface=img[37:111,107:194]
img[0:74,0:87]=myface

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()




#----------------------operation on image
import cv2
import matplotlib.pyplot as plt
img1=cv2.imread('E:\\Games\\Internship\\python\\Object detection project\\openCV\\mnm.jpg')
img2=cv2.imread('E:\\Games\\Internship\\python\\Object detection project\\openCV\\mnm.jpg') 

add=img1+img2 #this perform different operation


add=cv2.add(img1,img2)#add pixel value together
#Example-->(155,211,79) + (50, 170, 200) = 205, 381, 279...translated to (205, 255,255).

weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)#like first image part is 60% and second of 40% and last argument is gamma  
cv2.imshow('weighted',weighted)#weighted 
cv2.waitKey(0)
cv2.destroyAllWindows()
#For the addWeighted method, the parameters are the first image, the weight, the second image, that weight, and then finally gamma, which is a measurement of light. We'll leave that at zero for now.


cv2.imshow('Adding',add)   
cv2.waitKey(0)
cv2.destroyAllWindows()




#---------------takin out the image section
img1=cv2.imread('E:\\Games\\Internship\\python\\Object detection project\\openCV\\mainlogo.png') 
img2=cv2.imread('E:\\Games\\Internship\\python\\Object detection project\\openCV\\ashu.jpg') 

rows,cols,channels=img2.shape
roi=img1[0:rows,0:cols]

img2gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)#convert the color to grey
ret,mask=cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY_INV)#if more than 220 it converted into 255 or in while and if it is below 220 so it converted into black

mask_inv=cv2.bitwise_not(mask)

img1_bg=cv2.bitwise_and(roi,roi,mask=mask_inv)#background
img1_fg=cv2.bitwise_and(roi,roi,mask=mask)#foregrounf 
dat=cv2.add(img1_bg,img1_fg)
img1[0:rows,0:cols]=dat

cv2.imshow('Adding',mask  )   
cv2.waitKey(0)
cv2.destroyAllWindows()

#Thresholding with opencv-Everything be converted into 0 and 1 may be in black and white color 

img=cv2.imread('E:\\Games\\Internship\\python\\Object detection project\\openCV\\bookp.jpeg') 
img=cv2.imread('E:\\Games\\Internship\\python\\Object detection project\\openCV\\first.jpg') 

retval,threshold=cv2.threshold(img,95,255,cv2.THRESH_BINARY)

grayscaled=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval2,threshold2=cv2.threshold(grayscaled,150,255,cv2.THRESH_BINARY)

retval3,threshold3=cv2.threshold(grayscaled,99,255,cv2.THRESH_BINARY)

gaus=cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)#best
retval4,otsu=cv2.threshold(grayscaled,203,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow('original',img)
cv2.imshow('threshold',threshold)
cv2.imshow('threshold2',threshold2)
cv2.imshow('threshold3',threshold3)
cv2.imshow('gaus',gaus)
cv2.imshow('otsu',otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()


#filtera image or video for specific range of colors 
#finding specific color,removing specific color 
#show specific color or show all color

import cv2
import numpy as np
cap=cv2.VideoCapture(0)

while True:
    _,frame=cap.read() # _ is a variable 
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)#hue,saturation,value
    
    lower_red=np.array([50,0,0])   #Change this to change HSV 
    upper_red=np.array([180,255,150])
    
    #dark_red=np.unit8([[[12,22,121]]])   we use t5hese to convert BGR to HSV but we use default our own nump array as above var
    #dark_red=cv2.cvtColor(dark_red,cv2.COLOR_BGR2HSV)
    
    mask=cv2.inRange(hsv,lower_red,upper_red) #it is the things which is in the range here everything comes inside or mask is now identical to the frame variable
    res=cv2.bitwise_and(frame,frame,mask=mask)#something in the fame where mask is true like 1 for white now everything is 1
   
    
    #blurring technique kernel=np.ones((15,15), np.float32)/225
    #blurring technique smoothed=cv2.filter2D(res,-1,kernel)
    
    #garguian blur   
    blur=cv2.GaussianBlur(res,(15,15),0)
    #median blur
    median=cv2.medianBlur(res,15)
    #bilateral blur or filter
    bilateral=cv2.bilateralFilter(res,15,75,75)
    
    cv2.imshow('frame',frame)
    # cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    cv2.imshow('blur',blur)
    cv2.imshow('median',median)
    cv2.imshow('bilateral',bilateral)
   # cv2.imshow('smoothed',smoothed)
    
    
    k=cv2.waitKey(5) & 0xFF
    if k==27:
        break
    
cv2.destroyAllWindows()
cap.release()    
    

#Too many noise in previous program that can be removed by foreground extraction and background abstraction
# the things which are falsely detect is also a problem.
#morphological transformation--
#these are of many types-->
#1.errosion endilation--Mstudy about it

import cv2
import numpy as np
cap=cv2.VideoCapture(0)

while True:
    _,frame=cap.read() # _ is a variable 
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)#hue,saturation,value
    
    lower_red=np.array([50,100,10])   #Change this to change HSV 
    upper_red=np.array([255,255,255])
 
    mask=cv2.inRange(hsv,lower_red,upper_red) #it is the things which is in the range here everything comes inside or mask is now identical to the frame variable
    res=cv2.bitwise_and(frame,frame,mask=mask)#something in the fame where mask is true like 1 for white now everything is 1
    

    
    
    cv2.imshow('frame',frame)
    cv2.imshow('res',res)
 
    
    k=cv2.waitKey(5) & 0xFF
    if k==27:
        break
    
cv2.destroyAllWindows()
cap.release()    
    
 
    
#-----------------------just testing of object detection(not working)

import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

img = cv2.imread('E:\\Games\\Internship\\python\\Object detection project\\openCV\\ashu.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()



#-------------------------]morphological transformation


import cv2
import numpy as np
cap=cv2.VideoCapture(0)

while True:
    _,frame=cap.read() # _ is a variable 
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)#hue,saturation,value
    
    lower_red=np.array([0,120,150])   #Change this to change HSV 
    upper_red=np.array([60,255,255])
 
    mask=cv2.inRange(hsv,lower_red,upper_red) #it is the things which is in the range here everything comes inside or mask is now identical to the frame variable
    res=cv2.bitwise_and(frame,frame,mask=mask)#something in the fame where mask is true like 1 for white now everything is 1
    
    kernel=np.ones((5,5))
    erosion=cv2.erode(mask,kernel,iterations=1)
    dilation=cv2.dilate(mask,kernel,iterations=1)
    
    opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
    closing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
    
    
    cv2.imshow('frame',frame)
    cv2.imshow('res',res)
    cv2.imshow('erosion',erosion)
    cv2.imshow('dialation',dilation)
    cv2.imshow('Opening',opening)#outside the object
    cv2.imshow('Closing',closing)#inside oject
    
    k=cv2.waitKey(5) & 0xFF
    if k==27:
        break
    
cv2.destroyAllWindows()
cap.release()  
  

#--------------------gradient and edge detection  


import cv2
import numpy as np
cap=cv2.VideoCapture(0)

while True:
    _,frame=cap.read() # _ is a variable 
    
    laplacien=cv2.Laplacian(frame,cv2.CV_64F)
    sobelx=cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)#frame,datatype,x-axis,y-axis,kernelsize
    sobely=cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)
    
    #there are many edge detectors are available and here we use canny as edge detector
    edges100=cv2.Canny(frame,100,100)
    edges200=cv2.Canny(frame,100,200)
    edges50=cv2.Canny(frame,50,50)#more noise
    
    
    cv2.imshow('Original',frame)
    cv2.imshow('Lapacian',laplacien)
    cv2.imshow('sobelx',sobelx)
    cv2.imshow('sobely',sobely)
    cv2.imshow('edges100',edges100)
    cv2.imshow('edges200',edges200)
    cv2.imshow('edges50',edges50)
    k=cv2.waitKey(5) & 0xFF
    if k==27:
        break
    
cv2.destroyAllWindows()
cap.release()  
  


#------------TEMPLATE MATCHING
import cv2
import numpy as np
img1=cv2.imread('E:\\Games\\Internship\\python\\Object detection project\\openCV\\mainlogo.png') 







