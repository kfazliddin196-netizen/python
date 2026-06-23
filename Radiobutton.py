from tkinter import *
from tkinter import ttk

root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")

position = {"padx":6, "pady":6, "anchor" : NW}
language=['pyhton','javascript','java','c#']
selected_language=StringVar()

header=ttk.Label(text='tilni tanlang')
header.pack(**position)

def select():
    header.config(text=f'tanlang{selected_language.get()}')

for lang in language:
    lang_btn=ttk.Radiobutton(text=lang,value=lang,
            variable=selected_language,command=select)
    lang_btn.pack(**position)
root.mainloop()