from customtkinter import *
set_appearance_mode("dark")
a=CTk()
a.title()
a.geometry("500x500")
l=CTkLabel(master=a,
           text="text..",
           font=("Arial",50),
           text_color="red",
           bg_color="green")
def g ():
    l.configure(text="Salom")
b=CTkButton(master=a,
            text="bosma",
            corner_radius=32,
            fg_color="blue",
            hover_color="black"
,            border_color="yellow",
            border_width=2,command=g)
b.pack(pady=100)
l.place(x=250,y=250)
a.mainloop()