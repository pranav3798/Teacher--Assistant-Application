import firebase_admin;
from firebase_admin import credentials;
from firebase_admin import storage;
from datetime import datetime;

cred=credentials.Certificate('C:\\Users\\Pranav Mahajan\\Desktop\\Review\\Teacher-Assistant\\firebase\\capstone-60eb9-firebase-adminsdk-3kesq-995d9f6207.json');
default_app=firebase_admin.initialize_app(cred,{
'storageBucket': 'capstone-60eb9.appspot.com'
});
bucket=storage.bucket();
uploadBlob = bucket.blob("attendance"+str(datetime.now().date())+'.xls');
#uploadBlob = bucket.get_blob('attendance2018-09-10.xls');
#print(uploadBlob);
uploadBlob.upload_from_filename(filename="C:\\Users\\Pranav Mahajan\\Desktop\\Review\\Teacher-Assistant\\firebase\\attendance_files\\attendance"+str(datetime.now().date())+'.xls');
print('file uploaded! ');
