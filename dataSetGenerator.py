# -*- coding: utf-8 -*-
import cv2
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

cam = cv2.VideoCapture(0)
detector=cv2.CascadeClassifier('Classifiers/face.xml')

i=0
offset=50

id=raw_input('enter your id')
name=raw_input('enter your name')
unicname=unicode(name,"utf-8")
newpath = "dataSet/"+unicname

if not os.path.exists(newpath):
    os.makedirs(newpath)

    while True:
        ret, im =cam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
        for(x,y,w,h) in faces:
            i=i+1
            cv2.imwrite(("dataSet/"+name+"/face-"+id+'.'+ str(i) + ".jpg").encode("windows-1252"), gray[y-offset:y+h+offset,x-offset:x+w+offset])
            cv2.rectangle(im,(x-50,y-50),(x+w+50,y+h+50),(225,0,0),2)
            cv2.imshow('im',im[y-offset:y+h+offset,x-offset:x+w+offset])
            cv2.waitKey(100)
        if i>20:
            cam.release()
            cv2.destroyAllWindows()
            break
else:
    print("var")
