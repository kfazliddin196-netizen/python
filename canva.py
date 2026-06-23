from tkinter import *
def draw_person(event):
    x = event.x
    y = event.y
    # Head
    canvas.create_oval(x - 20, y - 40, x + 20, y + 20, fill="lightblue")
    # Body
    canvas.create_line(x, y + 20, x, y + 100, fill="lightblue", width=5)
    # Arms
    canvas.create_line(x - 20, y + 40, x - 50, y + 80, fill="lightblue", width=5)
    canvas.create_line(x + 20, y + 40, x + 50, y + 80, fill="lightblue", width=5)
    # Legs
    canvas.create_line(x, y + 100, x - 20, y + 160, fill="lightblue", width=5)
    canvas.create_line(x, y + 100, x + 20, y + 160, fill="lightblue", width=5)

root = Tk()
root.title("Draw a Person")

canvas = Canvas(root, width=400, height=400, bg="white")
canvas.pack() 

canvas.bind("<Button-1>", draw_person)

root.mainloop()
