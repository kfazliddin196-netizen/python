from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
a=Tk()
a.title()
a.geometry('400x500')
a.configure(bg='red')
def R30():
 if e12.get() == "Komilov" and b12.get() == "Fazliddin" and d12.get() == "kfazliddin196@gmail.com" and c12.get() == '7777':
    n15=Tk()
    n15.title('Magazin')
    n15.geometry('1000x1000')
    n15.configure(bg='black')
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
        elif e.get() == 'Asus':
            l.insert(END, 'Asus')
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
            l.insert(END, 'Xech narsa topilmadi')
    def O():
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
        l.delete(0, END)
        p.delete(0, END)
        b.delete(0, END)

    def G():
        s = l.get(l.curselection())
        if s == 'Sir':
            b.insert(END, 'Sir Chiqazilgan sana 2021/01/21 Saqlanish muddati tugashi,2023/12/11')
        elif s == 'Kalbasa':
            b.insert(END, ' Kalbasasi Chiqazilgan sana 2022/01/21 Saqlanish muddati tugashi,2024/12/11')
        elif s == 'Kartoshka':
            b.insert(END, 'Russia Kartoshkasi')
        elif s == 'Makarom':
            b.insert(END, 'Russia Makaromi Chiqazilgan sana 2021/01/21 Saqlanish muddati tugashi,2025/12/11')
        elif s == 'Hp':
            b.insert(END, 'Hp yili 2023 2 kullerkli intel9 SDD 1T xotira qo\'shsa bo\'ladi')
        elif s == 'Acer':
            b.insert(END, 'Acer yili 2023 2 kullerkli intel7 SDD 1T xotira qo\'shsa bo\'ladi')
        elif s == 'Asus':
            b.insert(END, 'Asus yili 2022 1 kuller ofisni intel3 SDD 128 xotira qo\'shsa bo\'ladi')
        elif s == 'Lenova':
            b.insert(END, 'Lenova yili 2011 1 kuller ofisni intel5 SDD512 xotira qo\'shsa bo\'ladi')
        elif s == 'Ko\'la':
            b.insert(END, 'Ko\'la 1,5 litr Chiqazilgan sana 2021/01/21 Saqlanish muddati tugashi,2023/8/11')
        elif s == 'Pepsi':
            b.insert(END, 'Pepsi 1,0 litr Chiqazilgan sana 2020/23/21 Saqlanish muddati tugashi,2024/5/18')
        elif s == 'Fanta':
            b.insert(END, 'Fanta 2,0 litr Chiqazilgan sana 2020/01/21 Saqlanish muddati tugashi,2022/12/31')
    def n():
        h = b.get(b.curselection())
        e1 = len(e.get())
        if h == 'Sir Chiqazilgan sana 2021/01/21 Saqlanish muddati tugashi,2023/12/11':
            p.insert(END, 'Sir 35000 ming so\'m')
            e10.insert(e1, '+35000')
        elif h == ' Kalbasasi Chiqazilgan sana 2022/01/21 Saqlanish muddati tugashi,2024/12/11':
            p.insert(END, 'Kalbasa 21000 ming so\'m')
            e10.insert(e1, '+21000')
        elif h == 'Russia Kartoshkasi':
            p.insert(END, 'Kartoshka 1 kilosi 4000')
            e10.insert(e1, '+4000')
        elif h == 'Russia Makaromi Chiqazilgan sana 2021/01/21 Saqlanish muddati tugashi,2025/12/11':
            p.insert(END, 'Makarom 14000 ming so\'m')
            e10.insert(e1, '14000')
        elif h == 'Hp yili 2023 2 kullerkli intel9 SDD 1T xotira qo\'shsa bo\'ladi':
            p.insert(END, 'Hp 2200000')
            e10.insert(e1, '+2200000')
        elif h == 'Acer yili 2023 2 kullerkli intel7 SDD 1T xotira qo\'shsa bo\'ladi':
            p.insert(END, 'Acer 1500000')
            e10.insert(e1, '+1500000')
        elif h == 'Asus yili 2022 1 kuller ofisni intel3 SDD 128 xotira qo\'shsa bo\'ladi':
            p.insert(END, 'Asus 5000000')
            e10.insert(e1, '+5000000')
        elif h == 'Lenova yili 2011 1 kuller ofisni intel5 SDD512 xotira qo\'shsa bo\'ladi':
            p.insert(END, 'Lenova 4000000')
            e10.insert(e1, '+4000000')
        elif h == 'Ko\'la 1,5 litr Chiqazilgan sana 2021/01/21 Saqlanish muddati tugashi,2023/8/11':
            p.insert(END, 'Ko\'la 13000 ming so\'m')
            e10.insert(e1, '+13000')
        elif h == 'Pepsi 1,0 litr Chiqazilgan sana 2020/23/21 Saqlanish muddati tugashi,2024/5/18':
            p.insert(END, 'Pepsi 10000 ming so\'m')
            e10.insert(e1, '+10000')
        elif h == 'Fanta 2,0 litr Chiqazilgan sana 2020/01/21 Saqlanish muddati tugashi,2022/12/31':
            p.insert(END, 'Fanta 15000 ming so\'m')
            e10.insert(e1, '+13000')
    def V1():
        e3 = e10.get()
        if e3 == '':
            showinfo(title='narx', message=f'jami 0 so`m')
        else:
            e2 = eval(e3)
            showinfo(title='narx', message=f'jami {e2}so`m')
    #..........................................................................................
    if e12.get() == "Komilov":
        if b12.get() == "Fazliddin":
            if d12.get() == "kfazliddin196@gmail.com":
                if c12.get() == '7777':
                    showinfo(title="Xabar", message="magazinga xush kelibsiz")
    # .......................................................................................
    m = ['Oziq ovqat', 'Notebook', 'Suv']
    expression = StringVar()
    e = ttk.Entry(n15,width=70)
    e.pack(anchor=NW, pady=6, padx=6, )
    l = Listbox(n15,width=35, height=20, bg='red', fg='black')
    l.place(x=200, y=100)
    b = Listbox(n15,width=65, height=15, bg='red', fg='black')
    b.place(x=450, y=100)
    p = Listbox(n15,width=70, height=13, bg='red', listvariable=expression)
    p.place(x=355, y=450, )
    d1 = StringVar(value='Menyu')
    c = ttk.Combobox(n15,values=m, textvariable=d1)
    c.place(anchor=NW, x=6, y=35)
    d = ttk.Button(n15,width=20, text='Qidiruv', command=R)
    d.place(x=455, y=6)
    d2 = ttk.Button(n15,width=20, text='Menyudan Tanlash', command=O)
    d2.place(x=455, y=370)
    f = ttk.Button(n15,width=20, text='Malumot', command=G)
    f.place(x=705, y=370)
    w = ttk.Button(n15,width=20, text='O\'chirish', command=P)
    w.place(x=580, y=400)
    h = ttk.Button(n15,width=20, text='Narxi', command=n)
    h.place(x=200, y=490)
    k = ttk.Button(n15,width=20, text='Sotib olish', command=V1)
    k.place(x=200, y=600)
    e10 = ttk.Entry(n15)
    e10.place(x=100000000000000000000000000, y=1000000000000000000000000000000)
#......................................................................................................
m12=ttk.Button(width=20,text='Ro\'yxatdan o\'tish',command=R30)
m12.place(x=150,y=300)
l=Label(width=17,text='Familya',bg='red')
l.place(x=150,y=77)
e12=ttk.Entry(width=20)
e12.place(x=150,y=100)
l=Label(width=17,text='Ism',bg='red')
l.place(x=150,y=127)
b12=ttk.Entry(width=20)
b12.place(x=150,y=150)
l=Label(width=17,text='Gmail',bg='red')
l.place(x=150,y=177)
d12=ttk.Entry(width=20)
d12.place(x=150,y=200)
l=Label(width=17,text='Paro\'l',bg='red')
l.place(x=150,y=227)
c12=ttk.Entry(width=20,show='*')
c12.place(x=150,y=250)
a.mainloop()
