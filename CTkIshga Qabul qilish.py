from customtkinter import *
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import *
a = CTk()
a.title("Title")
a.geometry("800x650")
set_appearance_mode('dark')
t = CTkTextbox(master=a, width=350, height=210)
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

def k():
    en = e.get().strip()
    name = e1.get().strip()
    email = e2.get().strip()
    parol = e3.get().strip()

    if en and name and email and parol:
        showinfo(title='Xabar', message='Ro\'yxatdan o\'tingiz')
        t.insert(END, 'Familya: '+en + "\n" 'Ism: '+ name + "\n" 'Email: '+ email + "\n" 'Paro\'l: '+ parol + "\n")
        e.delete(0, END)
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
    else:
        showerror(title='Xabar', message='Ma\'lumotlarni to\'ldiring')
def g():
    t.delete(0.0,'end')
la=CTkLabel(master=a,text='Familya')
la.place(x=150,y=-1)
e = CTkEntry(master=a, width=300, border_color='red', corner_radius=32)
e.place(x=20, y=25)
la=CTkLabel(master=a,text='Ism')
la.place(x=160,y=53)
e1 = CTkEntry(master=a, width=300, border_color='red', corner_radius=32)
e1.place(x=20, y=80)
la=CTkLabel(master=a,text='Email')
la.place(x=160,y=109)
e2 = CTkEntry(master=a, width=300, border_color='red', corner_radius=32)
e2.place(x=20, y=135)
la=CTkLabel(master=a,text='Paro\'l')
la.place(x=160,y=165)
e3 = CTkEntry(master=a, width=300, border_color='red', corner_radius=32)
e3.place(x=20, y=190)
b1 = CTkButton(width=226, master=a, corner_radius=32, text='open_file', command=open_file, hover_color='black')
b1.place(x=35, y=290)
b2 = CTkButton(width=226, master=a, corner_radius=32, text='save_file', command=save_file, hover_color='black')
b2.place(x=450, y=290)
b = CTkButton(master=a, width=680, corner_radius=32, text="Ro'yhatdan o'tish", command=k, hover_color='black')
b.place(x=20, y=245)
b3=CTkButton(master=a,width=40,text='',command=g)
b3.place(x=720,y=20)
la=CTkLabel(master=a,text="o'chirish")
la.place(x=720,y=50)
a.mainloop()
