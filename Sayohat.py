from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import ttk
a=Tk()
a.title()
a.geometry('400x400')
a.configure(bg='black')
def M1():
  if e.get() == "Komilov" and b.get() == "Fazliddin" and d.get() == "kfazliddin196@gmail.com" and c.get() == '7777':
    showinfo(title="Xabar", message="Ro\'yxatdan o\'tingiz")
    d1 = Tk()
    d1.title()
    d1.geometry('700x300')
    d1.configure(bg='black')
    b1 = ['Python', 'java', 'C++', 'c#']
    d2 = ttk.Combobox(d1,values=b1)
    d2.place(x=100, y=150)
    d3=ttk.Combobox(d1,values=b1)
    d3.place(x=300,y=150)
    d3=ttk.Combobox(d1,values=b1)
    d3.place(x=500,y=150)
m=ttk.Button(width=20,text='Ro\'yxatdan o\'tish',command=M1)
m.place(x=136,y=300)
l=ttk.Label(width=20,text='Familya')
l.place(x=136,y=80,height=21)
e = ttk.Entry(width=20)
e.place(x=136, y=100)
b=ttk.Entry(width=20)
b.place(x=136,y=150)
d=ttk.Entry(width=20)
d.place(x=136,y=200)
c=ttk.Entry(width=20)
c.place(x=136,y=250)
a.mainloop()