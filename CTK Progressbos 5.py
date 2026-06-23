import tkinter.messagebox

from customtkinter import *
from tkinter.messagebox import showinfo
a = CTk()
a.title("Progress Bar Demo")
a.geometry("500x500")

def Ulash():
    p1 = int(p.get() * 101)
    l.configure(text=f"Progress: {p1}%")
    if p1 < 100:
        a.after(100, Ulash)
    if p1==100 and p.stop():
            showinfo(message="o'tqazildi",title="Xabar")

def s():
    p.start()
    Ulash()
def m():
    p.stop()
s = CTkButton(master=a, text="Start", command=s)
s.place(x=10, y=100)
s = CTkButton(master=a, text="Stop",command=m)
s.place(x=10, y=150)
p = CTkProgressBar(master=a, orientation='horizontal', determinate_speed=0.5)
p.place(x=10, y=10)
p.set(0)

l = CTkLabel(master=a, text="Progress: 0%")
l.place(x=10, y=50)

a.mainloop()
