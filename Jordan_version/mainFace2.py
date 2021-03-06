# HackTCNJ 2020 project
# facial and eye detection program to determine if person falls asleep
# if asleep for > desired time period, set of alarm

import cv2
import numpy as np
from playsound import playsound

# font definitions
font = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10,200)
fontScale = 0.5
fontColor = (255,0,0)
lineType = 2

# import face harr classifiers
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# import eye harr classifiers
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

# opens video capture
cap = cv2.VideoCapture(0)\

countEyesClosed = 0

while 1:
    ret, img = cap.read() # reading capture
    if ret:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # create grayscale version of image
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            # flags = cv2.CV_HAAR_SCALE_IMAGE
        )

        if len(faces) > 0:
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]
                cv2.putText(img, 'Face Detected', (10,100), font, fontScale, (255,0,0), lineType)

                #eyes = eye_cascade.detectMultiScale(roi_gray)
                frame_tmp = img[faces[0][1]:faces[0][1] + faces[0][3], faces[0][0]:faces[0][0] + faces[0][2]:1]
                gray = gray[faces[0][1]:faces[0][1] + faces[0][3], faces[0][0]:faces[0][0] + faces[0][2]:1]
                eyes = eye_cascade.detectMultiScale(
                    gray,
                    scaleFactor=1.1,
                    minNeighbors=5,
                    minSize=(30, 30),
                )
                if len(eyes) == 0:
                    countEyesClosed += 1
                    print(countEyesClosed)
                else:
                    print(countEyesClosed)
                    #countEyesClosed += 1
                    cv2.putText(img, 'Eyes Detected',bottomLeftCornerOfText,font,fontScale,(0,255,0),lineType)
                    cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

                if countEyesClosed >= 1000:
                    playsound('audio2.mp3')
                    countEyesClosed = 0

            cv2.imshow('img',img)

        waitkey = cv2.waitKey(1)
        if waitkey == ord('q') or waitkey == ord('Q'):
            cv2.destroyAllWindows()
            break

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')