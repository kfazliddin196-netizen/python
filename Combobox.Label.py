from tkinter import *
from tkinter import ttk
a=Tk()
a.title("fimaya_me")
a.configure(bg="black")
a.geometry("1000x800")
def S ():
    if  c.get()=='Mevalar':
        l['text']='glos , olma , olcha , banan , qulupnay '
        a['bg']='blue'
    elif c.get()=='Notebook':
         l['text']='HpH , Acer , Lenova , Samsung , Asus'
         a['bg']='green'
    elif c.get()=='Suv':
         l['text']='Kola , Pepsi , Kavsar , sprayt , Fanta'
         a['bg']='yellow'
    elif c.get()=='Savsabotlar':
         l['text']='Savzi , Rediska , Kartoshka , Piyoz , Pamidor'
         a['bg']='red'
b=ttk.Button(width=20,command=S,text='Tanlang')
b.place(x=5,y=80)
l1=["Mevalar","Notebook","Suv","Savsabotlar",]
l=ttk.Label()
l.pack(anchor=NW,padx=6,pady=6)
c=ttk.Combobox(values=l1,)
c.pack(anchor=NW,pady=6,padx=6,)
a.mainloop()