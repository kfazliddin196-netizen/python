from customtkinter import *
a=CTk()
a.title()
a.geometry('500x500')
def f():
    p.step()
    l.configure(text=(int(p.get()*101)))
p=CTkProgressBar(master=a,orientation='orizontal',
                 determinate_speed=0.5)
def f1():
    p.start()
def f2():
    p.stop()
p.place(x=10,y=20)
l=CTkLabel(master=a,text='')
l.place(x=10,y=50)
b=CTkButton(master=a,text='1+',command=f)
b.place(x=10,y=100)
b1=CTkButton(master=a,text='start',command=f1)
b1.place(x=10,y=150)
p.set(0)
b2=CTkButton(master=a,text='stop',command=f2)
b2.place(x=10,y=200)
a.mainloop()