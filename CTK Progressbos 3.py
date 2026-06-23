from customtkinter import *
a=CTk()
a.title()
a.geometry('500x500')
def G():
    p.start()
s=CTkButton(master=a,text='To\'ldirish',command=G,)
s.place(x=10,y=100)
p=CTkProgressBar(master=a,orientation='horizontal',
                 determinate_speed=0.5)
p.place(x=10,y=10)
p.set(0)
l=CTkLabel(master=a,text='')
l.place(x=10,y=50)
a.mainloop()