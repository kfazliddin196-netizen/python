from tkinter import *
from tkinter import ttk
a=Tk()
a.title('Fazliddin')
a.geometry('1000x1000')
a.configure(bg='green')
for c in range(3): a.columnconfigure(index=c, weight=1)
for r in range(3): a.rowconfigure(index=r, weight=1)
for r in range(3):
    for c in range(3):
        e=ttk.Button(text=f"({r},{c})")
        e.grid(row=r,column=c,ipady=6,padx=4,pady=4)
a.mainloop()

