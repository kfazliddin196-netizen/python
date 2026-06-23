from customtkinter import *
a=CTk()
a.title("custom tkinter - textbox")
a.geometry("700x500")
def delete():
    t.delete(0.0, 'end')
def copy():
    global r
    r = t.get(0.0 , "end")
def paste():
    if r:
        t.insert('end', r)
    else:
        t.insert('end', "text yoq")
t = CTkTextbox(master=a,
               border_color="yellow",
               border_width=3,
               fg_color="grey",
               text_color="white",
               scrollbar_button_color="black",
               scrollbar_button_hover_color="white")
t.pack(pady=15)
b = CTkButton(master=a, text='delete', command=delete)
b.place(x=20, y=20)
b2 = CTkButton(master=a, text="copy", command=copy)
b2.place(x=20, y=55)
b3 = CTkButton(master=a, text="paste", command=paste)
b3.place(x=20, y=90)
a.mainloop()