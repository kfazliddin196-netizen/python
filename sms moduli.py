from tkinter import *

a = Tk()
a.title("Two Listboxes with Entries")
a.geometry('850x600')
a.configure(bg='black')

def right(text, width):
    return text.rjust(width)
def left(text, width):
    return text.ljust(width)

def j():
    if e.get():
        text = right(e.get(), 35)
        l.insert(END, text)
        l1.insert(END, left(e.get(), 30))
        e.delete(0, END)  # Entry tozalash

def k():
    if e1.get():
        text = left(e1.get(), 30)
        l.insert(END, text)
        l1.insert(END, right(e1.get(), 35))
        e1.delete(0, END)  # Entry tozalash

l = Listbox(width=35, height=25, font=("Courier", 12))
l.place(x=50, y=20)

l1 = Listbox(width=35, height=25, font=("Courier", 12))
l1.place(x=450, y=20)

e = Entry(width=42)
e.place(x=50, y=510)
e.bind('<Return>', lambda event: j())  # "Enter" tugmasi bosilganda j() funksiyasini chaqirish

e1 = Entry(width=42)
e1.place(x=450, y=510)
e1.bind('<Return>', lambda event: k())  # "Enter" tugmasi bosilganda k() funksiyasini chaqirish

b = Button(width=5, text="Add", command=j)
b.place(x=355, y=510)

b2 = Button(width=5, text="Add", command=k)
b2.place(x=755, y=510)
a.mainloop()
