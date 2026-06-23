from tkinter import *
import pyttsx3
e = pyttsx3.init()
a = Tk()
a.title("")
a.geometry('700x500')
a.configure(bg='black')
def sekin():
    e.setProperty('rate', 200)  # Ovozni tezlashtirish tezligi
    t = e1.get().strip()
    if t:
        e.say(t)
        e.runAndWait()
    else:
        e.say("Iltimos, biror matn kiriting.")
        e.runAndWait()
def orta():
    e.setProperty('rate', 400)  # Ovozni tezlashtirish tezligi
    t = e1.get().strip()
    if t:
        e.say(t)
        e.runAndWait()
    else:
        e.say("Iltimos, biror matn kiriting.")
        e.runAndWait()
def Tez():
    e.setProperty('rate', 600)  # Ovozni tezlashtirish tezligi
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
b1 = Button(a, text="Orta", width=10, command=orta)
b1.place(x=300,y=100)
b2 = Button(a, text="Tez", width=10, command=Tez)
b2.place(x=300,y=150)

a.mainloop()
