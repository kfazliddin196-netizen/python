from tkinter import *
import random
a=Tk()
a.title('rendom')
a.geometry('1000x800')
a.configure(bg='grey')
def F():
     m=['qulupnay','olcha','olma','uzum','glos','o\'rik',]
     n=random.choice(m)
     l['text']=n
     l['fg']='red'
l=Label(width=20,height=10,bg='black',fg='red')
l.place(x=200,y=100,)
b=Button(width=20,height=2,text='so\'z',bg='black',fg='red',command=F,)
b.place(x=200,y=300)
a.mainloop()