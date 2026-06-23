from tkinter import *
from tkinter import ttk
a=Tk()
a.title("fimaya_me")
a.configure(bg="red")
a.geometry("700x500")
def D ():
    d.delete(0,END)
def S ():
    if c.get()=='Mevalar':
       d.insert(END,'Glos')
       d.insert(END,'Olcha')
       d.insert(END,'Uzum')
       d.insert(END,'Olma')
       d.insert(END,'O\'rik')
    elif c.get()=='Notebook':
       d.insert(END,'HpH')
       d.insert(END,'Acer')
       d.insert(END,'Asus')
       d.insert(END,'Samsung')
       d.insert(END,'Lenova')
    elif c.get()=='Savzavotlar':
       d.insert(END, 'Piyoz')
       d.insert(END,'Sabzi')
       d.insert(END,'Kartoshka')
       d.insert(END,'Rediska')
       d.insert(END,'Baqalojon' )
    elif c.get()=='Suv':
       d.insert(END,'Ko\'la')
       d.insert(END,'Pepsi')
       d.insert(END,'Fanta')
       d.insert(END,'Sprayt')
       d.insert(END,'Gdralayt')
def K():
    g=d.get(d.curselection())
    if g=='Glos':
     a.configure(bg='green')  # Orqa fonni o'zgartirish
    elif g=='Olcha':
     a.configure(bg='red')
    elif g=='Uzum':
     a.configure(bg='yellow')
    elif g=='Olma':
     a.configure(bg='blue')
    elif g=='O\'rik':
     a.configure(bg='black')
d=Listbox(width=30,height=15)
d.place(x=300,y=8)
b=ttk.Button(width=20,command=K,text='O\'chirish')
b.place(anchor=NW,x=150,y=40)
b=ttk.Button(width=20,command=S,text='Tanlang')
b.place(anchor=NW, x=150,y=6)
l1=["Mevalar","Notebook","Savzavotlar","Suv"]
l2=StringVar(value='Menyu')
c=ttk.Combobox(textvariable=l2,values=l1,)
c.pack(anchor=NW,pady=6,padx=6,)
a.mainloop()