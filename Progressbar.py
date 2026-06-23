from  tkinter import *
from  tkinter import ttk
a=Tk()
a.title('nomlar')
a.geometry('250x250')
ttk.Progressbar(orient='vertical',length=100, value=40).pack(pady=5)
ttk.Progressbar(orient='horizontal',length=100, value=40).pack(pady=5)
a.mainloop()