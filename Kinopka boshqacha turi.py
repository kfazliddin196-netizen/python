from tkinter import *
from tkinter import ttk
a = Tk()
a.title("METANIT.COM")
a.geometry("250x200")
def e(event):
    b["text"] = "Entered"
def l(event):
    b["text"] = "Left"
b = ttk.Button(text="Click")
b.pack(anchor=CENTER, expand=1)
b.bind("<Enter>", e)
b.bind("<Leave>", l)
a.mainloop()