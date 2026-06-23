from tkinter import *
from customtkinter import *

a = Tk()
a.title("Mening dasturim")
a.geometry('500x500')
a.configure(bg='black')
def q():
    t.delete('1.0', END)
    p = str(e.get()) * int(e1.get())
    g = str(e.get()) + "\n"  # sep \n qo'shildi
    t.insert(END, str(p) + g)

e = CTkEntry(master=a, width=125, placeholder_text='So\'z', placeholder_text_color='red')
e.place(x=10, y=10)

e1 = CTkEntry(master=a, width=125, placeholder_text='Son', placeholder_text_color='red')
e1.place(x=10, y=40)

t = Text(a, width=50, height=20)
t.pack(expand=1)

b = Button(a, width=10, height=1, text="Bosish", command=q)
b.place(y=20, x=145)

a.mainloop()