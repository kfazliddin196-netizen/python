from customtkinter import *
from tkinter.messagebox import showinfo
a=CTk()
a.title("custom")
a.geometry("500x500")
def ss():
    if m.get() == 1:
        showinfo(title="xabar", message="yondi")
    else:
        showinfo(title="xabar", message="o'chdi")
m = IntVar()
s = CTkSwitch(master=a,
              text="",
              text_color="red",
              fg_color="black",
              button_color="green",
              progress_color="red",
              border_color="yellow",
              button_hover_color="cyan",
              variable=m,
              command=ss)
s.place(x=10, y=10)
a.mainloop()