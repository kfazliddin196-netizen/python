from tkinter import *
from tkinter import ttk
a = Tk()
a.title("dars")
a.configure(bg="cyan")
a.geometry("1500x1500")
def F():
     a['bg']=e.get()
b =ttk.Button(width=15, text="Button", command=F)
b.place(x=500, y=150)
e = Entry(width=18)
e.place(x=500, y=50)
a.mainloop()