from tkinter import *
from tkinter import ttk
a=Tk()
a.title('<>')
a.geometry('500x500')
p=[('Komilov','Fazliddin',16),('To\'raqulov','Ozodbek',16),('Umrzoqov','Ismoil',16)]
c=('Familya','Ism','Yosh')
d=ttk.Treeview(columns=c,show='headings')
d.heading('Familya',text='Familya')
d.heading('Ism',text='Ism')
d.heading('Yosh',text='Yosh')
d.pack(fill=BOTH,expand=True)
for p in p:
 d.insert('',END,values=p)
a.mainloop()
