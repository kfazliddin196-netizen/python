from tkinter import *
from tkinter import ttk
from tkinter.messagebox import  showinfo,askyesno
a=Tk()
a.title('...')
a.geometry('1000x800')
a.configure(bg='red')
def c():
    r=askyesno(title='karta',message='pulingiz otkazilsinmi')
    if r:
        showinfo('javobi','o\' tkazildi')
    else:
        showinfo('javobi','o\'tkazilmadi')

d=ttk.Button(text='click',command=c)
d.pack(expand=True)
a.mainloop()