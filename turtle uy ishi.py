import turtle
c=turtle.Turtle()
a=turtle.Screen()
c.hideturtle()
a.bgcolor('black')
c.color('red')
c.speed(0)
for i in range(60):
    c.circle(150,10)
    c.forward(20)
    c.left(100)
    c.circle(50)
a.mainloop()