from tkinter import *
a = Tk()
a.title("dars2")
a.geometry("1500x1500")
a.configure(bg = "cyan")
def f():
    a = f1.curselection()
    if a == (0,):
        m.insert(END,"Kitob-5000 som",)
    elif a==(1,):
        m.insert(END,"Daftar-10000 som")
    elif a==(2,):
        m.insert(END,"Ruchka-2000 som")
    elif a==(3,):
        m.insert(END,"Qalam-7000 som")
    elif a==(4,):
        m.insert(END,'Popka-50000 som')
    elif a==(5,):
        m.insert(END,'Penal-15000 som')
    elif a==(6,):
        m.insert(END,'Guvash-10000 som')
menyu=["kitob","daftar","ruchka","qalam",'popka','penal','guvash']
menyu_var=Variable(value=menyu)
f1=Listbox(listvariable=menyu_var,width=25,height=15,font=100,bg='red')
f1.place(x=10,y=10)
m=Listbox(width=25,height=15,font=100,bg='red')
m.place(x=500,y=10)
b=Button(bg="red",text="click me",width=10,height=2,font=15,command=f)
b.place(x=50,y=400)
a.mainloop()