from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.messagebox import showinfo
from customtkinter import *
a=Tk()
a.title('cofe')
a.geometry('1000x1000')
def j():
    ab=Tk()
    ab.title('cofe')
    ab.configure(bg='brown')
    ab.geometry('1000x1000')
    t = CTkTextbox(master=ab, width=350, height=210)
    t.place(x=350, y=20)
    def open_file():
        filepath = filedialog.askopenfilename()
        if filepath != "":
            with open(filepath, "r") as file:
                text = file.read()
                t.delete("1.0", END)
                t.insert("1.0", text)
    def save_file():
        filepath = filedialog.asksaveasfilename()
        if filepath != "":
            text = t.get("1.0", END)
            with open(filepath, "w") as file:
                file.write(text)
        t.delete("1.0", END)
    def k():
        en = e.get().strip()
        name = e1.get().strip()
        email = e2.get().strip()
        parol = e3.get().strip()
        if en and name and email and parol:
         t.insert(END,
                     'Familya: ' + en + "\n" 'Ism: ' + name + "\n" 'Stol: ' + email + "\n" 'Vaqt: ' + parol + "\n")
         e.delete(0, END)
         e1.delete(0, END)
         e2.delete(0, END)
         e3.delete(0, END)

    def g():
        t.delete(0.0, 'end')
        salom2.delete(0,END)
    la = CTkLabel(master=ab, text='Familya')
    la.place(x=150, y=-1)
    e = CTkEntry(master=ab, width=300, border_color='red', corner_radius=32, placeholder_text='Familya')
    e.place(x=20, y=25)
    la = CTkLabel(master=ab, text='Ism')
    la.place(x=160, y=53)
    e1 = CTkEntry(master=ab, width=300, border_color='red', corner_radius=32, placeholder_text='Ism')
    e1.place(x=20, y=80)
    la = CTkLabel(master=ab, text='Stol')
    la.place(x=160, y=109)
    e2 = CTkEntry(master=ab, width=300, border_color='red', corner_radius=32, placeholder_text='Stol')
    e2.place(x=20, y=135)
    la = CTkLabel(master=ab, text='Soat')
    la.place(x=160, y=165)
    e3 = CTkEntry(master=ab, width=300, border_color='red', corner_radius=32, placeholder_text='soat')
    e3.place(x=20, y=190)
    b1 = CTkButton(width=226, master=ab, corner_radius=32, text='open_file', command=open_file, hover_color='black')
    b1.place(x=35, y=290)
    b2 = CTkButton(width=226, master=ab, corner_radius=32, text='save_file', command=save_file, hover_color='black')
    b2.place(x=450, y=290)
    b = CTkButton(master=ab, width=680, corner_radius=32, text="Ro'yhatdan o'tish", command=k, hover_color='black')
    b.place(x=20, y=245)
    b3 = CTkButton(master=ab, width=40, text='', command=g)
    b3.place(x=720, y=20)
    la = CTkLabel(master=ab, text="o'chirish")
    la.place(x=720, y=50)
    def gh():
        sd=b1.get()
        e1 = len(e.get())
        if sd=='Latte':
            salom2.insert(END,'Latte 10.000')
            e10.insert(e1,'+10000')
        elif sd=='Americano':
            salom2.insert(END,'Americano 7.000')
            e10.insert(e1,'+7000')
        elif sd== 'Cappuccino':
            salom2.insert(END,'Cappuccino 12.000')
            e10.insert(e1,'+12000')
        elif sd=='Espresso':
            salom2.insert(END,'Espresso 9.000')
            e10.insert(e1,'+9000')
        elif sd=='Mocco':
            salom2.insert(END,'Mocco 15.000')
            e10.insert(e1,'+15000')
        elif sd=='Arabica':
            salom2.insert(END,'Arabica 14.000')
            e10.insert(e1,'14000')
        elif sd=='Cacao':
            salom2.insert(END,'Cacao 4.500')
            e10.insert(e1,'+4500')
        elif sd=='Qulupneyli To\'rt':
            salom2.insert(END,'Qulupneyli To\'rt 40.000')
            e10.insert(e1,'+40000')
        elif sd=='Bananli piroq':
            salom2.insert(END,'Bananli piroq 35.000')
            e10.insert(e1, '+35000')
        elif sd=='Plitka':
            salom2.insert(END,'Plitka 14.000')
            e10.insert(e1,'+14000')
        elif sd=='Shkalatli to\'rt':
            salom2.insert(END,'Shkalatli to\'rt 45.000')
            e10.insert(e1,'+45000')
    def f(event):
        s = b.get()
        if s == "Shrinlik":
            b1['values'] = ['Qulupneyli To\'rt','Bananli piroq','Plitka','Shkalatli to\'rt']
            b1.set('Shrinlik')
        elif s == "Cofe":
            b1.set('Cofe')
            b1['values'] = ['Latte', 'Americano', 'Espresso', 'Cappuccino', 'Mocco', 'Arabica', 'Cacao']

    def V1():
        e3 = e10.get()
        if e3 == '':
            showinfo(master=ab,title='narx', message=f'jami 0 so`m')
        else:
            e2 = eval(e3)
            showinfo(master=ab,title='narx', message=f'jami {e2}so`m')


    b12 = CTkButton(master=ab,width=15,command=gh,
                  corner_radius=42,
                  text='tanlash')
    b12.place(x=710,y=130)
    salom2=Listbox(ab,width=24,height=12)
    salom2.place(x=780,y=200)
    b3 = CTkButton(master=ab, text='Xisoblash', command=V1)
    b3.place(x=800, y=400)
    days = ["Shrinlik",'Cofe']
    s2 = StringVar(value='Menyu')
    b = ttk.Combobox(ab, values=days, textvariable=s2)
    b.place(x=800, y=40)
    b.bind("<<ComboboxSelected>>", f)
    b1 = ttk.Combobox(ab)
    b1.place(x=800, y=130)
    e10=ttk.Entry(master=ab)
    e10.place(x=100000000000000000000000000,y=1000000000000000000000000000000)
l=Label(text='Cofe xush kelibsiz',font=('Arial',50))
l.place(x=230,y=150)
b=CTkButton(master=a,text='kirish',command=j)
b.place(x=450,y=400)
a.mainloop()
