from tkinter import *
from tkinter.scrolledtext import ScrolledText
a = Tk()
a.title("METANIT.COM")
a.geometry("250x150")
st = ScrolledText(a, width=50, height=10)
st.pack(fill=BOTH, expand=True)
a.mainloop()