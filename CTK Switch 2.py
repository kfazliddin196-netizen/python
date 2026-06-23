from customtkinter import *
a=CTk()
a.title("switch")
a.geometry("500x500")
b=StringVar(value="on")
l=CTkSwitch(master=a,text="salom",)
l.place(x=100,y=100)
a.mainloop()