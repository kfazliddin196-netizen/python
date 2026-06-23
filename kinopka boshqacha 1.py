from tkinter import *
from tkinter import ttk
a = Tk()
a.title("METANIT.COM")
a.geometry("250x200")
def single_click(event):
    b["text"] = "Single Click"
def double_click(event):
    b["text"] = "Double Click"
b = ttk.Button(text="Click")
b.pack(anchor=CENTER, expand=1)
b.bind("<ButtonPress-1>", single_click)
b.bind("<Double-ButtonPress-1>", double_click)
a.mainloop()