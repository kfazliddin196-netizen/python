from tkinter import *
a=Tk()
a.title('F')
a.geometry('1000x800')
a.configure(bg='grey')
def x():
    l['text']=e.get()
e=Entry(width=35,bg='green')
e.place(x=400,y=100)
l=Label(width=30,height=10,bg='black',fg='red',)
l.place(x=400,y=200)
b=Button(width=30, height=2,text='so\'z',fg='red',bg='black',command=x)
b.place(x=400,y=400)
a.mainloop()
