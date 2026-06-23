from  tkinter import *
from  tkinter import ttk
a=Tk()
s=StringVar()
b=['Pyton','JavaScript','C#','Java','C++']
l=ttk.Label(textvariable=s)
l.place(x=10,y=50)
s1=ttk.Spinbox(textvariable=s,values=b)
s1.pack(anchor=NW)
a.mainloop()