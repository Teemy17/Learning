class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height
    
    def GetPerimeter(self):
        return 2*(self.width) + 2*(self.height)
    
    def Move(self, newX, newY):
        self.x = newX
        self.y = newY

    def draw(self):
        for i in range(4):
            