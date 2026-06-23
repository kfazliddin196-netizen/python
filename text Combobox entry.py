from tkinter import *
from tkinter import ttk
from tkinter import filedialog
a=Tk()
a.title('Paliknika')
a.geometry('1000x600')
a.configure(bg='red')
l=Label(text='Paliknika',font=200,bg='red')
l.pack(anchor=N,expand=True,pady=15,)
t=Text()
t.place(width=470,height=320,x=300,y=100)
def o():
    filepath = filedialog.askopenfilename()
    if filepath != "":
        with open(filepath, "r") as file:
            text = file.read()
            t.delete("1.0", END)
            t.insert("1.0", text)
def s():
    filepath = filedialog.asksaveasfilename()
    if filepath != "":
        text = t.get("1.0", END)
        with open(filepath, "w") as file:
            file.write(text)
def u():
    s = c.get()
    if s=="Tish og'rig'i":
     t.insert(END,"Komilov Fazliddin Qabuliga yozildingiz\n", s)
    elif s=="Bosh og'rig'i":
     t.insert(END,"Xotamov Akbarmirzo Qabuliga yozildingiz\n", s)
    elif s=='Pisxologiya':
     t.insert(END,'Umurziqov Ismoil Qabuliga yozildingiz\n', s)
    elif s=="Yurak og'rig'i":
     t.insert(END,'Solijonov Abdurahmon Qabuliga yozildingiz\n',s)
def k():
   if e.get()=='':
    t.insert(END,'')
   else:
    t.insert(END,e.get())
def I():
    if e1.get()=='':
     t.insert(END,'')
    else:
     t.insert(END,e1.get())
def J():
    if e2.get()=='':
     t.insert(END,e2.get())
    else:
     t.insert(END,e2.get())
def J1():
    if e3.get()=="":
     t.insert(END,e3.get())
def f5():
    t.delete(1.0,END)
m=["Tish og'rig'i","Bosh og'rig'i","Yurak og'rig'i",'Pisxologiya']
d1=StringVar(value='Menyu')
c=ttk.Combobox(values=m,textvariable=d1)
c.place(x=25,y=50)
def F6(event):
    e.config(state=NORMAL)
    e.delete(0,END)
e=ttk.Entry(width=30)
e.place(x=25,y=160)
e.insert(0,'F.I.O')
e.config(state=DISABLED)
e.bind('<Button-1>',F6)
def W1(event):
    e1.config(state=NORMAL)
    e1.delete(0,END)
e1=ttk.Entry(width=30)
e1.place(x=25,y=230)
e1.insert(0,"Yil Oy Tug'ilgan kun")
e1.config(state=DISABLED)
e1.bind('<Button-1>',W1)
def U8(event):
    e2.config(state=NORMAL)
    e2.delete(0,END)
e2=ttk.Entry(width=30)
e2.place(x=25,y=300)
e2.insert(0,"No'mer")
e2.config(state=DISABLED)
e2.bind('<Button-1>',U8)
def MA8(event):
    e3.config(state=NORMAL)
    e3.delete(0,END)
e3=ttk.Entry(width=30)
e3.place(x=25,y=370)
e3.insert(0,"Kasalik turi")
e3.config(state=DISABLED)
e3.bind('<Button-1>',MA8)
b3=ttk.Button(width=8,command=k)
b3.place(x=220,y=160)
b4=ttk.Button(width=8,command=I)
b4.place(x=220,y=230)
b5=ttk.Button(width=8,command=J)
b5.place(x=220,y=300,)
b6=ttk.Button(width=8,command=J1)
b6.place(x=220,y=370)
b7=ttk.Button(width=20,command=u,text='kasalikni turi')
b7.place(x=25,y=100)
b8=ttk.Button(width=20,command=f5,text="O'chirish")
b8.place(x=800,y=100)
b1=ttk.Button(width=20,command=s,text='Saqlab qo\'yish')
b1.place(x=300,y=450)
b2=ttk.Button(width=20,command=o,text='Fayil ochish')
b2.place(x=640,y=450)
a.mainloop()


