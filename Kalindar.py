from tkinter import *
from customtkinter import *
a=Tk()
a.title('Kalindar')
a.geometry('400x400')
a.configure(bg='red')
def f():
    import calendar
    a=int(e.get())
    b=int(e.get())
    l['text']=(calendar.month(a,b))
e=CTkEntry(master=a,placeholder_text='Oy')
e.place(x=250,y=50)
e1=CTkEntry(master=a,placeholder_text='Yil')
e1.place(x=250,y=100)
l=Label(width=20,height=10)
l.place(x=200,y=200)
b=Button(width=7,height=1,command=f)
b.place(x=170,y=80)
a.mainloop()