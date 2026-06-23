from tkinter import *
from tkinter import ttk
a = Tk()
a.title("METANIT.COM")
a.geometry("250x200")
for r in range(3):
    for c in range(3):
        b = ttk.Button(text=f"{r},{c}")
        b.grid(row=r, column=c)
a.mainloop()