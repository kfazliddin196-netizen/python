from customtkinter import *
from tkinter import *
a=CTk()
a.title('')
a.geometry('500x500')
def k():
    l.delete(0, END)
    l.insert(END, 'Olma')
    l.insert(END, 'olcha')
    l.insert(END, 'glos')
    l.insert(END, 'Uzum')
def j():
    l.delete(0, END)
    l.insert(END, 'Iphone')
    l.insert(END, 'Redmi')
    l.insert(END, 'Samsung')
    l.insert(END, 'Realmi')
def j1():
    l.delete(0,END)
    l.insert(END,'Hp')
    l.insert(END,'Acer')
    l.insert(END,'Asus')
    l.insert(END,'Lenova')
f=CTkScrollableFrame(master=a,label_text='Menyu',
                     label_fg_color='green',
                     border_width=5,border_color='red',
                     width=200,height=180)
f.place(x=10,y=10)
b=CTkButton(master=f,text='Mevalar',hover_color='red',corner_radius=32,command=k)
b.pack(pady=5)
b1=CTkButton(master=f,text='Smartfonlar',hover_color='red',corner_radius=32,command=j)
b1.pack(pady=5)
b3=CTkButton(master=f,text='Notebook',hover_color='red',corner_radius=32,command=j1)
b3.pack(pady=5)
l=Listbox(master=a,width=20,height=10,bg='green')
l.place(x=300,y=10)
a.mainloop()