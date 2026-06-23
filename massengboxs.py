from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
a=Tk()
a.title()
a.geometry('1000x800')
a.configure(bg='red')
def U():
    if e.get()=='1111':
        showinfo(title='Javobi',message='to\'g\'ri')
    else:
        showinfo(title='Javobi',message='Noto\'g\'ri')
e=Entry(width=20)
e.pack(anchor=NW)
b=ttk.Button(width=20,command=U)
b.pack(expand=True)
a.mainloop()