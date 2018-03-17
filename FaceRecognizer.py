# -*- coding: utf-8 -*-
import cv2
import FaceTrainer
import FaceDetection
import FaceConfig


def RecognizeFace(image, faceCascade, eyeCascade, faceSize, threshold,recognizer):
    found_faces = []

    gray, faces = FaceDetection.detectFaces(image, faceCascade, eyeCascade, returnGray=1)

    # If faces are found, try to recognize them
    for ((x, y, w, h), eyedim)  in faces:
        label, confidence = recognizer.predict(cv2.resize(FaceDetection.levelFace(gray, ((x, y, w, h), eyedim)), faceSize))
        print(label)
        print(confidence)
        # note that for some distributions of python-opencv, the predict function
        # returns the label only.
        #label = recognizer.predict(cv2.resize(detect.levelFace(gray, ((x, y, w, h), eyedim)), faceSize))
        #confidence = -1
        if confidence < threshold:
            found_faces.append((label, confidence, (x, y, w, h)))

    return found_faces


#if __name__ == '__main__':
def FaceRecognize():

    faceCascade = cv2.CascadeClassifier(FaceConfig.FACE_CASCADE_FILE)
    eyeCascade = cv2.CascadeClassifier(FaceConfig.EYE_CASCADE_FILE)
    faceSize = FaceConfig.DEFAULT_FACE_SIZE
    threshold = 500
    labelinfo=[]

    labelinfo,recognizer= FaceTrainer.trainRecognizer('dataSet',faceSize, showFaces=False,forceTrain=True)

    name=None
    cv2.namedWindow("camera", 1)
    capture = cv2.VideoCapture(0)
    while True:
        retval, img = capture.read()

        for (label, confidence, (x, y, w, h)) in RecognizeFace(img, faceCascade, eyeCascade, faceSize, threshold,recognizer):

            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)


            #print(labelinfo[label][1])
            if(confidence<70):
                cv2.putText(img, "{} = {}".format(labelinfo[label][1], int(confidence)), (x, y), cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.CV_AA)
                name=labelinfo[label][1]
                break
        cv2.imshow("camera", img)

        #if cv2.waitKey(30) & 0xFF == ord('q'):
        if (name is not None):
            break
    return name;