from tkinter import *
a=Tk()
a.geometry('500x500')
a.configure(bg='black')
def j():
    if e.get()=="Admin" and e1.get()=='Admin':
        l.config(text="Parol tog'ri")
    else:
        l.config(text="Parol noto'g'ri")
l=Label(width=50,height=10)
l.pack(expand=1)
e=Entry()
e.place(x=70,y=350)
e1=Entry()
e1.place(x=280,y=350)
b=Button(width=15,height=1,text='Ulanish',command=j)
b.place(x=190,y=400)
a.mainloop()