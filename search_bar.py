from tkinter import *
from tkinter import ttk
import webbrowser
import speech_recognition as sr
from pygame import mixer
import wikipedia
 

root = Tk()
root.title('Universal Search Bar')

style = ttk.Style()
style.theme_use('winnative')


label1 = ttk.Label(root, text='Query:')
label1.grid(row=0, column=0)
entry1 = ttk.Entry(root, width=50)
entry1.grid(row=0, column=1, columnspan=4)

btn2 = StringVar()

def callback():
    
    if btn2.get() == 'google' and entry1.get() != '':
        webbrowser.open('http://google.com/search?q='+entry1.get())
        
    elif btn2.get() == 'duck' and entry1.get() != '':
        webbrowser.open('http://duckduckgo.com/?q='+entry1.get())

    elif btn2.get() == 'amz' and entry1.get() != '':
        webbrowser.open('https://amazon.com/s/?url=search-alias%3Dstripbooks&field-keywords='+entry1.get())

    elif btn2.get() == 'ytb' and entry1.get() != '':
        webbrowser.open('https://www.youtube.com/results?search_query='+entry1.get())

    elif btn2.get() == 'wiki' and entry1.get() != '':
        webbrowser.open('https://en.m.wikipedia.org/wiki/Special:Search?search='+entry1.get())
        complete_content = wikipedia.page(entry1.get())
        l=list(complete_content.content)
        fw=open('Content.txt','w')
        fw.writelines(l)

    else:
        pass

def get(event):

    if btn2.get() == 'google' and entry1.get() != '':
        webbrowser.open('http://google.com/search?q='+entry1.get())
        
    elif btn2.get() == 'duck' and entry1.get() != '':
        webbrowser.open('http://duckduckgo.com/?q='+entry1.get())

    elif btn2.get() == 'amz' and entry1.get() != '':
        webbrowser.open('https://amazon.com/s/?url=search-alias%3Dstripbooks&field-keywords='+entry1.get())

    elif btn2.get() == 'ytb' and entry1.get() != '':
        webbrowser.open('https://www.youtube.com/results?search_query='+entry1.get())

    elif btn2.get() == 'wiki' and entry1.get() != '':
        webbrowser.open('https://en.m.wikipedia.org/wiki/Special:Search?search='+entry1.get())
        complete_content = wikipedia.page(entry1.get())
        l=list(complete_content.content)
        fw=open('Content.txt','w')
        fw.writelines(l)

    else:
        pass


entry1.bind('<Return>', get)

MyButton1 = ttk.Button(root, text='Search', width=10, command=callback)
MyButton1.grid(row=0, column=6)

MyButton2 = ttk.Radiobutton(root, text='Google', value='google', variable=btn2)
MyButton2.grid(row=1, column=0, sticky=W)

MyButton3 = ttk.Radiobutton(root, text='Duck', value='duck', variable=btn2)
MyButton3.grid(row=1, column=1, sticky=W)

MyButton4 = ttk.Radiobutton(root, text='Amazon', value='amz', variable=btn2)
MyButton4.grid(row=1, column=2)

MyButton5 = ttk.Radiobutton(root, text='Youtube', value='ytb', variable=btn2)
MyButton5.grid(row=1, column=3, sticky=E)

MyButton6 = ttk.Radiobutton(root, text='Wikipedia', value='wiki', variable=btn2)
MyButton6.grid(row=1, column=4, sticky=W)


entry1.focus()
root.wm_attributes('-topmost', 1)
btn2.set('google')
root.mainloop()