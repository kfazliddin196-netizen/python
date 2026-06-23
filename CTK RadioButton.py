from customtkinter import *
a=CTk()
a.title("qwertyuiop[]")
a.geometry('700x700')
def h():
    l.configure(text=" JAVOB UCHUN RAXMAT")
l=CTkLabel(master=a,text='siz pitsani yaxshi korasizmi')
l.place(x=100,y=70)
b=CTkButton(master=a,command=h)
b.place(x=100,y=170)
g=StringVar()
r=CTkRadioButton(master=a,
                 text='ha',
                 text_color="red",
                 border_color="green",
                 bg_color="yellow",
                 variable=g,
                 hover_color="red",
                 )
r.place(x=100,y=100)
t=CTkRadioButton(master=a,
                 text='yoq',
                 text_color="black",
                 border_color="red",
                 bg_color="green",
                 variable=g,
                 hover_color="yellow",
                 )
t.place(x=100,y=140)
a.mainloop()