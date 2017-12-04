import os
from os.path import join, isdir
import cv2
import numpy as np

import FaceDetection
import FaceConfig



def getLabels(a_dir):
    return [name for name in os.listdir(a_dir) if isdir(join(a_dir, name))]

def supportedImg(name):
    return name.lower().endswith('.png') or name.lower().endswith('.jpg')

def combineFaces(faces, w=100, h=100, numPerRow=5):
    small_img = []
    row_img = []
    count = 0
    for img in faces:
        small_img.append(cv2.resize(img, (w, h)))
        count += 1
        if count % numPerRow == 0:
            count = 0
            row_img.append(np.concatenate(small_img, axis=1))
            small_img = []
    if len(small_img) > 0:
        for x in range (0, numPerRow-len(small_img)):
            small_img.append(np.zeros((h,w), np.uint8))
        row_img.append(np.concatenate(small_img, axis=1))

    return np.concatenate(row_img, axis=0)

def extractFaces(a_dir, folder, levelFace=False):
    faceCascade = cv2.CascadeClassifier(FaceConfig.FACE_CASCADE_FILE)
    eyeCascade = cv2.CascadeClassifier(FaceConfig.EYE_CASCADE_FILE)

    the_path = join(a_dir, folder)
    result = []

    for img in [f for f in os.listdir(the_path) if supportedImg(f)]:
        img_path = join(the_path, img)
        image, faces = FaceDetection.detectFaces(cv2.imread(img_path), faceCascade, eyeCascade, True)
        if len(faces) == 0:
            print("No face found in " + img_path)
        for ((x, y, w, h), eyedim) in faces:
            print(img_path)
            if not levelFace:
                result.append(image[y:y+h, x:x+w])
            else:
                result.append(FaceDetection.levelFace(image, ((x, y, w, h), eyedim)))
                #result.append(image[y:y+h, x:x+w])
    return result

def trainRecognizer(db_folder ,trainSize=FaceConfig.DEFAULT_FACE_SIZE, showFaces=False, forceTrain=False):
    #recognizer = cv2.face.createLBPHFaceRecognizer()
    recognizer = cv2.createFisherFaceRecognizer()
    #recognizer = cv2.face.createEigenFaceRecognizer()
    info=[]

    if (not forceTrain) and loadRecognizer(recognizer):
        return recognizer

    folders = getLabels(db_folder)
    images = []
    labels = []

    label_count = 0
    label_map = {}

    for folder in folders:
        faces = extractFaces(db_folder, folder, True)

        # resize all faces to same size for some recognizers
        images.extend([cv2.resize(face, trainSize) for face in faces])

        labels.extend([label_count] * len(faces))
        label_map[label_count] = folder
        label_count += 1

        if showFaces:
            cv2.namedWindow("faces", 1)
            cv2.imshow("faces", combineFaces(faces))
            cv2.waitKey(0)

    if showFaces:
        cv2.destroyWindow("faces")

    recognizer.train(images, np.array(labels))
    for key in label_map:
        #print(label_map[key])
        #print(key)

        info.append((key,label_map[key]))
        info2=(key,label_map[key])
        #print(info2)
        #print(info2[1])
        #print(info)
        #print(info[0][1])

    saveRecognizer(recognizer)
    #print(info)
    return info,recognizer

def saveRecognizer(recognizer, filename=FaceConfig.RECOGNIZER_OUTPUT_FILE):
    recognizer.save(filename)

def loadRecognizer(recognizer, filename=FaceConfig.RECOGNIZER_OUTPUT_FILE):
    try:
        recognizer.load(filename)
        return True
    except (cv2.error):
        return False

if __name__ == '__main__':
    recognizer = trainRecognizer("dataSet", showFaces=False, forceTrain=True)
