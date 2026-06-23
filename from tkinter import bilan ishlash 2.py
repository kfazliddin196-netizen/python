from tkinter import *
a=Tk()
a.title('2-dars')
a.geometry('1000x700')
a.configure(bg='grey')
def qizil():
    b['fg']='red'
    l['bg']='red'
def yashil():
    b1['fg']='green'
    l1['bg']='green'
def olorang():
    b2['fg']='orange'
    l2['bg']='orange'
def text():
    l['text']='qizil'
def text1():
    l1['text']='yashil'
def text2():
    l2['text']='olo\'vrang'
def kok():
    a3['fg']='blue'
    l3['bg']='blue'
def text3():
    l3['text']='ko\'k'
l=Label(width=20,height=10,)
l.place(x=100,y=100)
l1=Label(width=20,height=10)
l1.place(x=300,y=100)
l2=Label(width=20,height=10)
l2.place(x=500,y=100)
l3=Label(width=20,height=10)
l3.place(x=700,y=100)
b=Button(width=20,height=2,text='1-tugma',command=qizil)
b.place(x=100,y=275)
b1=Button(width=20,height=2,text='2-tugma',command=yashil)
b1.place(x=300,y=275)
b2=Button(width=20,height=2,text='3-tugma',command=olorang)
b2.place(x=500,y=275)
a=Button(width=20,height=2,text='4-tugma',command=text)
a.place(x=100,y=350)
a1=Button(width=20,height=2,text='5-tugma',command=text1)
a1.place(x=300,y=350)
a2=Button(width=20,height=2,text='6-tugma',command=text2)
a2.place(x=500,y=350)
a3=Button(width=20,height=2,text='7-tugma',command=kok)
a3.place(x=700,y=275)
a4=Button(width=20,height=2,text='8-tugma',command=text3)
a4.place(x=700,y=350)
a.mainloop()