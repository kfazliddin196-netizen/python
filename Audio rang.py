from tkinter import *
import pyttsx3
e=pyttsx3.init()
a=Tk()
a.title()
a.geometry('500x500')
def  d():
     a['bg'] = e1.get()
     e.say(e1.get())
     e.runAndWait()
e1 = Entry(width=10)
e1.place(x=50, y=50)
b=Button(width=10,command=d)
b.place(x=10,y=10)
a.mainloop()