from customtkinter import *
set_appearance_mode("dark")  # dark / light
a = CTk()
a.title("custom tkinter - birinchi dars")
a.geometry("500x500")
# a.iconbitmap("code icon.ico")
def but_leb():
    leb.configure(text="salom")
b = CTkButton(master=a, text="Click me",
              corner_radius=32,
              fg_color="transparent",
              hover_color="#4158D0",
              border_color="#FFCC70",
              border_width=2, command=but_leb)
b.pack(pady=100)
leb = CTkLabel(master=a,
               text="text...",
               font=("Arial", 20),
               text_color="red",
               bg_color="green")
leb.pack()
a.mainloop()
