import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(3)

radius = float(input("Enter radius: "))


t.penup()
t.backward(radius*2)
t.pendown()


t.color("blue")
t.circle(radius)
t.penup()
t.forward(radius*2 + radius/5)
t.pendown()
t.color("black")
t.circle(radius)
t.penup()
t.forward(radius*2 + radius/5)
t.pendown()
t.color("red")
t.circle(radius)
t.penup()


t.left(180)
t.forward(radius + radius/10)
t.right(90)
t.forward(radius)
t.left(90)


t.pendown()
t.color("green")
t.circle(radius)
t.penup()
t.forward(2*radius + radius/5)
t.pendown()
t.color("yellow")
t.circle(radius)



turtle.done()