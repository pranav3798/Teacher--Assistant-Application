from gtts import gTTS
from playsound import playsound

import os

fd=open('text-speech.txt','r')
l=fd.read()
language='en'
myobj = gTTS(text=l, lang=language, slow=False) 
  

myobj.save("welcome.mp3") 
  

playsound('welcome.mp3')