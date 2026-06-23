from tkinter import *
from tkinter import ttk
a = Tk()
a.title("dars")
a.configure(bg="blue")
a.geometry("1000x600")
def K():
    if e.get() == "Ertak kitoblar":
        l.insert(END,'Qalam va sichqon',)
        l.insert(END,'Kampir va bo\'ri',)
        l.insert(END,'Alochi xo\'zcha',)
        l.insert(END,'Baxtli hayot')
    elif e.get()=='Adabiy kitoblar':
        l.insert(END,'Dayus')
        l.insert(END,'Anor')
        l.insert(END,'Oq kema')
        l.insert(END,'Shum bola')
    elif e.get() == 'Qalam va sichqon':
       l.insert(END,'Qalam va sichqon')
    elif e.get() == 'Kampir va bo\'ri':
       l.insert(END,'Kampir va bo\'ri')
    elif e.get() == 'Alochi va xo\'rozcha':
       l.insert(END,'Alochi va xo\'rozcha')
    elif e.get() == 'Baxtli xayot':
       l.insert(END,'Baxtli xayot')
    elif e.get() == 'Dayus':
       l.insert(END,'Dayus')
    elif e.get() == 'Oq kema':
       l.insert(END,'Oq kema')
    elif e.get() == 'Shum bola':
       l.insert(END,'Shum bola')
    elif e.get() == 'Anor':
       l.insert(END,'Anor')
    else:
        l.insert(END, "hech narsa topilmadi")
def R():
    l.delete(0,END)
def Q():
    a=l.get(l.curselection())
    if a==('Qalam va sichqon'):
     M.insert(END,'Harid qildingiz')
    elif a == (1,):
     M.insert(END,'Harid qildingiz')
    elif a==(2,):
     M.insert(END,'Harid qildingiz')
    elif  a == (3,):
     M.insert(END, 'Harid qildingiz')
    elif  a == (4,):
     M.insert(END,'Harid qildingiz')
    elif  a == (5,):
     M.insert(END,'Harid qildingiz')
    elif a == (6,):
     M.insert(END,'Harid qildingiz')
    elif a == (7,):
     M.insert(END,'Harid qildingiz')
    elif a == (8,):
     M.insert(END, 'Harid qildingiz')
    elif a== (9,):
     M.insert(END,'Harid qildingiz')
    elif a==(10,):
     M.insert(END,'Harid qildingiz')
    elif a==(11,):
     M.insert(END,'Harid qildingiz')
    elif a==(12,):
     M.insert(END,'Harid qildingiz')
    elif a==(13,):
     M.insert(END,'Harid qildingiz')
    elif a == (14,):
     M.insert(END,'Harid qildingiz')
    elif a== (15,):
     M.insert(END,'Hard qildingiz')
    elif a== (16,):
     M.insert(END, 'Harid qildingiz')
    elif a== (17,):
     M.insert(END, 'Harid qildingiz')
    elif a==(18,):
     M.insert(END, 'Harid qildingiz')
    elif a == (19,):
     M.insert(END, 'Harid qildingiz')
    elif a== (20,):
     M.insert(END,'Harid qildingiz')
    elif a==(21,):
     M.insert(END,'Harid qildingiz')
def W():
   b=l.curselection()
   if b == (0,):
     M.insert(END,'Hariddingiz bekor qilindi')
   elif b==(1,):
     M.insert(END,'Hariddingiz bekor qilindi')
   elif b==(2,):
     M.insert(END,'Hariddingiz bekor qilindi')
   elif b==(3,):
     M.insert(END,'Hariddingiz bekor qilindi')
   if  b==(4,):
     M.insert(END,'Hariddingiz bekor qilindi')
   elif b==(5,):
     M.insert(END,'Hariddingiz bekor qilindi')
   elif b==(6,):
     M.insert(END,'Hariddingiz bekor qilindi')
   elif b==(7,):
       M.insert(END, 'Hariddingiz bekor qilindi')
   elif b==(8,):
       M.insert(END, 'Hariddingiz bekor qilindi')
   elif b==(9,):
       M.insert(END, 'Hariddingiz bekor qilindi')
   elif b==(10,):
       M.insert(END, 'Hariddingiz bekor qilindi')
   elif b==(11,):
       M.insert(END, 'Hariddingiz bekor qilindi')
   elif b==(12,):
       M.insert(END, 'Hariddingiz bekor qilindi')
   elif b==(13,):
       M.insert(END, 'Hariddingiz bekor qilindi')
   elif b==(14,):
       M.insert(END, 'Hariddingiz bekor qilindi')
   elif b==(15,):
       M.insert(END, 'Harddingiz bekor qilindi ')
   elif b==(16,):
       M.insert(END, 'Hariddingiz bekor qilindi')
   elif b==(17,):
       M.insert(END, 'Hariddingiz bekor qilindi')
   elif b==(18,):
       M.insert(END, 'Hariddingiz bekor qilindi')
   elif b==(19,):
       M.insert(END, 'Hariddingiz bekor qilindi')
   elif b==(20,):
       M.insert(END, 'Hariddingiz bekor qilindi')
   elif b==(21,):
       M.insert(END, 'Hariddingiz bekor qilindi')
def H():
    M.delete(0,END)
l1=["Ertak kitoblar",'Adabiy kitoblar']
I=Listbox(width=40,height=15,bg='green')
I.place(x=420,y=300)
l=Listbox(width=30,height=15,bg='black',fg='red')
l.place(x=300,y=8)
M=Listbox(width=30,height=15,bg='red',fg='black')
M.place(x=620,y=6)
q=ttk.Label(width=15,text='Harid qilasizmi')
q.place(x=500,y=30)
M1=ttk.Button(width=15,command=Q,text='OK')
M1.place(x=500,y=60)
M3=ttk.Button(width=15,command=H,text='O\'chirish')
M3.place(x=500,y=120)
M2=ttk.Button(width=15,command=W,text='NO')
M2.place(x=500,y=90)
I=ttk.Button(width=20,text='Narx')
I.place(anchor=NW,x=155,y=90)
b =ttk.Button(width=20, text="Qidrish",command=K)
b.place(anchor=NW,x=155,y=30)
f=ttk.Button(width=20,text='O\'chirish',command=R)
f.place(anchor=NW,x=155,y=60)
e = Entry(width=21)
e.place(anchor=NW,x=155,y=6)
d1=StringVar(value='Menyu')
d=ttk.Combobox(values=l1,textvariable=d1)
d.place(anchor=NW,x=6,y=6)
a.mainloop()