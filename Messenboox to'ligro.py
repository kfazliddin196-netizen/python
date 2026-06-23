from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo,showerror
a=Tk()
a.title()
a.geometry('400x500')
a.configure(bg='red')
def R ():
 if e.get() =="Komilov":
  if b.get() == "Fazliddin":
   if d.get() == "kfazliddin196@gmail.com":
    if c.get() == '7777':
         showinfo(title="Xabar", message="Ro\'yxatdan o\'tingiz")
# .......................................................................................
 if e.get() != "Komilov" and c.get() != '7777':
      showerror(title='Xabar', message="Familya va parol xato")
 elif b.get() != "Fazliddin" and d.get() != "kfazliddin196@gmail.com":
            showerror(title='Xabar', message='Ism va gmail xato')
 elif e.get() != "Komilov" and d.get() != "kfazliddin196@gmail.com":
            showerror(title='Xabar', message='Familya va gmail xato')
 elif b.get() != 'Fazliddin' and c.get() != '7777':
       showerror(title='Xabar', message='Ism va Paro\'l xato')
 elif d.get() != "kfazliddin196@gmail.com" and c.get() != '7777':
            showerror(title='Xabar', message='gmail va Paro\'l xato')
 elif e.get() != "Komilov" and b.get() != "Fazliddin":
            showerror(title='Xabar', message='Ism va Familya xato')
 elif e.get() != "Komilov":
            showerror(title='Xabar', message="Familya xato")
 elif c.get() != '7777':
            showerror(title='Xabar', message="Parol xato")
 elif b.get() != "Fazliddin":
            showerror(title='Xabar', message="Ism xato")
 elif d.get() != "kfazliddin196@gmail.com":
           showerror(title='Xabar', message="Gmail xato")
# ..............................................................................................
 if e.get() != "Komilov":
            showerror(title='Xabar', message='Ro\'yxatdan o\'tmadiz')
 elif b.get() != "Fazliddin":
            showerror(title='Xabar', message='Ro\'yxatdan o\'tmadiz')
 elif d.get() != "kfazliddin196@gmail.com":
            showerror(title='Xabar', message='Ro\'yxatdan o\'tmadiz')
 elif c.get() != '7777':
            showerror(title='Xabar', message='Ro\'yxatdan o\'tmadiz')
m12=ttk.Button(width=20,text='Ro\'yxatdan o\'tish',command=R)
m12.place(x=150,y=300)
l=Label(width=17,text='Familya',bg='red')
l.place(x=150,y=77)
e=ttk.Entry(width=20)
e.place(x=150,y=100)
l=Label(width=17,text='Ism',bg='red')
l.place(x=150,y=127)
b=ttk.Entry(width=20)
b.place(x=150,y=150)
l=Label(width=17,text='Gmail',bg='red')
l.place(x=150,y=177)
d=ttk.Entry(width=20)
d.place(x=150,y=200)
l=Label(width=17,text='Paro\'l',bg='red')
l.place(x=150,y=227)
c=ttk.Entry(width=20,show='*')
c.place(x=150,y=250)
a.mainloop()
