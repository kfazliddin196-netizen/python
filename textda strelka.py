from tkinter import *
from tkinter import ttk
a = Tk()
a.title("METANIT.COM")
a.geometry("250x200")
a.grid_columnconfigure(0, weight = 1)
a.grid_rowconfigure(0, weight = 1)
e = Text(wrap = "none")
e.grid(column = 0, row = 0, sticky = NSEW)
y = ttk.Scrollbar(orient = "vertical", command = e.yview)
y.grid(column = 1, row = 0, sticky = NS)
x = ttk.Scrollbar(orient = "horizontal", command = e.xview)
x.grid(column = 0, row = 1, sticky = EW)
e["yscrollcommand"] = y.set
e["xscrollcommand"] = x.set
a.mainloop()