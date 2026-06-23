from tkinter import *
from tkinter import ttk

a = Tk()
a.title("METANIT.COM")
a.geometry("1000x800")

python = "Python"
java = "Java"
csharp = "C#"

l = StringVar(value=java)

h = ttk.Label(textvariable=l)
h.pack(anchor=NW)

p = PhotoImage(file="img.png",width=100,height=100)
c = PhotoImage(file="img_1.png",width=100,height=100)
j = PhotoImage(file="img_2.png",width=100,height=100)
b = ttk.Radiobutton(value=python, variable=l, image=p)
b.pack(anchor=NW)

f = ttk.Radiobutton(value=csharp, variable=l, image=c)
f.pack(anchor=NW)

m = ttk.Radiobutton(value=java, variable=l, image=j)
m.pack(anchor=NW)

a.mainloop()