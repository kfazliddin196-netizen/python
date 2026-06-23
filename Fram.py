from tkinter import *
from tkinter import ttk

a = Tk()
a.title("METANIT.COM")
a.geometry("250x200")
f = ttk.Frame( relief=SOLID, padding=[8, 10])
n = ttk.Label(f, text="Введите имя")
n.pack(anchor=NW)

e = ttk.Entry(f)
e.pack(anchor=NW)

f.pack(anchor=NW, fill=X, padx=5, pady=5)

a.mainloop()