from tkinter import *
from tkinter import ttk
a = Tk()
a.geometry("300x200")
def on(event):
    l.config(text=c.get())
l = Label( text="Choose an option:")
l.pack()
s= StringVar()
c= ttk.Combobox()
c['values'] = ('Option 1', 'Option 2', 'Option 3')
c.pack()
c.bind("<<ComboboxSelected>>", on)
a.mainloop()
