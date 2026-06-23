from tkinter import *
a=Tk()
a.title('klavatura')
a.geometry('1150x1000')
a.configure(bg='black')
def ochirish():
    e.delete(0,)
def a1():
    e.insert(END, 'Q')
def a2():
    e.insert(END, 'W')
def a3():
    e.insert(END, 'E')
def a4():
    e.insert(END, 'R')
def a5():
    e.insert(END, 'T')
def a6():
    e.insert(END, 'Y')
def a7():
    e.insert(END, 'U')
def a8():
    e.insert(END, 'I')
def a9():
    e.insert(END, 'O')
def a10():
    e.insert(END, 'P')
def b1():
    e.insert(END, 'A')
def b2():
    e.insert(END, 'S')
def b3():
    e.insert(END, 'D')
def b4():
    e.insert(END, 'F')
def b5():
    e.insert(END, 'G')
def b6():
    e.insert(END, 'H')
def b7():
    e.insert(END, 'J')
def b8():
    e.insert(END, 'K')
def b9():
    e.insert(END, 'L')
def d1():
    e.insert(END, 'Z')
def d2():
    e.insert(END, 'X')
def d3():
    e.insert(END, 'C')
def d4():
    e.insert(END, 'V')
def d5():
    e.insert(END, 'B')
def d6():
    e.insert(END, 'N')
def d7():
    e.insert(END, 'M')
e=Entry(width=100, bg='black', fg='red')
e.place(x=250,y=100,height=25)
a1=Button(width=8, height=2, text='Q', fg='red', bg='black', command=a1)
a1.place(x=100,y=200)
a2=Button(width=8, height=2, text='W', fg='red', bg='black', command=a2)
a2.place(x=200,y=200)
a3=Button(width=8, height=2, text='E', fg='red', bg='black', command=a3)
a3.place(x=300,y=200)
a4=Button(width=8, height=2, text='R', fg='red', bg='black', command=a4)
a4.place(x=400,y=200)
a5=Button(width=8, height=2, text='T', fg='red', bg='black', command=a5)
a5.place(x=500,y=200)
a6=Button(width=8, height=2, text='Y', fg='red', bg='black', command=a6)
a6.place(x=600,y=200)
a7=Button(width=8, height=2, text='U', fg='red', bg='black', command=a7)
a7.place(x=700,y=200)
a8=Button(width=8, height=2, text='I', fg='red', bg='black', command=a8)
a8.place(x=800,y=200)
a9=Button(width=8, height=2, text='O', fg='red', bg='black', command=a9)
a9.place(x=900,y=200)
a10=Button(width=8, height=2, text='P', fg='red', bg='black', command=a10)
a10.place(x=1000,y=200)
b1=Button(width=8, height=2, text='A', fg='red', bg='black', command=b1)
b1.place(x=150,y=300)
b2=Button(width=8, height=2, text='S', fg='red', bg='black', command=b2)
b2.place(x=250,y=300)
b3=Button(width=8, height=2, text='D', fg='red', bg='black', command=b3)
b3.place(x=350,y=300)
b4=Button(width=8, height=2, text='F', fg='red', bg='black', command=b4)
b4.place(x=450,y=300)
b5=Button(width=8, height=2, text='G', fg='red', bg='black', command=b5)
b5.place(x=550,y=300)
b6=Button(width=8, height=2, text='H', fg='red', bg='black', command=b6)
b6.place(x=650,y=300)
b7=Button(width=8, height=2, text='J', fg='red', bg='black', command=b7)
b7.place(x=750,y=300)
b8=Button(width=8, height=2, text='K', fg='red', bg='black', command=b8)
b8.place(x=850,y=300)
b9=Button(width=8, height=2, text='L', fg='red', bg='black', command=b9)
b9.place(x=950,y=300)
d1=Button(width=8, height=2, text='Z', fg='red', bg='black', command=d1)
d1.place(x=200,y=400)
d2=Button(width=8, height=2, text='X', fg='red', bg='black', command=d2)
d2.place(x=300,y=400)
d3=Button(width=8, height=2, text='C', fg='red', bg='black', command=d3)
d3.place(x=400,y=400)
d4=Button(width=8, height=2, text='V', fg='red', bg='black', command=d4)
d4.place(x=500,y=400)
d5=Button(width=8, height=2, text='B', fg='red', bg='black', command=d5)
d5.place(x=600,y=400)
d6=Button(width=8, height=2, text='N', fg='red', bg='black', command=d6)
d6.place(x=700,y=400)
d7=Button(width=8, height=2, text='M', fg='red', bg='black', command=d7)
d7.place(x=800,y=400)
m=Button(width=10, height=2, text='Del', fg='red', bg='black', command=ochirish)
m.place(x=900,y=400)
a.mainloop()