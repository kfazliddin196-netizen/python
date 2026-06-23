from turtle import *
bgcolor('black')
pensize(0)
tracer(50)
hideturtle()
for i in range(301):
 for c in 'red','blue':
  color(c)
  circle(i+2,150)
  left(80)
done()