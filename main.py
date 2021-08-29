import cv2
import numpy as np
import face_recognition

imgjord = face_recognition.load_image_file('imagesbasic/Jordan_Fisher.jpg')
imgjord = cv2.cvtColor(imgjord,cv2.COLOR_BGR2RGB)
imgtest = face_recognition.load_image_file('Imagesbasic/Jordan_Fisher_test.jpg')
imgtest = cv2.cvtColor(imgtest,cv2.COLOR_BGR2RGB)

faceloc = face_recognition.face_locations(imgjord)[0]
encodejord = face_recognition.face_encodings(imgjord) [0]
cv2.rectangle(imgjord,(faceloc[3] ,faceloc[0]),(faceloc[1],faceloc[2]),(255,5,255))

faceloctest = face_recognition.face_locations(imgtest)[0]
encodetest = face_recognition.face_encodings(imgtest) [0]
cv2.rectangle(imgtest,(faceloctest[3] ,faceloctest[0]),(faceloctest[1],faceloctest[2]),(255,5,255))

results = face_recognition.compare_faces([encodejord],encodetest)
facedis = face_recognition.face_distance ([encodejord],encodetest)
print(results,facedis)
cv2.putText(imgtest,f'{results} {round(facedis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)


cv2.imshow('Jordan fisher',imgjord)
cv2.imshow('Jordan test',imgtest)
cv2.waitKey(0)