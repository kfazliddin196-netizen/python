from customtkinter import *
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo,showerror
def o():
    a = Toplevel()
    a.title('')
    a.geometry('290x440')

    im = PhotoImage(file='ku.png')
    la = Label(a, image=im)
    la.place(x=0, y=0, relwidth=1, relheight=1)

    def U8(event):
        e1.config(state=NORMAL)
        e1.delete(0, END)
    e1 = ttk.Entry(a, width=13)
    e1.place(x=106, y=150)
    e1.insert(0, "Email")
    e1.config(state=DISABLED)
    e1.bind('<Button-1>', U8)

    def U8(event):
        e2.config(state=NORMAL)
        e2.delete(0, END)
    e2 = ttk.Entry(a, width=13)
    e2.place(x=106, y=200)
    e2.insert(0, "Paro'l")
    e2.config(state=DISABLED)
    e2.bind('<Button-1>', U8)
    def G2():
        if e1.get() == "kfazliddin196@gmail.com" and e2.get()=='Kom1lov':
             showinfo(title='Xabar',message='Xisobga kirildi')
        elif e1.get() != "kfazliddin196@gmail.com" and e2.get()!='Kom1lov':
             showerror(title='Xabar',message='Email yoki Paro\'l xato')
    b = ttk.Button(a, text='kirish', width=12,command=G2)
    b.place(x=106, y=250)
    a.mainloop()
f = CTk()
f.title('')
f.geometry('1000x1000')

s = CTkTabview(master=f, width=600, height=400,
               fg_color="silver",
               text_color="black", border_color="green", border_width=3,
               segmented_button_fg_color="green",
               segmented_button_selected_color="white",
               segmented_button_selected_hover_color="red",
               segmented_button_unselected_color="grey38",
               segmented_button_unselected_hover_color="white",)
s1 = s.add('Bosh sahifa')
s2 = s.add('Do\'kon')
r=PhotoImage(file='l1.png')
b1=ttk.Button(master=s2,image=r)
b1.place(x=10,y=10)
s4 = s.add('Biz haqimizda')
#a4................................................
im1 = PhotoImage(file='1Kitob.png')
la = Label(s4, image=im1)
la.place(x=0, y=0, )
F12=PhotoImage(file='123.png')
la12=Label(s4,image=F12)
la12.place(x=250,y=2,)
F13=PhotoImage(file='Rasm.png')
la13=Label(s4,image=F13)
la13.place(x=250,y=240,)
#...................................................
s5 = s.add('Aloqa')
#s5 Aloqa..........................................................................................................
n=PhotoImage(file='k1.png')
n1=Label(s5,image=n)
n1.place(x=0,y=6)
def g(event):
    e2.config(state=NORMAL)
    e2.delete(0, END)
e2=Entry(s5,width=25)
e2.place(x=30,y=180,height=50)
e2.insert(0, "Enter your name")
e2.config(state=DISABLED)
e2.bind('<Button-1>', g)
def g1(event):
    e3.config(state=NORMAL)
    e3.delete(0, END)
e3=Entry(s5,width=25)
e3.place(x=215,y=180,height=50)
e3.insert(0, "Enter your email")
e3.config(state=DISABLED)
e3.bind('<Button-1>', g1)
def g2(event):
    e4.config(state=NORMAL)
    e4.delete(0, END)
e4=Entry(s5,width=25)
e4.place(x=400,y=180,height=50)
e4.insert(0, "Subject(Optional)")
e4.config(state=DISABLED)
e4.bind('<Button-1>', g2)
t=CTkTextbox(master=s5,
             border_color='yellow',
             border_width=3,
             fg_color='grey',
             text_color='white',
             scrollbar_button_color='black',
             scrollbar_button_hover_color='white',height=100,width=440)
t.place(x=30,y=240)
def l9():
    name= e2.get().strip()
    email= e3.get().strip()
    supject= e4.get().strip()
    message= t.get(0.0, 'end').strip()
    if name and email and supject and message:
        showinfo(title='Xabar', message='Xabaringiz uchun rahmat')
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        t.delete(0.0, 'end')
    else:
        showerror(title='Xabar', message='Ma\'lumotlarni to\'ldiring')
a=CTkButton(master=s5,width=100,height=100,command=l9,text='Yuborish')
a.place(y=240,x=480)
l0=CTkLabel(master=s5,width=200,height=25,text_color='black',text='Biz bilan bog\'lansh')
l0.place(y=154,x=200)
#...............................................................................................
s.pack(padx=200, pady=40)

m = CTkEntry(master=f,
             corner_radius=3, width=450)
m.place(x=382, y=6)
b1 = CTkButton(master=f,
                text='Topish',
               hover_color='black',width=70)
b1.place(x=835, y=6)

b2 = CTkButton(f, text='Kirish',width=70 ,command=o)
b2.place(x=910, y=6)

f.mainloop()
