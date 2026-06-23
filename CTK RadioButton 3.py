from customtkinter import *
a=CTk()
a.title("qwertyuiop[]")
a.geometry('700x700')
def hhh():
    l.configure(text=g.get())
l=CTkLabel(master=a,text='Tanlang')
l.place(x=100,y=70)
g=StringVar()
r=CTkRadioButton(master=a,
                 text='Yes,I do',
                 text_color="red",
                 border_color="green",
                 variable=g,
                 hover_color="red",
                 command=hhh)
r.place(x=100,y=100)
t=CTkRadioButton(master=a,
                 text="No,I don't",
                 text_color="red",
                 border_color="green",
                 variable=g,
                 hover_color="red",
                 command=hhh)
t.place(x=100,y=140)
y=CTkRadioButton(master=a,
                 text='Hello',
                 text_color="red",
                 border_color="green",
                 variable=g,
                 hover_color="red",
                 command=hhh)
y.place(x=100,y=180)
a.mainloop()