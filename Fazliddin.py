from tkinter import *
a=Tk()
a.title('salom')
a.geometry('1000x800')
a.configure(bg='grey')
def t():
    l['bg']='red'
    b2['bg']='red'
def f():
    l['bg']='black'
    b3['bg']='black'
    b3['fg']='red'
def m():
    l['bg']='green'
    b4['bg']='green'
def c():
    l['bg']='blue'
    b1['bg']='blue'
def n():
    l['bg']='yellow'
    c['bg']='yellow'
def o():
    l['bg']='pink'
    d['bg']='pink'
def i():
    l['bg']='orange'
    d1['bg']='orange'
b1=Button(width=20,height=2,text='ko\'k',command=c)
b1.place(x=350,y=240)
b2=Button(width=20,height=2,text='qizil',command=t,)
b2.place(x=350,y=295)
l=Label(width=30,height=15,bg='black',fg='red')
l.place(x=100,y=100)
b3=Button(width=20,height=2,text='qora',command=f)
b3.place(x=100,y=350)
b4=Button(width=20,height=2,text='yashil',command=m)
b4.place(x=300,y=350)
c=Button(width=20,height=2,text='sariq',command=n)
c.place(x=350,y=185)
d=Button(width=20,height=2,text='pushti',command=o)
d.place(x=350,y=130)
d1=Button(width=20,height=2,text='olo\'vrang',command=i)
d1.place(x=140,y=50)
a.mainloop()