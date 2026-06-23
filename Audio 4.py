from tkinter import *
import pyttsx3
e = pyttsx3.init()
a = Tk()
a.title("")
a.geometry('500x500')
def l():
    if e1.get()=='Assalomu alekum':
       e.say('Valekum Assalom')
       e.runAndWait()
    elif e1.get()=='Sani isming nima':
       e.say('Suniy intulekt')
       e.runAndWait()
    elif e1.get()==('Dunyodagi eng chiroyli Ayol'):
       e.say('Ona')
       e.runAndWait()
e1 = Entry(a, width=10)
e1.place(x=50, y=50)
b = Button(a, text="Speak", width=10, command=l)
b.place(x=10, y=10)
a.mainloop()