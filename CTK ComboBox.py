from customtkinter import *
a=CTk()
a.title("LEFT 4 DEAD 2")
a.geometry("500x500")
def k(b):
       l.configure(text=b,text_color=b)
q=['red',"green","yellow"]
c=CTkComboBox(master=a,values=q,command=k)
c.place(x=100,y=10)
l=CTkLabel(master=a,)
l.place(x=100,y=50)
a.mainloop()