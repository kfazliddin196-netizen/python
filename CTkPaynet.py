from customtkinter import *
from tkinter import *
import pyttsx3
e=pyttsx3.init()
from tkinter.messagebox import askyesno,showinfo
def f1():
    a3=Toplevel()
    a3.title()
    a3.geometry('500x450')
    def h1():
        Nomer = e.get().strip()
        Summa = e12.get().strip()
        if Nomer and Summa :
         r = askyesno(title='Xabar', message='Chek olasizmi')
         if r:
            showinfo(title='Xabar', message='To\'lov o\'tdi:\nNo\'mer raqamingiz:\n' + e12.get() + '\nSumma:' + e.get())
    e12=CTkEntry(master=a3,width=250,font=('Arial',32),placeholder_text="_ ___ __ ___ __ __")
    e12.place(x=25,y=10)
    e=CTkEntry(master=a3,width=250,font=('Arial',32),placeholder_text="Summa")
    e.place(x=25,y=80)
    l=Label(master=a3,text="uyali aloqa",font=('Arial',22))
    l.place(x=320,y=25)
    v1=CTkButton(master=a3,width=250,corner_radius=32,text='Oldingi',command=h1)
    v1.place(x=25,y=180,)
def f3():

    a3=Toplevel()
    a3.title()
    a3.geometry('600x350')
    a3.configure(bg='black')

    def l9():

        plastik = e.get().strip()
        yil = e5.get().strip()
        Summa = e6.get().strip()
        if plastik and yil and Summa :
         r = askyesno(title='Xabar', message='Chek olasizmi')
         if r:
            showinfo(title='Xabar', message='To\'lov o\'tdi:\nplastik raqamiz:\n' + e.get() + '\nSumma:' + e6.get())

    l=Label(master=a3,text='Minimal: ''1 000',font=('Arial',22))
    l.place(x=340,y=30)
    l = Label(master=a3, text='Maksimal:  ''500 000', font=('Arial', 22))
    l.place(x=340, y=60)
    e=CTkEntry(master=a3,width=300,font=('Arial',32),placeholder_text="____ ____ ____ ____")
    e.place(x=25,y=30)
    e5=CTkEntry(master=a3,width=250,font=('Arial',32),placeholder_text="_/_")
    e5.place(x=25,y=100)
    e6=CTkEntry(master=a3,width=250,font=('Arial',32),placeholder_text="Summa")
    e6.place(x=25,y=170)
    v=CTkButton(master=a3,width=250,corner_radius=32,text='Oldingi',command=l9)
    v.place(x=25,y=240,)
def f():
    a2=Toplevel()
    a2.title()
    a2.geometry('700x500')
    a2.configure(bg='black')
    p=PhotoImage(file='Karta1.png')
    b=Button(master=a2,width=230,height=150,image=p,command=f1)
    b.image=p
    b.place(x=100,y=40)
    p1=PhotoImage(file='Karta.png')
    b1=Button(master=a2,width=230,height=150,image=p1,command=f3)
    b1.image=p1
    b1.place(x=400,y=40)
    l=Label(master=a2,text='Naqt pul',font=('Arial',32),bg='black',fg='white')
    l.place(x=140,y=200)
    l1 = CTkLabel(master=a2, text='Karta', font=('Arial', 42))
    l1.place(x=460, y=200)
a=CTk()
a.title()
a.geometry('700x500')
p3=PhotoImage(file='kompaniya2.png')
b=Button(master=a,command=f,image=p3)
b.pack(expand=True)
def Audio():
    if a:
        showinfo(title='Xabar',message='Xush kelibsiz')
Audio()
a.mainloop()