import cv2
import numpy as np
import os
import xlsxWriter
from datetime import datetime;
import firebase_admin;
from firebase_admin import credentials;
from firebase_admin import storage;


cred=credentials.Certificate('C:\\Users\\Pranav Mahajan\\Desktop\\Review\\Teacher-Assistant\\firebase\\capstone-60eb9-firebase-adminsdk-3kesq-995d9f6207.json');
default_app=firebase_admin.initialize_app(cred,{
'storageBucket': 'capstone-60eb9.appspot.com'
});

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
font = cv2.FONT_HERSHEY_SIMPLEX
id = 0
names = ['None', 'Udai', 'Mayank','Anand','Piyush','Pranav'] 
cam = cv2.VideoCapture(0)
cam.set(3, 640) 
cam.set(4, 480) 
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

workbook=xlsxWriter.Workbook("C:\\Users\\Pranav Mahajan\\Desktop\\Review\\Teacher-Assistant\\firebase\\attendance_files\\attendance"+str(datetime.now().date())+'.xls')
worksheet = workbook.add_worksheet()
row = 2
column = 0
content=set()
worksheet.write('A1', 'Name') 
worksheet.write('B1', 'Present') 
while True:
    ret, img =cam.read()
    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale(gray,scaleFactor = 1.2,minNeighbors = 5,minSize = (int(minW), int(minH)),)
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
                
        if (confidence < 100):
            id = names[id]
            confidence = "  {0}%".format(round(confidence))
            content.add(str(id))
            
        else:
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))
        
        cv2.putText(img,str(id),(x+5,y-5),font,1,(255,255,255),2)
        cv2.putText(img,str(confidence),(x+5,y+h-5),font,1,(255,255,0),1)  
    
    cv2.imshow('camera',img) 
    k = cv2.waitKey(10) & 0xff 
    if k == 27:
        break
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
for val in content:
	worksheet.write(row, column, val)
	column=1
	worksheet.write(row, column, 'Yes')
	row += 1
	column=0
worksheet.write(row,0,'Total Present')
worksheet.write(row,1,len(content))
workbook.close()
print(content)


bucket=storage.bucket();
uploadBlob = bucket.blob("attendance"+str(datetime.now().date())+'.xls');
#uploadBlob = bucket.get_blob('attendance2018-09-10.xls');
#print(uploadBlob);
uploadBlob.upload_from_filename(filename="C:\\Users\\Pranav Mahajan\\Desktop\\Review\\Teacher-Assistant\\firebase\\attendance_files\\attendance"+str(datetime.now().date())+'.xls');
print('file uploaded! ');

cv2.destroyAllWindows()