from customtkinter import *
from tkinter.messagebox import showinfo, showwarning
from tkinter import *
from tkinter import ttk
a=CTk()
a.title("play market")
a.geometry("1000x1000")
set_appearance_mode("dark")
def Ulash():
    p1 = int(p.get() * 101)
    l.configure(text=f"Download: {p1}%")
    if p1 < 100:
        a.after(100, Ulash)
def f():
    p.start()
    Ulash()
    showinfo(title='xabar',message='Yuklanvoti')
def f1():
    p.stop()
    showwarning(title='Xabar',message='Yuklash to\'xtatildi')
l = CTkLabel(master=a, text='Download: 0%')
l.place(x=350, y=30)
b1=CTkButton(master=a,corner_radius=32,hover_color='red',fg_color='blue',text='start',command=f,width=220, height=30, )
b1.place(x=330, y=150)
s3 = CTkButton(master=a,corner_radius=32,fg_color='blue',hover_color='green', text="Stop / Pauza", width=220, height=30,command=f1)
s3.place(x=330, y=200)
p = CTkProgressBar(master=a, orientation="horizontal", determinate_speed=0.5, width=225)
p.place(x=330, y=10)
p.set(0) # set progressbar
leb2 = CTkLabel(master=a, text="Hill Climb Racing", font=("Arial", 20))
leb2.place(x=45, y=210)
p14 = PhotoImage(file="image(3).png")
leb3 = ttk.Label(image=p14)
leb3.place(x=50, y=45)
p2 = PhotoImage(file="images (1) (1).png")
leb4 = ttk.Label(image=p2)
leb4.place(x=50, y=370)
p3 = PhotoImage(file="images (1).png")
leb5 = ttk.Label(image=p3)
leb5.place(x=380, y=370)
a.mainloop()