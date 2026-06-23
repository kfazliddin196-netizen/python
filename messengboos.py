from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
a=Tk()
a.title()
a.geometry('900x800')
a.configure(bg='red')
def f():
   if e.get() !="Komilov":
      showinfo(title='Xabar',message='Familya xato')
   elif b.get() != "Fazliddin":
       showinfo(title='Xabar',message='Ism xato')
   elif d.get() != "kfazliddin196@gmail.com":
         showinfo(title='Xabar',message='gmail xato')
   elif c.get() != '7777':
          showinfo(title='Xabar',message='Paro\'l xato')
   if e.get() != "Komilov":
       showinfo(title='Xabar', message='Ro\'yxatdan o\'tmadiz')
   elif b.get() != "Fazliddin":
       showinfo(title='Xabar', message='Ro\'yxatdan o\'tmadiz')
   elif d.get() != "kfazliddin196@gmail.com":
       showinfo(title='Xabar', message='Ro\'yxatdan o\'tmadiz')
   elif c.get() != '7777':
       showinfo(title='Xabar', message='Ro\'yxatdan o\'tmadiz')

   if c.get()=='7777':
     if  e.get() =="Komilov":
       if b.get() == "Fazliddin":
        if d.get() == "kfazliddin196@gmail.com":
          if c.get() == '7777':
              showinfo("Xabar", "Ro\'yxatdan o\'tingiz")
m=ttk.Button(width=20,text='Ro\'yxatdan o\'tish',command=f)
m.place(x=400,y=300)
l=ttk.Label(width=20,text='Familya')
l.place(x=400,y=80,height=21)
e=ttk.Entry(width=20,show='*')
e.place(x=400,y=100)
b=ttk.Entry(width=20,show='*')
b.place(x=400,y=150)
d=ttk.Entry(width=20,show='*')
d.place(x=400,y=200)
c=ttk.Entry(width=20,show='*')
c.place(x=400,y=250)
a.mainloop()
