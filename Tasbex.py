from tkinter import *
from tkinter import ttk
b= Tk()
b.title()
b.configure(bg='red')
b.geometry("1000x1000")
a = 0
def c():
    global a
    a += 1
    g["text"] = a
def h():
    global a
    a=0
    g['text']=''
d=PhotoImage(file='2023.png')
l=Label(bd=5,image=d)
l.pack(expand=1,pady=100)
g=Label(bg='#DFDFDD',)
g.place(x=555,y=367)
s = ttk.Button(text="Tasbeh", command=c,)
s.place(x=600,y=550)
s = ttk.Button(text="qayta bowlaw", command=h,)
s.place(x=325,y=550)
b.mainloop()