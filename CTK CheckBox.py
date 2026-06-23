from customtkinter import *
a=CTk()
a.title('tkinter')
a.geometry('500x500')
def c():
    l2.configure(text='ha')
c1=StringVar(value='off')
l=CTkCheckBox(master=a,text='Siz dasturchimisiz?',variable=c1,
                  onvalue='on',offvalue='off',command=c)
l.place(x=10,y=10)
l2=CTkLabel(master=a,
            text='text..',
            font=('Arial',25),
            text_color='red')
l.pack()
a.mainloop()