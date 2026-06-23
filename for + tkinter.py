from tkinter import *
from tkinter import ttk
a = Tk()
a.title("METANIT.COM")
a.geometry("250x250")
for c in range(3): a.columnconfigure(index=c, weight=1)
for r in range(3): a.rowconfigure(index=r, weight=1)
for r in range(3):
    for c in range(3):
        b = ttk.Button(text=f"{r},{c}")
        b.grid(row=r, column=c)
a.mainloop()