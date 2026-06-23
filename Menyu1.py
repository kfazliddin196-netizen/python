from tkinter import *
a=Tk()
a.title('Menyu')
a.geometry('300x300')
a.configure(bg='red')
a.option_add('tearOFF',FALSE)
def W():
     a['bg']='black'
def D():
     a['bg']='blue'
def F():
     a['bg']='green'
def S():
     a['bg']='yellow'
def A():
     a['bg']='red'
b=Menu()
c=Menu()
s=Menu()
s.add_command(label='Save',command=W)
s.add_command(label='Open')
c.add_cascade(label='Settings',menu=s)
c.add_separator()
c.add_cascade(label='Blue',command=D)
c.add_cascade(label='green',command=F)
c.add_separator()
c.add_cascade(label='Exit',command=A)
b.add_cascade(label='File',menu=c,)
b.add_cascade(label='Edit',command=S)
a.config(menu=b)
a.mainloop()