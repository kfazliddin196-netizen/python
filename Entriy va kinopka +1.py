from tkinter import *
a=Tk()
a.title()
a.geometry('600x400')
a.configure(bg='black')
a1=0
def f():
    global a1
    a1 +=1
    e.insert(END,a1)
b=Button(width=15,height=2,bg='red',text='tugma',command=f)
b.place(x=250,y=200)
e=Entry(width=15,bg='blue')
e.place(x=250,y=50)
a.mainloop()