import cv2
import numpy as np

car_classifier = cv2.CascadeClassifier('haarcascade_car.xml')
body_classifier = cv2.CascadeClassifier('haarcascade_fullbody.xml')


video = cv2.VideoCapture('traffic_signal_video.mp4')

while True:

    ret,frame = video.read()
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)

    cars = car_classifier.detectMultiScale(gray, 1.1 , 2)
    bodies = body_classifier.detectMultiScale(gray, 1.1, 3)

    print(cars)

    

    for(x,y,w,h) in cars:
        cv2.rectangle(frame , (x,y) ,(x+w, y+h) , (0,255,255), 2)
        cv2.imshow('Pedestrians',frame)
        cv2.putText(frame,' CAR',(x,y-10),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0),4)

    for (px,py,pw,ph) in bodies:
        cv2.rectangle(frame, (px, py), (px+pw, py+ph), (0, 0, 255), 2)
        cv2.putText(frame,' HUMAN',(px,py-10),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0),4)
        cv2.imshow('Pedestrians', frame)



    Key=cv2.waitKey(1)
    if Key==ord('q') or Key == 25000:
        #release the camera
        video.release()
        #destroy all windows
        cv2.destroyAllWindows()
        break
    
