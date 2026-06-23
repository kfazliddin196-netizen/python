from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
a=Tk()
a.title()
a.geometry('1000x1000')
a.configure(bg='black')
def R():
    if e.get() == 'Oziq ovqat':
        l.insert(END, 'Sir')
        l.insert(END, 'Kalbasa')
        l.insert(END, 'Kartoshka')
        l.insert(END, 'Makarom')
    elif e.get() == 'Notebook':
        l.insert(END, 'Hp')
        l.insert(END, 'Acer')
        l.insert(END, 'Asus')
        l.insert(END, 'Lenova')
    elif e.get() == 'Suv':
        l.insert(END, 'Ko\'la')
        l.insert(END, 'Pepsi')
        l.insert(END, 'Fanta')
    elif e.get() == 'Sir':
        l.insert(END, 'Sir')
    elif e.get() == 'Kalbasa':
        l.insert(END, 'Kalbasa')
    elif e.get() == 'Kartoshka':
        l.insert(END, 'Kartoshka')
    elif e.get() == 'Makarom':
        l.insert(END, 'Makarom')
    elif e.get() == 'Hp':
        l.insert(END, 'Hp')
    elif e.get() == 'Acer':
        l.insert(END, 'Acer')
    elif e.get() == 'Lenova':
        l.insert(END, 'Lenova')
    elif e.get() == 'Ko\'la':
        l.insert(END, 'Ko\'la')
    elif e.get() == 'Pepsi':
        l.insert(END, 'Pepsi')
    elif e.get() == 'Fanta':
        l.insert(END, 'Fanta')
    else:
        l.insert(END,'Xech narsa topilmadi')
def o():
    if c.get() == 'Oziq ovqat':
        l.insert(END, 'Sir')
        l.insert(END, 'Kalbasa')
        l.insert(END, 'Kartoshka')
        l.insert(END, 'Makarom')
    elif c.get() == 'Notebook':
        l.insert(END, 'Hp')
        l.insert(END, 'Acer')
        l.insert(END, 'Asus')
        l.insert(END, 'Lenova')
    elif c.get() == 'Suv':
        l.insert(END, 'Ko\'la')
        l.insert(END, 'Pepsi')
        l.insert(END, 'Fanta')
def P():
    l.delete(0,END)
    p.delete(0,END)
    b.delete(0,END)
def G():
    s= l.get(l.curselection())
    if s=='Sir':
     b.insert(END,'Sir Chiqazilgan sana 2021/01/21 Saqlanish muddati tugashi,2023/12/11')
    elif s=='Kalbasa':
     b.insert(END,' Kalbasasi Chiqazilgan sana 2022/01/21 Saqlanish muddati tugashi,2024/12/11')
    elif s=='Kartoshka':
     b.insert(END,'Russia Kartoshkasi')
    elif s=='Makarom':
     b.insert(END,'Russia Makaromi Chiqazilgan sana 2021/01/21 Saqlanish muddati tugashi,2025/12/11')
    elif s=='Hp':
     b.insert(END,'Hp yili 2023 2 kullerkli intel9 SDD 1T xotira qo\'shsa bo\'ladi')
    elif s=='Acer':
     b.insert(END,'Acer yili 2023 2 kullerkli intel7 SDD 1T xotira qo\'shsa bo\'ladi')
    elif s=='Asus':
     b.insert(END,'Asus yili 2022 1 kuller ofisni intel3 SDD 128 xotira qo\'shsa bo\'ladi')
    elif s=='Lenova':
     b.insert(END,'Lenova yili 2011 1 kuller ofisni intel5 SDD512 xotira qo\'shsa bo\'ladi')
    elif s=='Ko\'la':
     b.insert(END,'Ko\'la 1,5 litr Chiqazilgan sana 2021/01/21 Saqlanish muddati tugashi,2023/8/11')
    elif s=='Pepsi':
     b.insert(END,'Pepsi 1,0 litr Chiqazilgan sana 2020/23/21 Saqlanish muddati tugashi,2024/5/18')
    elif s=='Fanta':
     b.insert(END,'Fanta 2,0 litr Chiqazilgan sana 2020/01/21 Saqlanish muddati tugashi,2022/12/31')
def n():
    h=b.get(b.curselection())
    if h=='Sir Chiqazilgan sana 2021/01/21 Saqlanish muddati tugashi,2023/12/11':
     p.insert(END,'Sir 35,000 ming so\'m')
    elif h==' Kalbasasi Chiqazilgan sana 2022/01/21 Saqlanish muddati tugashi,2024/12/11':
     p.insert(END,'Kalbasa 21,000 ming so\'m')
    elif h=='Russia Kartoshkasi':
     p.insert(END,'Kartoshka 1 kilosi 4,000')
    elif h=='Russia Makaromi Chiqazilgan sana 2021/01/21 Saqlanish muddati tugashi,2025/12/11':
     p.insert(END,'Makarom 14,000 ming so\'m')
    elif h=='Hp yili 2023 2 kullerkli intel9 SDD 1T xotira qo\'shsa bo\'ladi':
     p.insert(END,'Hp 2200$')
    elif h=='Acer yili 2023 2 kullerkli intel7 SDD 1T xotira qo\'shsa bo\'ladi':
     p.insert(END,'Acer 1500$')
    elif h=='Asus yili 2022 1 kuller ofisni intel3 SDD 128 xotira qo\'shsa bo\'ladi':
     p.insert(END,'Asus 500$')
    elif h=='Lenova yili 2011 1 kuller ofisni intel5 SDD512 xotira qo\'shsa bo\'ladi':
     p.insert(END,'Lenova 400$')
    elif h=='Ko\'la 1,5 litr Chiqazilgan sana 2021/01/21 Saqlanish muddati tugashi,2023/8/11':
     p.insert(END,'Ko\'la 13,000 ming so\'m')
    elif h=='Pepsi 1,0 litr Chiqazilgan sana 2020/23/21 Saqlanish muddati tugashi,2024/5/18':
     p.insert(END,'Pepsi 10,000 ming so\'m')
    elif h=='Fanta 2,0 litr Chiqazilgan sana 2020/01/21 Saqlanish muddati tugashi,2022/12/31':
     p.insert(END,'Fanta 15,000 ming so\'m')
def V():
    n=p.get(p.curselection())
    if n=='Sir 35,000 ming so\'m':
        showinfo(title='Xabar',message='Sir sotib oliz')
    elif n=='Kalbasa 21,000 ming so\'m':
        showinfo(title='Xabar',message='Kalbasa sotib oldiz ')
    elif n=='Kartoshka 1 kilosi 4,000':
        showinfo(title='Xabar',message='Kartoshka sotib oldiz')
    elif n=='Makarom 14,000 ming so\'m':
        showinfo(title='Xabar',message='Makarom sotib oldiz')
    elif n=='Hp 2200$':
        showinfo(title='Xabar',message='Hp sotib oldiz')
    elif n=='Acer 1500$':
        showinfo(title='Xabar',message='Acer sotib oldiz')
    elif n=='Asus 500$':
        showinfo(title='Xabar',message='Asus sotib oldiz')
    elif n=='Lenova 400$':
        showinfo(title='Xabar',message='Lenova sotib oldiz')
    elif n=='Ko\'la 13,000 ming so\'m':
        showinfo(title='Xabar',message='Ko\'la sotib oldiz')
    elif n=='Pepsi 10,000 ming so\'m':
        showinfo(title='Xabar',message='Pepsi sotib oldiz')
    elif n=='Fanta 15,000 ming so\'m':
        showinfo(title='Xabar',message='Fanta sotib oldiz')
m=['Oziq ovqat','Notebook','Suv']
e=ttk.Entry(width=70)
e.pack(anchor=NW,pady=6,padx=6,)
l=Listbox(width=35,height=20)
l.place(x=200,y=100)
b=Listbox(width=65,height=15)
b.place(x=450,y=100)
p=Listbox(width=70,height=13)
p.place(x=355,y=450)
d1=StringVar(value='Menyu')
c=ttk.Combobox(values=m,textvariable=d1)
c.place(anchor=NW,x=6,y=35)
d=ttk.Button(width=20,text='Qidiruv',command=R)
d.place(x=455,y=6)
d1=ttk.Button(width=20,text='Menyudan Tanlash',command=o)
d1.place(x=455,y=370)
f=ttk.Button(width=20,text='Malumot',command=G)
f.place(x=705,y=370)
w=ttk.Button(width=20,text='O\'chirish',command=P)
w.place(x=580,y=400)
h=ttk.Button(width=20,text='Narxi',command=n)
h.place(x=200,y=490)
k=ttk.Button(width=20,text='Sotib olish',command=V)
k.place(x=200,y=600)

a.mainloop()