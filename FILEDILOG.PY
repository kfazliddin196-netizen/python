from tkinter import *
from tkinter import ttk
from tkinter import filedialog
a = Tk()
a.title("METANIT.COM")
a.geometry("650x800")
a.grid_rowconfigure(index=0, weight=1)
a.grid_columnconfigure(index=0, weight=1)
a.grid_columnconfigure(index=1, weight=1)
t = Text(width=69,height=22)
t.place(x=50,y=15)
def o():
    f = filedialog.askopenfilename()
    if f != "":
        with open(f, "r") as file:
            text = file.read()
            t.delete("1.0", END)
            t.insert("1.0", text)
def s():
    f= filedialog.asksaveasfilename()
    if f != "":
        text = t.get("1.0", END)
        with open(f, "w") as file:
            file.write(text)
o = ttk.Button(width=45,text="FAYLNI OCHISH", command=o)
o.place(x=50,y=370)
s = ttk.Button(width=45,text="FAYLNI SAXRANIT QILISH", command=s)
s.place(x=325,y=370)
a.mainloop()