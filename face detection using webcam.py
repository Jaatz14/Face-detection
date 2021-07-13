import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

cap = cv2.VideoCapture(0)     # 0 for webcam

while True :
    _, img = cap.read()     # for reading image

    if(_ ==False):          # _ is a flag for detection 
        continue

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)     # converting img to grayscale img

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)            #detecting faces    ( input_image, scale_factor, min_neighbours)

    for(x, y, w, h) in faces:       
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('Webcam',img)

    key_pressed = cv2.waitKey(30) & 0xFF
    if key_pressed == 27:                    #escape for breaking
        break
cap.release()
