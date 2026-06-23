from tkinter import *
from tkinter.messagebox import askyesno,showinfo
from tkinter import ttk
from customtkinter import *
from datetime import datetime
a = Tk()
a.title()
a.geometry("600x600")
a.configure(bg='black')
custom=datetime.now()
now=custom.strftime('%H:%M:%S')
def m():
    r=askyesno(title=now,message='Naxtga 189 900 000 So\'m')
    if r==True:
        showinfo(title=now,message='To\'landi tez orada buyurmangiz keladi')
    else:
        showinfo(title=now,message='Bekor qilindi')
def m1():
    r=askyesno(title=now,message='Naxtga 586 900 000 So\'m')
    if r==True:
        showinfo(title=now,message='To\'landi tez orada buyurmangiz keladi')
    else:
        showinfo(title=now,message='Bekor qilindi')
def m2():
    r=askyesno(title=now,message='Naxtga  999 900 000  So\'m')
    if r==True:
        showinfo(title=now,message='To\'landi tez orada buyurmangiz keladi')
    else:
        showinfo(title=now,message='Bekor qilindi')
def m3():
    r=askyesno(title=now,message='Naxtga 379 900 000 So\'m')
    if r==True:
        showinfo(title=now,message='To\'landi tez orada buyurmangiz keladi')
    else:
        showinfo(title=now,message='Bekor qilindi')
def m4():
    r=askyesno(title=now,message='Naxtga 869 900 000  So\'m')
    if r==True:
        showinfo(title=now,message='To\'landi tez orada buyurmangiz keladi')
    else:
        showinfo(title=now,message='Bekor qilindi')
def m5():
    r=askyesno(title=now,message='Naxtga 317 900 000 So\'m')
    if r==True:
        showinfo(title=now,message='To\'landi tez orada buyurmangiz keladi')
    else:
        showinfo(title=now,message='Bekor qilindi')
def m6():
    r=askyesno(title=now,message='Naxtga 409 900 000  So\'m')
    if r==True:
        showinfo(title=now,message='To\'landi tez orada buyurmangiz keladi')
    else:
        showinfo(title=now,message='Bekor qilindi')
def m7():
    r=askyesno(title=now,message='Naxtga 699 900 000 So\'m')
    if r==True:
        showinfo(title=now,message='To\'landi tez orada buyurmangiz keladi')
    else:
        showinfo(title=now,message='Bekor qilindi')
def m8():
    r=askyesno(title=now,message='Naxtga  379 900 000 So\'m')
    if r==True:
        showinfo(title=now,message='To\'landi tez orada buyurmangiz keladi')
    else:
        showinfo(title=now,message='Bekor qilindi')
def m9():
    r=askyesno(title=now,message='Naxtga 603 900 000 So\'m')
    if r==True:
        showinfo(title=now,message='To\'landi tez orada buyurmangiz keladi')
    else:
        showinfo(title=now,message='Bekor qilindi')
def m10():
    r=askyesno(title=now,message='Naxtga 729 900 000 So\'m')
    if r==True:
        showinfo(title=now,message='To\'landi tez orada buyurmangiz keladi')
    else:
        showinfo(title=now,message='Bekor qilindi')
def m11():
    r=askyesno(title=now,message='Naxtga 269 900 000 So\'m')
    if r==True:
        showinfo(title=now,message='To\'landi tez orada buyurmangiz keladi')
    else:
        showinfo(title=now,message='Bekor qilindi')
def fm():
    o = 189900000
    s = int(c1.get())
    d1 = o // s
    r1 = askyesno(title=now, message=f'Naxtga {d1:,} So\'m')
    if r1 == True:
        showinfo(title=now, message='To\'landi tez orada buyurmangiz keladi')
    else:
        showinfo(title=now, message='Bekor qilindi')
def fm1():
    o1 = 586900000
    s1 = int(c2.get())
    d2 = o1 // s1
    r2 = askyesno(title=now, message=f'Naxtga {d2:,} So\'m')
    if r2 == True:
        showinfo(title=now, message='To\'landi tez orada buyurmangiz keladi')
    else:
        showinfo(title=now, message='Bekor qilindi')
def fm2():
    o2 = 999900000
    s2 = int(c3.get())
    d3 = o2 // s2
    r3 = askyesno(title=now, message=f'Naxtga {d3:,} So\'m')
    if r3 == True:
        showinfo(title=now, message='To\'landi tez orada buyurmangiz keladi')
    else:
        showinfo(title=now, message='Bekor qilindi')
def fm3():
    o3 = 379900000
    s3 = int(c4.get())
    d4 = o3 // s3
    r4 = askyesno(title=now, message=f'Naxtga {d4:,} So\'m')
    if r4 == True:
        showinfo(title=now, message='To\'landi tez orada buyurmangiz keladi')
    else:
        showinfo(title=now, message='Bekor qilindi')
def fm4():
    o4 = 869900000
    s4 = int(c5.get())
    d5 = o4 // s4
    r5 = askyesno(title=now, message=f'Naxtga {d5:,} So\'m')
    if r5 == True:
        showinfo(title=now, message='To\'landi tez orada buyurmangiz keladi')
    else:
        showinfo(title=now, message='Bekor qilindi')
def fm5():
    o5 = 317900000
    s5 = int(c6.get())
    d6 = o5 // s5
    r6 = askyesno(title=now, message=f'Naxtga {d6:,} So\'m')
    if r6 == True:
        showinfo(title=now, message='To\'landi tez orada buyurmangiz keladi')
    else:
        showinfo(title=now, message='Bekor qilindi')
def fm6():
    o6 = 409900000
    s6 = int(c7.get())
    d7 = o6 // s6
    r7 = askyesno(title=now, message=f'Naxtga {d7:,} So\'m')
    if r7 == True:
        showinfo(title=now, message='To\'landi tez orada buyurmangiz keladi')
    else:
        showinfo(title=now, message='Bekor qilindi')
def fm7():
    o7 = 699900000
    s7 = int(c8.get())
    d8 = o7 // s7
    r8 = askyesno(title=now, message=f'Naxtga {d8:,} So\'m')
    if r8 == True:
        showinfo(title=now, message='To\'landi tez orada buyurmangiz keladi')
    else:
        showinfo(title=now, message='Bekor qilindi')
def fm8():
    o8 = 379900000
    s8 = int(c9.get())
    d9 = o8 // s8
    r9 = askyesno(title=now, message=f'Naxtga {d9:,} So\'m')
    if r9 == True:
        showinfo(title=now, message='To\'landi tez orada buyurmangiz keladi')
    else:
        showinfo(title=now, message='Bekor qilindi')
def fm9():
    o9 = 603900000
    s9 = int(c10.get())
    d10 = o9 // s9
    r10 = askyesno(title=now, message=f'Naxtga {d10:,} So\'m')
    if r10 == True:
        showinfo(title=now, message='To\'landi tez orada buyurmangiz keladi')
    else:
        showinfo(title=now, message='Bekor qilindi')
def fm10():
    o10 = 729900000
    s10 = int(c11.get())
    d11 = o10 // s10
    r11 = askyesno(title=now, message=f'Naxtga {d11:,} So\'m')
    if r11 == True:
        showinfo(title=now, message='To\'landi tez orada buyurmangiz keladi')
    else:
        showinfo(title=now, message='Bekor qilindi')
def fm11():
    o11 = 269900000
    s11 = int(c12.get())
    d12 = o11 // s11
    r12 = askyesno(title=now, message=f'Naxtga {d12:,} So\'m')
    if r12 == True:
        showinfo(title=now, message='To\'landi tez orada buyurmangiz keladi')
    else:
        showinfo(title=now, message='Bekor qilindi')
def oyna1():
    mf=Tk()
    mf.title()
    mf.geometry()
    label=Label(mf,width=25,height=15,text='2024-Yil\n'
                                           'Matori 1.5\n'
                                            'Xolati: Yengi\n'
                                             'yoqilg\'i: Benzin',)

    label.pack(expand=1)
def oyna2():
    mf=Tk()
    mf.title()
    mf.geometry()
    label=Label(mf,width=25,height=15,text='2024-Yil\n'
                             'Matori: 2.5\n'
                              'Xolati: Yengi\n'
                               'Yoqilg\'i: Benzin')
    label.pack(expand=1)
def oyna3():
    mf2=Tk()
    mf2.title()
    mf2.geometry()
    label1=Label(mf2,width=25,height=15,text='2024-Yil\n'
                                             'Matori: 3.0\n'
                                              'Xolati:Yangi\n'
                                              'Yoqilg\'i: Elektr')
    label1.pack(expand=1)
def oyna4():
    mf=Tk()
    mf.title()
    mf.geometry()
    label=Label(mf,width=25,height=15,text='2024-Yil\n'
                                             'Matori: 2.8\n'
                                              'Xolati:Yangi\n'
                                              'Yoqilg\'i: Elektr')
    label.pack(expand=1)
def oyna5():
    mf=Tk()
    mf.title()
    mf.geometry()
    label=Label(mf,width=25,height=15,text='2024-Yil\n'
                                             'Matori: 3.2\n'
                                              'Xolati:Yangi\n'
                                              'Yoqilg\'i:Benzin')
    label.pack(expand=1)
def oyna6():
    mf2=Tk()
    mf2.title()
    mf2.geometry()
    label1=Label(mf2,width=25,height=15,text='2024-Yil\n'
                                             'Matori: 2.1\n'
                                              'Xolati:Yangi\n'
                                              'Yoqilg\'i: Elektr')
    label1.pack(expand=1)
def oyna7():
    mf=Tk()
    mf.title()
    mf.geometry()
    label=Label(mf,width=25,height=15,text='2024-Yil\n'
                                             'Matori:1.8\n'
                                              'Xolati:Yangi\n'
                                             'Yoqilg\'i:')
    label.pack(expand=1)
def oyna8():
    mf=Tk()
    mf.title()
    mf.geometry()
    label=Label(mf,width=25,height=15,text='2024-Yil\n'
                                             'Matori:2.3\n'
                                              'Xolati:Yangi\n'
                                              'Yoqilg\'i:')
    label.pack(expand=1)
def oyna9():
    mf=Tk()
    mf.title()
    mf.geometry()
    label=Label(mf,width=25,height=15,text='2023-Yil\n'
                                             'Matori 3.2\n'
                                              'Xolati:Yangi\n'
                                              'Yoqilg\'i:')
    label.pack(expand=1)
def oyna10():
    mf2=Tk()
    mf2.title()
    mf2.geometry()
    label1=Label(mf2,width=25,height=15,text='2023-Yil\n'
                                             'Matori:3.1\n'
                                              'Xolati:Yangi\n'
                                             'Yoqilg\'i:')
    label1.pack(expand=1)
def oyna11():
    mf=Tk()
    mf.title()
    mf.geometry()
    label=Label(mf,width=25,height=15,text='2023-Yil\n'
                                             'Matori: 3.4\n'
                                              'Xolati:Yangi\n'
                                              'Yoqilg\'i:')
    label.pack(expand=1)
def oyna12():
    mf=Tk()
    mf.title()
    mf.geometry()
    label=Label(mf,width=25,height=15,text='2023-Yil\n'
                                             'Matori:2.2'
                                              'Xolati:Yangi\n'
                                              'Yoqilg\'i:Benzin')
    label.pack(expand=1)
u=Label(text='Model Kia',font=('Arial',32))
u.place(x=220,y=30)
n=ttk.Notebook()
n.place(x=50,y=150,)
p1=PhotoImage(file='Sonet.png')
p2=PhotoImage(file='Sorento.png')
p3=PhotoImage(file='EV9.png')
p4=PhotoImage(file='Seltos.png')
p5=PhotoImage(file='K9.png')
p6=PhotoImage(file='Cerato.png')
p7=PhotoImage(file='Sportage.png')
p8=PhotoImage(file='EV6.png')
p9=PhotoImage(file='K5.png')
p10=PhotoImage(file='Carnival.png')
p11=PhotoImage(file='K8.png')
p12=PhotoImage(file='Bongo III.png')
f1 = ttk.Frame(n)
f2 = ttk.Frame(n)
f3=ttk.Frame(n)
f4=ttk.Frame(n)
f5=ttk.Frame(n)
f6=ttk.Frame(n)
f7=ttk.Frame(n)
f8=ttk.Frame(n)
f9=ttk.Frame(n)
f10=ttk.Frame(n)
f11=ttk.Frame(n)
f12=ttk.Frame(n)
n.add(f1, text="Sonet")
n.add(f2, text="Sorento")
n.add(f3,text='EV9')
n.add(f4,text='Seltos')
n.add(f5,text='K9')
n.add(f6,text='Cerato')
n.add(f7,text='Sportage')
n.add(f8,text='EV6')
n.add(f9,text='K5')
n.add(f10,text='Carnival')
n.add(f11,text='K8')
n.add(f12,text='Bongo III')
l = Label(f1, image=p1,height=300)
l.pack(pady=20)
l = Label(f2, image=p2,height=300)
l.pack(pady=20)
l = Label(f3, image=p3,height=300)
l.pack(pady=20)
l = Label(f4, image=p4,height=300)
l.pack(pady=20)
l = Label(f5, image=p5,height=300)
l.pack(pady=20)
l = Label(f6, image=p6,height=300)
l.pack(pady=20)
l = Label(f7, image=p7,height=300)
l.pack(pady=20)
l = Label(f8, image=p8,height=300)
l.pack(pady=20)
l = Label(f9, image=p9,height=300)
l.pack(pady=20)
l = Label(f10, image=p10,height=300)
l.pack(pady=20)
l = Label(f11, image=p11,height=300)
l.pack(pady=20)
l = Label(f12, image=p12,height=300)
l.pack(pady=20)
mu1=[12,24,36,48,60,72]
d15=StringVar(value='Yil')
c1=ttk.Combobox(f1,textvariable=d15,values=mu1,width=2)
c1.place(x=320,y=270)
#.......................................................................................
mu2=[12,24,36,48,60,72]
d16=StringVar(value='Yil')
c2=ttk.Combobox(f2,textvariable=d16,values=mu2,width=2)
c2.place(x=320,y=270)
#.......................................................................................
mu3=[12,24,36,48,60,72]
d17=StringVar(value='Yil')
c3=ttk.Combobox(f3,textvariable=d17,values=mu3,width=2)
c3.place(x=320,y=270)
#.......................................................................................
mu4=[12,24,36,48,60,72]
d18=StringVar(value='Yil')
c4=ttk.Combobox(f4,textvariable=d18,values=mu4,width=2)
c4.place(x=320,y=270)
#.......................................................................................
mu5=[12,24,36,48,60,72]
d19=StringVar(value='Yil')
c5=ttk.Combobox(f5,textvariable=d19,values=mu5,width=2)
c5.place(x=340,y=270)
#.......................................................................................
mu6=[12,24,36,48,60,72]
d20=StringVar(value='Yil')
c6=ttk.Combobox(f6,textvariable=d20,values=mu6,width=2)
c6.place(x=320,y=270)
#.......................................................................................
mu7=[12,24,36,48,60,72]
d21=StringVar(value='Yil')
c7=ttk.Combobox(f7,textvariable=d21,values=mu7,width=2)
c7.place(x=320,y=270)
#.......................................................................................
mu8=[12,24,36,48,60,72]
d22=StringVar(value='Yil')
c8=ttk.Combobox(f8,textvariable=d22,values=mu8,width=2)
c8.place(x=320,y=270)
#.......................................................................................
mu9=[12,24,36,48,60,72]
d23=StringVar(value='Yil')
c9=ttk.Combobox(f9,textvariable=d23,values=mu9,width=2)
c9.place(x=320,y=270)
#.......................................................................................
mu10=[12,24,36,48,60,72]
d24=StringVar(value='Yil')
c10=ttk.Combobox(f10,textvariable=d24,values=mu10,width=2)
c10.place(x=320,y=270)
#.......................................................................................
mu11=[12,24,36,48,60,72]
d25=StringVar(value='Yil')
c11=ttk.Combobox(f11,textvariable=d25,values=mu11,width=2)
c11.place(x=320,y=270)
#.......................................................................................
mu12=[12,24,36,48,60,72]
d26=StringVar(value='Yil')
c12=ttk.Combobox(f12,textvariable=d26,values=mu12,width=2)
c12.place(x=340,y=270)
#.......................................................................................
b=CTkButton(f1,text='Sotib olish',command=m)
b.place(x=10,y=270)

b1=CTkButton(f2,text='Sotib olish',command=m1)
b1.place(x=10,y=270)

b2=CTkButton(f3,text='Sotib olish',command=m2)
b2.place(x=10,y=270)

b3=CTkButton(f4,text='Sotib olish',command=m3)
b3.place(x=10,y=270)

b4=CTkButton(f5,text='Sotib olish',command=m4)
b4.place(x=10,y=270)

b5=CTkButton(f6,text='Sotib olish',command=m5)
b5.place(x=10,y=270)

b6=CTkButton(f7,text='Sotib olish',command=m6)
b6.place(x=10,y=270)

b7=CTkButton(f8,text='Sotib olish',command=m7)
b7.place(x=10,y=270)

b8=CTkButton(f9,text='Sotib olish',command=m8)
b8.place(x=10,y=270)

b9=CTkButton(f10,text='Sotib olish',command=m9)
b9.place(x=10,y=270)

b10=CTkButton(f11,text='Sotib olish',command=m10)
b10.place(x=10,y=270)

b11=CTkButton(f12,text='Sotib olish',command=m11)
b11.place(x=10,y=270)
#..............................................
l1=CTkButton(f1,text='Oyiga',command=fm)
l1.place(x=160,y=270)
l2=CTkButton(f2,text='Oyiga',command=fm1)
l2.place(x=160,y=270)
l3=CTkButton(f3,text='Oyiga',command=fm2)
l3.place(x=160,y=270)
l4=CTkButton(f4,text='Oyiga',command=fm3)
l4.place(x=160,y=270)
l5=CTkButton(f5,text='Oyiga',command=fm4)
l5.place(x=160,y=270)
l6=CTkButton(f6,text='Oyiga',command=fm5)
l6.place(x=160,y=270)
l7=CTkButton(f7,text='Oyiga',command=fm6)
l7.place(x=160,y=270)
l8=CTkButton(f8,text='Oyiga',command=fm7)
l8.place(x=160,y=270)
l9=CTkButton(f9,text='Oyiga',command=fm8)
l9.place(x=160,y=270)
l10=CTkButton(f10,text='Oyiga',command=fm9)
l10.place(x=160,y=270)
l11=CTkButton(f11,text='Oyiga',command=fm10)
l11.place(x=160,y=270)
l12=CTkButton(f12,text='Oyiga',command=fm11)
l12.place(x=160,y=270)
#.......................................................................................
n1=CTkButton(f1,text='Malumot',command=oyna1)
n1.place(x=85,y=300)
n2=CTkButton(f2,text='Malumot',command=oyna2)
n2.place(x=85,y=300)
n3=CTkButton(f3,text='Malumot',command=oyna3)
n3.place(x=85,y=300)
n4=CTkButton(f4,text='Malumot',command=oyna4)
n4.place(x=85,y=300)
n5=CTkButton(f5,text='Malumot',command=oyna5)
n5.place(x=25,y=300)
n6=CTkButton(f6,text='Malumot',command=oyna6)
n6.place(x=85,y=300)
n7=CTkButton(f7,text='Malumot',command=oyna7)
n7.place(x=85,y=300)
n8=CTkButton(f8,text='Malumot',command=oyna8)
n8.place(x=85,y=300)
n9=CTkButton(f9,text='Malumot',command=oyna9)
n9.place(x=85,y=300)
n10=CTkButton(f10,text='Malumot',command=oyna10)
n10.place(x=85,y=300)
n11=CTkButton(f11,text='Malumot',command=oyna11)
n11.place(x=85,y=300)
n12=CTkButton(f12,text='Malumot',command=oyna12)
n12.place(x=85,y=300)
a.mainloop()