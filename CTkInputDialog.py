from customtkinter import *
a=CTk()
a.title("custom tkinter- dialog")
a.geometry("700x500")
def d():
    dialog=CTkInputDialog(title="dialog")
    t=dialog.get_input()
    if t:
        l.configure(text=f" Parol {t}")
    else:
        l.configure(text=f" Parol kiritilmadi")
b3=CTkButton(master=a,text="parol kiriting",command=d)
b3.place(x=20,y=90)
l=CTkLabel(master=a,text="parolni kiritish uchun tugmani bosing")
l.place(x=10,y=10)
a.mainloop()