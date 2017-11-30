import cv2
import  numpy as np
import os
from PIL import Image
faceDetect=cv2.CascadeClassifier("haarcascade_frontalface_default.xml");
cam=cv2.VideoCapture(0);
rec=cv2.face.LBPHFaceRecognizer_create()
print(dir(rec))
rec.save("recognizer/trainingData.yml")
cascadePath = "Classifiers/face.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
id=0

fontface = cv2.FONT_HERSHEY_SIMPLEX
fontscale = 1
fontcolor = (255, 255, 255)

while (True):
    ret, img = cam.read();
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100),flags=cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in faces:


        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        id, conf = rec.predict(gray[y:y + h, x:x + w])
        if (id == 1):
            id = "Teyfik"
        elif (id == 2):
            id = "İbrahim"
        cv2.putText(img, str(id), (x, y + h), fontface, fontscale, fontcolor)
    cv2.imshow("Face", img);
    if (cv2.waitKey(1) == ord('q')):
        break;

cam.release()
cv2.destroyAllWindows()

