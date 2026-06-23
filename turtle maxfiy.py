from tkinter import *
import random
a=Tk()
a.geometry('1000x1000')
a.configure(bg='black')
c= Canvas(bg="white", width=1000, height=1000)
c.pack(anchor=CENTER, expand=1)
c.configure(bg='black')
def ch ():
    c.delete('red')
    for i in range(5):
     x1=random.randint(10,700)
     y1=random.randint(10,300)
     x=x1+70
     y=y1+70
     c.create_oval(x1,y1,x,y,fill='blue',outline='blue',tags='red')
def sh ():
    c.delete('red')
    for i in range(5):
     x2=random.randint(10,700)
     y2=random.randint(10,300)
     x3=x2+70
     y3=y2+70
     c.create_oval(x2,y2,x3,y3,fill='red',outline='red',tags='red')
b = Button(width=10, height=2, bg='blue',command=ch)
b.place(x=550, y=500)
b1 = Button(width=10, height=2, bg='red',command=sh)
b1.place(x=450, y=500)
a.mainloop()
