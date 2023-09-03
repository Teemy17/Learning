import math
import turtle as t
class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
    
    def getArea(self):
        return math.pi * self.radius**2

    def getPerimater(self):
        return 2 * math.pi * self.radius

    def move(self, newX, newY):
        self.x = newX
        self.y = newY
    
    def draw(self):
        t.penup()
        t.goto(self.x, self.y)
        t.rt(90)
        t.fd(self.radius)
        t.setheading(0)
        t.pendown()
        t.circle(self.radius)

c = Circle(0, 0, 50)
print(c.getArea())
print(c.getPerimater())
c.move(100,100)
c.draw()

d = Circle(0,0,50)
print(c.getArea())
print(c.getPerimater())
d.draw()







