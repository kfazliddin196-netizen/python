from tkinter import *
from tkinter import ttk
a=Tk()
a.title()
a.geometry()
people=[('Tohir',38,'tohir','tohir@email'),('Bobir',42,'bob@email.com'),('Fazliddin',16,'kfazliddin.com')]
c=('ism','Yosh','email')
t=ttk.Treeview(columns=c,show='headings')
t.heading('ism',text='ism')
t.heading('Yosh',text='Yosh')
t.heading('email',text='email')
t.pack(fill=BOTH,expand=True)
for person in people:
    t.insert('',END,values=person)
a.mainloop()
