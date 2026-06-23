from tkinter import *
from tkinter import ttk
a=Tk()
a.title('Fazliddin')
a.geometry('1000x1000')
a.configure(bg='black')
def P ():
   if d.get()=='Python':
      a.configure(bg='green')
b=['Python','java','C++','c#']
p=Variable(value='Salom')
d=ttk.Combobox(values=b,textvariable=p)
d.place(x=10,y=10)
f=ttk.Button(width=20,command=P)
f.pack(expand=1,)

a.mainloop()