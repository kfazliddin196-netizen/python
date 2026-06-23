from customtkinter import *
from tkinter import *
import pyttsx3
e=pyttsx3.init()
from tkinter import ttk
from tkinter.messagebox import askyesno,showinfo
def f1():
    a3=Toplevel()
    a3.title()
    a3.geometry('500x450')

    e=CTkEntry(master=a3,width=250,font=('Arial',32),placeholder_text="_ ___ __ ___ __ __")
    e.place(x=25,y=10)
    l=Label(master=a3,text="uyali aloqa",font=('Arial',22))
    l.place(x=320,y=25)
    def m():
        e.insert(END,'1')
    def m1():
        e.insert(END,'2')
    def m2():
        e.insert(END,'3')
    def m3():
        e.insert(END,'4')
    def m4():
        e.insert(END,'5')
    def m5():
        e.insert(END,'6')
    def m6():
        e.insert(END, '7')
    def m7():
        e.insert(END, '8')
    def m8():
        e.insert(END, '9')
    def m9():
        e.insert(END, '0')
    def m10():
        e.delete(0)
    def m11():
        e.delete(0,END)
    b4 = Button(master=a3, width=5, height=2, text='7', bg='black', fg='red',command=m6 )
    b4.place(x=300, y=100)
    b5 = Button(master=a3, width=5, height=2, text='8', bg='black', fg='red',command=m7 )
    b5.place(x=370, y=100)
    b6 = Button(master=a3, width=5, height=2, text='9', bg='black', fg='red',command=m8 )
    b6.place(x=440, y=100)
    d = Button(master=a3,width=5, height=2, text='4', bg='black', fg='red',command=m3 )
    d.place(x=300, y=170)
    d1 = Button(master=a3,width=5, height=2, text='5', bg='black', fg='red',command=m4)
    d1.place(x=370, y=170),
    d2 = Button(master=a3,width=5, height=2, text='6', bg='black', fg='red',command=m5)
    d2.place(x=440, y=170)
    d4 = Button(master=a3, width=5, height=2, text='1', bg='black', fg='red', command=m)
    d4.place(x=300, y=240)
    d5 = Button(master=a3, width=5, height=2, text='2', bg='black', fg='red', command=m1)
    d5.place(x=370, y=240)
    d6 = Button(master=a3, width=5, height=2, text='3', bg='black', fg='red', command=m2)
    d6.place(x=440, y=240)
    c1 = Button(master=a3, width=5, height=2, text='0', bg='black', fg='red', command=m9)
    c1.place(x=370, y=310)
    b7 = Button(master=a3,width=5, height=2, text='x', bg='black', fg='red', command=m10)
    b7.place(x=300, y=310)
    b7 = Button(master=a3,width=5, height=2, text='⌂', bg='black', fg='red', command=m11)
    b7.place(x=440, y=310)
def f3():
    a3=Toplevel()
    a3.title()
    a3.geometry('500x450')
    e=CTkEntry(master=a3,width=250,font=('Arial',32),placeholder_text="_ ___ __ ___ __ __")
    e.place(x=25,y=30)
    e5=CTkEntry(master=a3,width=250,font=('Arial',32),placeholder_text="_/_")
    e5.place(x=25,y=100)
    e6=CTkEntry(master=a3,width=250,font=('Arial',32),placeholder_text="Summa")
    e6.place(x=25,y=170)
    l=Label(master=a3,text="uyali aloqa",font=('Arial',22))
    l.place(x=320,y=25)
    def m():
        e.insert(END,'1')
    def m1():
        e.insert(END,'2')
    def m2():
        e.insert(END,'3')
    def m3():
        e.insert(END,'4')
    def m4():
        e.insert(END,'5')
    def m5():
        e.insert(END,'6')
    def m6():
        e.insert(END, '7')
    def m7():
        e.insert(END, '8')
    def m8():
        e.insert(END, '9')
    def m9():
        e.insert(END, '0')
    def m10():
        e.delete(0)
    def m11():
        e.delete(0,END)
    def f1():
        e5.insert(END,'1')
    b4 = Button(master=a3, width=5, height=2, text='7', bg='black', fg='red',command=m6 or f1 )
    b4.place(x=300, y=100)
    b5 = Button(master=a3, width=5, height=2, text='8', bg='black', fg='red',command=m7 )
    b5.place(x=370, y=100)
    b6 = Button(master=a3, width=5, height=2, text='9', bg='black', fg='red',command=m8 )
    b6.place(x=440, y=100)
    d = Button(master=a3,width=5, height=2, text='4', bg='black', fg='red',command=m3 )
    d.place(x=300, y=170)
    d1 = Button(master=a3,width=5, height=2, text='5', bg='black', fg='red',command=m4)
    d1.place(x=370, y=170),
    d2 = Button(master=a3,width=5, height=2, text='6', bg='black', fg='red',command=m5)
    d2.place(x=440, y=170)
    d4 = Button(master=a3, width=5, height=2, text='1', bg='black', fg='red', command=m)
    d4.place(x=300, y=240)
    d5 = Button(master=a3, width=5, height=2, text='2', bg='black', fg='red', command=m1)
    d5.place(x=370, y=240)
    d6 = Button(master=a3, width=5, height=2, text='3', bg='black', fg='red', command=m2)
    d6.place(x=440, y=240)
    c1 = Button(master=a3, width=5, height=2, text='0', bg='black', fg='red', command=m9)
    c1.place(x=370, y=310)
    b7 = Button(master=a3,width=5, height=2, text='x', bg='black', fg='red', command=m10)
    b7.place(x=300, y=310)
    b7 = Button(master=a3,width=5, height=2, text='⌂', bg='black', fg='red', command=m11)
    b7.place(x=440, y=310)

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
    e.say('хуш келибсиз')
    e.runAndWait()
    if a:
        showinfo(title='Xabar',message='Xush kelibsiz')
Audio()
a.mainloop()
