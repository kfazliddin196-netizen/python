import turtle,random
c=turtle.Turtle()
c.goto(-250,250)
c.goto(250,250)
a=turtle.Screen()
c.hideturtle()
a.bgcolor('black')
c.color('green')
c.speed(0)
c.up()
c.goto(250,250)
c.down()
c.goto(250,-250)
c.goto(-250,-250)
c.goto(-250,250)
c.goto(250,250)
d=turtle.Turtle()
d.shape('circle')
d.up()
d.goto(0,0)
d.color('red')
rx=random.randint(-240,240)
ry=random.randint(-240,240)
d.goto(rx,ry)
sx=6
sy=3
while True:
    x,y=d.position()
    if x+sx>=250 or x+sx<=-250:
        sx=-sx
    if sy+y>=250 or y+sy<=-250:
        sy=-sy
    d.goto(x+sx,y+sy)
a.mainloop()