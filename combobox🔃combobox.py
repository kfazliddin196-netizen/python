from tkinter import *
from tkinter import ttk
a = Tk()
a.title()
a.geometry('500x500')
def f(event):
    s = b.get()
    if s== "Dushanba":
        b1['values'] = ["Tarix", "Ona-Tili",'Jismoniy','Chizma']
        b1.set('Dushanba')
    elif s == "Seshanba":
        b1.set('Seshanba')
        b1['values'] = ["Inglish-tili",'Matematika','geometriya','Adabiyot']
    elif s == "Chorshanba":
        b1.set('Chorshanba')
        b1['values'] = ["Infarmaika",'Jaxon-Tarix','Tarbiya','Huquq']
days = ['Dushanba', 'Seshanba', 'Chorshanba']
s2 = StringVar(value='Menyu')
b = ttk.Combobox(a, values=days, textvariable=s2)
b.place(x=30, y=30)
b.bind("<<ComboboxSelected>>", f)
b1 = ttk.Combobox(a)
b1.place(x=200, y=30)

a.mainloop()
