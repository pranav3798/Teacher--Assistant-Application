from tkinter import *
from playsound import playsound
import os
from datetime import datetime;

root=Tk()

root.configure(background="white")

def function1():
    
    os.system("py dataset_capture.py")
    
def function2():
    
    os.system("py training_dataset.py")

def function3():

    os.system("py detect.py")
    playsound('sound.mp3')
   
def function6():

    root.destroy()

def function7():
    
    os.system("py text_speech.py")

def function8():
    
    os.system("py speech_text.py")

def function9():
    
    os.system("py search_bar.py")

def attend():
    os.startfile(os.getcwd()+"\\firebase\\attendance_files\\attendance"+str(datetime.now().date())+'.xls')


root.title("TEACHER ASSISTANT APPLICATION USING IMAGE AND SPEECH RECOGNITION")


Label(root, text="TEACHER ASSISTANT APPLICATION USING IMAGE AND SPEECH RECOGNITION",font=("times new roman",20),fg="white",bg="#0C0A3E",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


Button(root,text="Create Dataset",font=("times new roman",20),bg="#006BA6",fg='white',command=function1).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)


Button(root,text="Train Dataset",font=("times new roman",20),bg="#006BA6",fg='white',command=function2).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Take Attendance",font=('times new roman',20),bg="#006BA6",fg="white",command=function3).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Check Attendance Sheet",font=('times new roman',20),bg="#006BA6",fg="white",command=attend).grid(row=6,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Text-To-Speech",font=('times new roman',20),bg="#006BA6",fg="white",command=function7).grid(row=7,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Speech-To-Text",font=('times new roman',20),bg="#006BA6",fg="white",command=function8).grid(row=8,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Search Bar",font=('times new roman',20),bg="#006BA6",fg="white",command=function9).grid(row=9,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Exit",font=('times new roman',20),bg="#0C0A3E",fg="white",command=function6).grid(row=11,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


root.mainloop()
