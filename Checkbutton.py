from tkinter import *
from tkinter import ttk
a=Tk()
a.title()
a.geometry('1000x800')
a.configure(bg='red')
b=ttk.Checkbutton(width=10)
b.place(x=100,y=100)
a.mainloop()