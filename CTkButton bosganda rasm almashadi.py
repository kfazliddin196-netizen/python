from customtkinter import *
from tkinter import *
def change_image():
    b.config(image=p2)

# Create a custom Tkinter window
a = CTk()
a.geometry('1366x768')

# Load images
p1 = PhotoImage(file='k1.png')  # Initial image for the button
p2 = PhotoImage(file='ku.png')  # Image to be displayed after button click

# Create a button with initial image
b = Button(a, image=p1,width=200,height=200 ,command=change_image)
b.place(x=10, y=30)

# Run the Tkinter event loop
a.mainloop()
