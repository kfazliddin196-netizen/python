from  tkinter import *
from tkinter import ttk
def a(label_text):
  b=ttk.Frame(borderwidth=1,relief=SOLID,padding=[8,10])
  l=ttk.Label(b,text=label_text)
  l.pack(anchor=NW)
  e=ttk.Entry(b)
  e.pack(anchor=NW)
  return b
c=Tk()
c.title('Metanli.com')
c.geometry('250x200')
d=a('FIO ism')
d.pack(anchor=NW,fill=X,padx=5,pady=5)
c.mainloop()
