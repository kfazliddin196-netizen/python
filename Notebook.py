from tkinter import *
from tkinter import ttk
a=Tk()
a.title('Menyu')
a.geometry('500x500')
def D():
    a['bg']='red'
n=ttk.Notebook()
n.pack(expand=True, fill=BOTH,)
f1=ttk.Frame(n)
f1.pack(fill=BOTH,expand=True)
f2=ttk.Frame(n)
f2.pack(fill=BOTH,expand=True)
n.add(f1,text='Python')
n.add(f2,text='Java')
a.mainloop()