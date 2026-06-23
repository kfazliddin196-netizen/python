from customtkinter import *
a=CTk()
a.title('')
a.geometry('500x500')
def P():
    b.configure(text='Hello')
b=CTkButton(master=a,hover_color='red',
            corner_radius=42,
            text_color='blue',
            text='Salom',
            fg_color='yellow',command=P)
b.place(x=10,y=10)
a.mainloop()
