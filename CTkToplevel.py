from customtkinter import *
from tkinter import ttk
from tkinter import *
a=CTk()
a.title()
a.geometry('700x500')
def g():
    a1=CTkToplevel()
    a1.title()
    a.geometry('700x500')
    p=PhotoImage(file='images (1).png')
    l=ttk.Label(a1,image=p)
    l.place(x=10,y=10)
    a1.mainloop()
b3=CTkButton(master=a,text='xayot uchun xafli',command=g)
b3.place(x=20,y=90)
a.mainloop()