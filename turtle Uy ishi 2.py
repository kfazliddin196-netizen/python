import turtle
c=turtle.Turtle()
a=turtle.Screen()
c.hideturtle()
a.bgcolor('black')
c.color('green')
c.speed(0)
for i in range(150):
  c.left(110)
  c.right(300)
  c.forward(300)
a.mainloop()