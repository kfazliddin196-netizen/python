from tkinter import *
import turtle


def d():
    # Create or clear turtle screen
    screen = turtle.Screen()
    screen.reset()

    # Create a turtle for drawing




a = Tk()
a.geometry('250x400')

# Create a button
b = Button(a, text='Draw Square', width=20, height=2, command=d)
b.place(x=20, y=40)

a.mainloop()
