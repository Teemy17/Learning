# Q1

import turtle

t = turtle.Turtle()

p0x = float(input("Enter x-cord for p0: "))
p0y = float(input("Enter y-cord for p0: "))
p1x = float(input("Enter x-cord for p1: "))
p1y = float(input("Enter y-cord for p1: "))
p2x = float(input("Enter x-cord for p2: "))
p2y = float(input("Enter y-cord for p2: "))

if abs(p2x-p1x) > abs(p2x-p0x):
    print("p2 is on the left side of the line between p0 & p1")
elif abs(p2x-p0x) > abs(p2x-p1x):
    print("p2 is on the right side of the line between p0 & p1")
else:
    print("p2 is exactly at the middle of the line")

t.penup()
t.goto(p0x,p0y)
t.write("p0")
t.pendown()
t.goto(p1x,p1y)
t.write("p1")
t.penup()
t.goto(p2x,p2y)
t.pendown()
t.write("p2")
t.dot(10, color="red")
t.hideturtle()

turtle.done()

# Q2

import turtle
import math

p1x = float(input("Enter x-cord for rectangle 1: "))
p1y = float(input("Enter y-cord for rectangle 1: "))
p2x = float(input("Enter x-cord for rectangle 2: "))
p2y = float(input("Enter y-cord for rectsngle 2: "))
width_rec1 = float(input("Enter width of rectangle 1: "))
height_rec1 = float(input("Enter height of rectangle 1: "))
width_rec2 = float(input("Enter width of rectangle 2: "))
height_rec2 = float(input("Enter height of rectangle 2: "))


distance_x = math.sqrt(p1x**2 + p2x**2)
distance_y = math.sqrt(p1y**2 + p2y**2)

distance_width = (width_rec1/2) + (width_rec2/2) 
distance_height = (height_rec1/2) + (height_rec2/2) 

if distance_x > distance_width:
    print("Rectangle2 does not overlap Rectangle1")
elif distance_y  > distance_height:
    print("Rectangle2 does not overlap Rectangle1")
elif distance_x < distance_width  and distance_y  < distance_height:
    print("Rectangle2 is inside Rectangle1.")
else:
   print("Rectangle2 overlaps Rectangle1")

def draw_rectangle(x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)

draw_rectangle(p1x, p1y, width_rec1, height_rec1)
draw_rectangle(p2x, p2y, width_rec1, height_rec2)

turtle.hideturtle()

turtle.done()


