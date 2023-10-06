import turtle
from abc import ABC, abstractmethod

class TwoDShape(ABC):
    def __init__(self, obj):
        self.object = obj
    
    @abstractmethod
    def draw(self):
        pass

class Line(TwoDShape):
    def __init__(self, obj, distance):
        super().__init__(obj)
        self.distance = distance
    
    def draw(self):
        turtle.forward(self.distance)

class Rectangle(TwoDShape):
    def __init__(self, obj, width, height):
        super().__init__(obj)
        self.width = width
        self.height = height
    
    def draw(self):
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
        turtle.right(90)
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)

class Circle(TwoDShape):
    def __init__(self, obj, rad):
        super().__init__(obj)
        self.rad = rad
    
    def draw(self):
        turtle.circle(self.rad)

class Square(TwoDShape):
    def __init__(self, obj, side):
        super().__init__(obj)
        self.side = side
    
    def draw(self):
        for i in range(4):
            turtle.forward(self.side)
            turtle.right(90)

line = Line(turtle.Turtle(), 200)
rectangle = Rectangle(turtle.Turtle(), 100, 300)
circle = Circle(turtle.Turtle(), 50)
line2 = Line(turtle.Turtle(), 200)
rectangle2 = Rectangle(turtle.Turtle(), 200, 100)
circle2 = Circle(turtle.Turtle(), 200)
sq1 = Square(turtle.Turtle(), 100)
sq2 = Square(turtle.Turtle(), 200)

turtle.speed(0)

line.draw()
rectangle.draw()
circle.draw()
line2.draw()
rectangle2.draw()
circle2.draw()
sq1.draw()
sq2.draw()

turtle.done()