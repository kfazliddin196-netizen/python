from tkinter import *
from tkinter.messagebox import showinfo
from customtkinter import *
import random

a = Tk()
a.title('Cofe')
a.geometry('800x600')


def j():
    ab = Toplevel()
    ab.title('Cofe')
    ab.configure(bg='brown')
    ab.geometry('800x600')

    def fm():
        ent = e.get()
        if ent.isdigit() and 1 <= int(ent) <= 10:
            random_text = random.randint(100000, 999999)
            t2.insert(END, f'ID: {random_text}')
            price = int(ent) * 2000
            t.insert(END, f"{price} so'm")
            salom2.insert(END, ent)
            showinfo(title='Xabar', message='Bu raqamni unutmang')
        else:
            showinfo(title='Xabar', message='Maksimal 10 ta chipta olish mumkin')

    lbl = Label(ab, text='Nechta raqam tanlamoqchisiz?', font=('Arial', 16), bg='brown', fg='white')
    lbl.pack(pady=20)

    e = CTkEntry(master=ab, border_color='red', width=200, corner_radius=10, placeholder_text='Nechta raqam tanlisiz')
    e.pack()

    btn_e = CTkButton(master=ab, text='Kiritish', command=fm)
    btn_e.pack(pady=10)

    t2 = Listbox(ab, width=30, height=8)
    t2.pack(side=LEFT, padx=20, pady=20)

    t = Listbox(ab, width=30, height=8)
    t.pack(side=LEFT, padx=20, pady=20)

    salom2 = Listbox(ab, width=10, height=8)
    salom2.pack(side=LEFT, padx=20, pady=20)

    def V1():
        total = sum(int(item) * 2000 for item in salom2.get(0, END))
        showinfo(master=ab, title='Narx', message=f'Jami: {total} so`m')

    bt = CTkButton(master=ab, text='Hisoblash', command=V1, width=100)
    bt.place(x=650, y=400)


lbl = Label(a, text='Metroga xush kelibsiz', font=('Arial', 24))
lbl.pack(pady=50)

btn = CTkButton(master=a, text='Kirish', command=j)
btn.pack()

a.mainloop()
