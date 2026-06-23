from customtkinter import *
a=CTk()
a.title("switch")
a.geometry("500x500")
def k():
    l.configure(text="hello")
b=StringVar(value="on")
l=CTkLabel(master=a,width=10)
l.place(x=100,y=10)
s=CTkSwitch(master=a,text="salom",command=k)
s.place(x=100,y=100)
a.mainloop()