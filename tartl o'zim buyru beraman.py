from tkinter import *
from tkinter import ttk
import turtle

def clear():
    a1.clear()
    c.clear()


def create():
    global a1, c
    a1 = turtle.Screen()
    c = turtle.Turtle()
    a1.setup(800, 700)

a = Tk()
a.geometry('200x600')

# To'g'riga
def m():
    d = int(e1.get())
    c.down()
    c.forward(d)
    c.up()

# Chapga
def t():
    a = int(e3.get())
    c.down()
    c.left(a)
    c.up()

# O'ngga
def u():
    a = int(e4.get())
    c.down()
    c.right(a)
    c.up()

# Doira
def F():
    r = int(e5.get())
    r1 = int(e6.get())
    c.down()
    c.circle(r, r1)
    c.up()

def T():
    clear()
    create()

# Turtle joyini o'zgarish
def L():
    x = int(e7.get())
    y = int(e8.get())
    c.up()
    c.goto(x, y)
    c.down()
def P1():
    k=str(e9.get())
    c.end_fill()
    c.color(k)
    c.begin_fill()
e1=Entry(width=20)
e1.place(x=35, y=70)
b1=ttk.Button(width=20, text="To'g'riga", command=m)
b1.place(x=35, y=100)
e3=Entry(width=20)
e3.place(x=35, y=130)
b3=ttk.Button(width=20, text="Chapga", command=t)
b3.place(x=35, y=160)
e4=Entry(width=20)
e4.place(x=35, y=190)
b4=ttk.Button(width=20, text="O'ngga", command=u)
b4.place(x=35, y=220)
e5=Entry(width=20)
e5.place(x=35, y=250)
b5=ttk.Button(width=20, text='Aylana', command=F)
b5.place(x=35, y=310)
e6=Entry(width=20)
e6.place(x=35, y=280)
e7=Entry(width=20)
e7.place(x=35, y=340)
e8=Entry(width=20)
e8.place(x=35, y=370)
b7=ttk.Button(width=20, command=L, text='Turtle boshqaruvi')
b7.place(x=35, y=400)
e9=Entry(width=20)
e9.place(x=35, y=430)
b8=ttk.Button(width=20,text='rang',command=P1,)
b8.place(x=35, y=460)
b6=ttk.Button(width=20, text='O\'chirish', command=T)
b6.place(x=35, y=500)
create()
a.mainloop()