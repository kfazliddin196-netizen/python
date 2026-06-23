from tkinter import *
import pyttsx3
e = pyttsx3.init()
a = Tk()
a.title("")
a.geometry('700x500')
a.configure(bg='black')
def sekin():
    t = e1.get().strip()
    if t:
        e.say(t)
        e.runAndWait()
    else:
        e.say("Iltimos, biror matn kiriting.")
        e.runAndWait()
e1 = Entry(a, width=10, bg='red')
e1.pack(anchor=CENTER, pady=10)
b = Button(a, text="Sekin", width=10, command=sekin)
b.place(x=300,y=50)
a.mainloop()