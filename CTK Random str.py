from customtkinter import *
import random
set_appearance_mode("dark")  # dark / light
a = CTk()
a.title("custom tkiinter - birinchi dars")
a.geometry("500x500")
def b2():
    t = ["Ozodbek", "Fazliddin", "Ismoil"]
    r = random.choice(t)
    l.configure(text=r)

b = CTkButton(master=a, text="Click me",
              corner_radius=32,
              fg_color="transparent",
              hover_color="#4158D0",
              border_color="#FFCC70",
              border_width=2, command=b2)
b.pack(pady=100)

l = CTkLabel(master=a,
               text="text...",
               font=("Arial", 20),
               text_color="red",
               bg_color="green")
l.pack()

a.mainloop()
