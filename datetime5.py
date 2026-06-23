from tkinter import *
import datetime
a=Tk()
a.title()
a.geometry('500x500')
now=datetime.date.today()
l=Label(width=10,height=10,text=now)
l.pack(expand=1)
a.mainloop()