from tkinter import *
from customtkinter import *
a=Tk()
a.title()
a.geometry('500x500')
def q():
      t.delete('1.0', END)
      p=e.get()*int(e1.get())
      g = e.get() + e.sep
      t.insert(END,str(p)+g)
e=CTkEntry(master=a,width=125,placeholder_text='So\'z',placeholder_text_color='red')
e.place(x=10,y=10)
e.sep='\n'
e1=CTkEntry(master=a,width=125,placeholder_text='Son',placeholder_text_color='red')
e1.place(x=10,y=40)
t=Text(width=50,height=20)
t.pack(expand=1)
b=Button(width=10,height=1,command=q)
b.place(y=20,x=145)
a.mainloop()