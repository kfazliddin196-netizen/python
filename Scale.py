from tkinter import *
from tkinter import ttk
a = Tk()
a.title("_nabiy._")
a.configure(bg="#dbf9b8")
a.geometry("780x640")
verticalscale = ttk.Scale(orient=VERTICAL, length=200, from_=1.0, to=100.0, value=50)
verticalscale.pack()
horizontalscale = ttk.Scale(orient=HORIZONTAL, length=200, from_=1.0, to=100.0, value=30)
horizontalscale.pack()
a.mainloop()
