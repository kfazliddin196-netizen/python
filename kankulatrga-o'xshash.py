from tkinter import *
a=Tk()
a.title('dars')
a.geometry('400x700')
a.configure(bg='black')
def f1():
    e.delete(0,)
def q():
    e.delete(0,END)
def w():
    e.insert(END,'()')
def r():
    e.insert(END,'%')
def t():
    e.insert(END,'÷')
def y():
    e.insert(END,'7')
def u():
    e.insert(END,'8')
def i():
    e.insert(END,'9')
def o():
    e.insert(END,'x')
def p():
    e.insert(END,'4')
def s():
    e.insert(END,'5')
def f():
    e.insert(END,'6')
def g():
    e.insert(END,'–')
def h():
    e.insert(END,'1')
def j():
    e.insert(END,'2')
def k():
    e.insert(END,'3')
def z():
    e.insert(END,'+')
def x():
    e.insert(END,'+/–')
def v():
    e.insert(END,'0')
def n():
    e.insert(END,',')
def m():
    e.insert(END,'=')
e=Entry(width=50,bg='green')
e.place(x=55,y=50,height=150)
b=Button(width=5,height=2,fg='red',bg='black',text='C',command=q)
b.place(x=55,y=250)
b1=Button(width=5,height=2,text='()',bg='black',fg='red',command=w)
b1.place(x=135,y=250)
b2=Button(width=5,height=2,text='%',bg='black',fg='red',command=r)
b2.place(x=220,y=250)
b3=Button(width=5,height=2,text='÷',bg='black',fg='red',command=t)
b3.place(x=300,y=250)
b4=Button(width=5,height=2,text='7',bg='black',fg='red',command=y)
b4.place(x=55,y=320)
b5=Button(width=5,height=2,text='8',bg='black',fg='red',command=u)
b5.place(x=135,y=320)
b6=Button(width=5,height=2,text='9',bg='black',fg='red',command=i)
b6.place(x=220,y=320)
b7=Button(width=5,height=2,text='×',bg='black',fg='red',command=o)
b7.place(x=300,y=320)
d=Button(width=5,height=2,text='4',bg='black',fg='red',command=p)
d.place(x=55,y=390)
d1=Button(width=5,height=2,text='5',bg='black',fg='red',command=s)
d1.place(x=135,y=390)
d2=Button(width=5,height=2,text='6',bg='black',fg='red',command=f)
d2.place(x=220,y=390)
d3=Button(width=5,height=2,text='–',bg='black',fg='red',command=g)
d3.place(x=300,y=390)
d4=Button(width=5,height=2,text='1',bg='black',fg='red',command=h)
d4.place(x=55,y=460)
d5=Button(width=5,height=2,text='2',bg='black',fg='red',command=j)
d5.place(x=135,y=460)
d6=Button(width=5,height=2,text='3',bg='black',fg='red',command=k)
d6.place(x=220,y=460)
d7=Button(width=5,height=2,text='+',bg='black',fg='red',command=z)
d7.place(x=300,y=460)
c=Button(width=5,height=2,text='+/–',bg='black',fg='red',command=x)
c.place(x=55,y=530)
c1=Button(width=5,height=2,text='0',bg='black',fg='red',command=v)
c1.place(x=135,y=530)
c2=Button(width=5,height=2,text=',',bg='black',fg='red',command=n)
c2.place(x=220,y=530)
c3=Button(width=5,height=2,text='=',bg='black',fg='red',command=m)
c3.place(x=300,y=530)
m1=Button(width=6,height=1,text='⌂',bg='black',fg='red',command=f1)
m1.place(x=300,y=210)
a.mainloop()