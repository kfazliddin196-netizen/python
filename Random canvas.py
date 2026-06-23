import random
from tkinter import *
a = Tk()
a.title("METANIT.COM")
a.geometry("1000x1200")
a.configure(bg='black')
c = Canvas(bg="white", width=1000, height=1000,)
c.pack(anchor=CENTER, expand=1)
c.configure(bg='black')
def sh():
    c.delete("red")
    for i in range(5):
        x = random.randint(10, 810)
        y = random.randint(10, 300)
        x1 = x + 70
        y1 = y + 70
        c.create_oval(x, y, x1, y1, fill='red', outline='red', tags="red")
def ch():
    c.delete("red")
    for i in range(5):
        x1 = random.randint(10, 810)
        y1 = random.randint(10, 300)
        x2 = x1 + 70
        y2 = y1 + 70
        c.create_oval(x1, y1, x2, y2,  fill='blue', outline='blue', tags="red")
b = Button(width=10, height=2, bg='blue',command=ch)
b.place(x=550, y=500)
b1 = Button(width=10, height=2, bg='red',command=sh)
b1.place(x=450, y=500)
a.mainloop()
