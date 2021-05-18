import cv2
import dlib
import face_recognition

#printing the version
print(cv2.__version__)
print(dlib.__version__)
print(face_recognition.__version__)
img = cv2.imread("C:/Users/chand/Downloads/WhatsApp Image 2021-01-23 at 4.10.47 PM.jpeg")
cv2.imshow('image', img)
