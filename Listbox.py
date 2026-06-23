from tkinter import *
a=Tk()
a.title()
a.geometry('1000x700')
a.configure(bg='red')
def F():
    a=l.get(l.curselection())
    if a=='Qalam':
     l1.insert(END,1000)
m=['Qalam','Ruchka']
v=Variable(value=m)
b=Button(width=20,height=2,command=F)
b.place(x=300,y=400)
l=Listbox(width=30,height=15,listvariable=v)
l.place(x=100,y=100)
l1=Listbox(width=30,height=15)
l1.place(x=500,y=100)
a.mainloop()