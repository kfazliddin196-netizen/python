from customtkinter import *
set_appearance_mode("dark")

a=CTk()
a.title("custom tkinter - button")
a.geometry("500x500")

b = CTkButton(master=a, text="hello!")
b.place(x=10, y=10)

b2 = CTkButton(master=a,
               text="ikkinchi tugma",
               text_color="yellow")
b2.place(x=10, y=50)

b3 = CTkButton(master=a,
               text="uchinchi tugma",
               text_color="yellow",
               corner_radius=30)
b3.place(x=10, y=90)

b4 = CTkButton(master=a,
               text="to'rtinchi tugma",
               text_color="white",
               corner_radius=30,
               fg_color="green")
b4.place(x=10, y=130)

b5 = CTkButton(master=a,
               text="beshinchi tugma",
               text_color="yellow",
               corner_radius=30,
               fg_color="green",
               hover_color="blue")
b5.place(x=10, y=170)

b6 = CTkButton(master=a,
               text="oltinchi tugma",
               text_color="yellow",
               corner_radius=30,
               fg_color="green",
               hover_color="orange",
               border_color="red",
               border_width=2)
b6.place(x=10, y=210)
b = CTkButton(master=a, text="Click me",
              corner_radius=32,
              fg_color="transparent",
              hover_color="#4158D0",
              border_color="#FFCC70",
              border_width=2)
b.place(x=10, y=250)
a.mainloop()