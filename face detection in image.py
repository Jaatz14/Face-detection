import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")    #classifier for detecting faces

img = cv2.imread('stock.JPG')                                               #for image reading

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)               #converting colored image to grayscale

faces = face_cascade.detectMultiScale(gray, 1.18, 5)        #detecting faces

for(x,y,w,h) in faces :         #for drawing rectangle over img
    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)            

cv2.imshow('img', img)                #for displaying image

cv2.waitKey()                         #for exiting