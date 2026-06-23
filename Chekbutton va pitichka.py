from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
a=Tk()
a.title('Checkbutton')
a.geometry('1000x700')
a.configure(bg='red')
def F():
    if d.get()==1:
        showinfo(title='info',message='yondi')
    else:
        showinfo(title='info',message='o\'chirish')
d=IntVar()
s=ttk.Checkbutton(text='yoqish',width=20,variable=d,command=F)
s.place(x=20,y=20)
a.mainloop()