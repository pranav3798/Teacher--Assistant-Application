import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    r.adjust_for_ambient_noise(source, duration=0.1)
    audio = r.listen(source)
    print("thanks")
try:
    text = r.recognize_google(audio)
    #print("Hi")
    l=list(text)
    
    fw=open('speech-text.txt','w')
    fw.writelines(l)

    print("You said : {}".format(text))
except:
    print("Sorry could not recognize what you said")
fw.close()