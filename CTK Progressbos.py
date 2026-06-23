from customtkinter import *
a=CTk()
a.title("salom")
a.geometry("500x500")
p=CTkProgressBar(master=a,fg_color="red",
                 corner_radius=32)
p.place(x=10,y=10)
a.mainloop()