import math

class Point:
    def __init__(self, x = 0.0, y = 0.0):
        self.x = x
        self.y = y
    
    def pirintInfo(self):
        return f"Position: {self.x}, {self.y}"
        

class Circle(Point):
    def __init__(self, x = 0.0, y = 0.0, r = 0.0):
        super().__init__(x, y)
        self.r = r
    
    def area(self):
        return math.pi * self.r * self.r
    
    def pirintInfo(self):
        print(f"{super().pirintInfo()}; Radius: {self.r}; Area: {self.area()}")
    
def main():
    x = float(input("Enter x: "))
    y = float(input("Enter y: "))
    r = float(input("Enter r: "))
    c = Circle(x, y, r)
    c.pirintInfo()

main()