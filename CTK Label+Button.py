from customtkinter import *
set_appearance_mode('dark')
a=CTk()
a.geometry("500x500")
def f():
    c.configure(text='Komilov')
def g():
    c1.configure(text='Fazliddin')
def g1():
    c2.configure(text='16 yosh')
c=CTkLabel(master=a,
           text="            ",
           corner_radius=32)
c.place(x=100,y=100)
c1=CTkLabel(master=a, text="        ",
           corner_radius=32)
c1.place(x=200,y=100)
c2=CTkLabel(master=a, text="         ",
           corner_radius=32)
c2.place(x=300,y=100)
b=CTkButton(master=a,text='Familya',
            corner_radius=32,
            border_width=1,
            height=20,width=10,command=f)
b.place(x=100,y=270)
b1=CTkButton(master=a,text='ism',
            corner_radius=32,
             height=20,width=10,
             command=g)
b1.place(x=200,y=270)
b2=CTkButton(master=a,text='Yosh',
            corner_radius=32,
             height=20,width=10,
             command=g1)
b2.place(x=300,y=270)
a.mainloop()