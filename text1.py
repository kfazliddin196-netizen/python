from tkinter import *
from tkinter import ttk
a=Tk()
a.title()
a.geometry('600x600')
t=ttk.Treeview(show='tree')
t.pack(expand=True,fill=BOTH)
t.insert("",END,iid=1,text='23.11')
t.insert("",END,iid=2,text='23.14')
t.insert("",END,iid=3,text='23.17')
t.insert(1, index=END,text='Tom')
t.insert(2, index=END,text='Sam')
t.insert(3, index=END,text='Salom')
a.mainloop()