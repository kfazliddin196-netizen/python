from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo

a = Tk()
a.title("METANIT.COM")
a.geometry("250x200")
a.configure(bg='red')
def open_info():
    showinfo(title="Malumot",
             message="Malumotlar xabar")
def open_warning():
    showwarning(title="Ogohlantrish", 
                message="ogohlantrish haqida habar")
def open_error():
    showerror(title="Xato",
              message="xato haqida habar")
info_button = ttk.Button(text="Malumot", command=open_info)
info_button.pack(anchor="center", expand=1)

warning_button = ttk.Button(text="ogohlantrish", command=open_warning)
warning_button.pack(anchor="center", expand=1)

error_button = ttk.Button(text="xato", command=open_error)
error_button.pack(anchor="center", expand=1)
a.mainloop()