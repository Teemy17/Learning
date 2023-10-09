from abc import ABC, abstractmethod
import turtle as t
t.speed(0)

class Char(ABC):
    @abstractmethod
    def __init__(self, width):
        self.width = width

    @abstractmethod
    def draw(self, x, y):
        pass

    @abstractmethod
    def getWidth(self):
        return self.width
    
class Char0(Char):
    def __init__(self, width):
        super().__init__(width)

    def draw(self, x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.forward(self.width)
        t.right(90)
        t.forward(2*self.width)
        t.right(90)
        t.forward(self.width)
        t.right(90)
        t.forward(2*self.width)
        t.setheading(0)
        

    def getWidth(self):
        return super().getWidth()
    
class Char1(Char):
    def __init__(self, width):
        super().__init__(width)

    def draw(self, x, y):
        t.pu()
        t.goto(x, y)
        t.pd()
        t.rt(90)
        t.fd(self.width*2)
        t.setheading(0)

    def getWidth(self):
        return super().getWidth()
    
class Char2(Char):
    def __init__(self, width):
        super().__init__(width)

    def draw(self, x, y):
        t.pu()
        t.goto(x, y)
        t.pd()
        t.fd(self.width)
        t.rt(90)
        t.fd(self.width)
        t.rt(90)
        t.fd(self.width)
        t.lt(90)
        t.fd(self.width)
        t.lt(90)
        t.fd(self.width)

    def getWidth(self):
        return super().getWidth()
    
class Char3(Char):
    def __init__(self, width):
        super().__init__(width)

    def draw(self, x, y):
        t.pu()
        t.goto(x, y)
        t.pd()
        for i in range(2):
            t.fd(self.width)
            t.rt(90)
        t.fd(self.width)
        for i in range(2):
            t.bk(self.width)
            t.rt(90)
        t.bk(self.width)


    def getWidth(self):
        return super().getWidth()
    
class Char4(Char):
    def __init__(self, width):
        super().__init__(width)

    def draw(self, x, y):
        t.pu()
        t.goto(x, y)
        t.pd()
        t.rt(90)
        t.fd(self.width)
        t.lt(90)
        t.fd(self.width)
        t.lt(90)
        t.fd(self.width)
        t.bk(self.width*2)
        t.setheading(0)

    def getWidth(self):
        return super().getWidth()
    
class Char5(Char):
    def __init__(self, width):
        super().__init__(width)

    def draw(self, x, y):
        t.pu()
        t.goto(x, y)
        t.pd()
        t.fd(self.width)
        t.bk(self.width)
        t.rt(90)
        t.fd(self.width)
        t.lt(90)
        t.fd(self.width)
        t.rt(90)
        t.fd(self.width)
        t.rt(90)
        t.fd(self.width)
        t.setheading(0)
        
    def getWidth(self):
        return super().getWidth()
    
class Char6(Char):
    def __init__(self, width):
        super().__init__(width)

    def draw(self, x, y):
        t.pu()
        t.goto(x, y)
        t.pd()
        t.fd(self.width)
        t.bk(self.width)
        t.rt(90)
        t.fd(self.width*2)
        t.lt(90)
        t.fd(self.width)
        t.lt(90)
        t.fd(self.width)
        t.lt(90)
        t.fd(self.width)
        t.setheading(0)
        
    def getWidth(self):
        return super().getWidth()
    
class Char7(Char):
    def __init__(self, width):
        super().__init__(width)

    def draw(self, x, y):
        t.pu()
        t.goto(x, y)
        t.pd()
        t.fd(self.width)
        t.rt(90)
        t.fd(self.width*2)
        t.setheading(0)

    def getWidth(self):
        return super().getWidth()
    
class Char8(Char):
    def __init__(self, width):
        super().__init__(width)

    def draw(self, x, y):
        t.pu()
        t.goto(x, y)
        t.pd()
        for i in range(2):
            t.fd(self.width)
            t.rt(90)
        t.fd(self.width)
        t.rt(90)
        t.fd(self.width)
        t.rt(90)
        t.fd(self.width)
        t.rt(90)
        t.fd(self.width*2)
        t.rt(90)
        t.fd(self.width)
        t.rt(90)
        t.fd(self.width)
        t.setheading(0)
        

    def getWidth(self):
        return super().getWidth()

class Char9(Char):
    def __init__(self, width):
        super().__init__(width)

    def draw(self, x, y):
        t.pu()
        t.goto(x, y)
        t.pd()
        for i in range(2):
            t.fd(self.width)
            t.rt(90)
        t.fd(self.width)
        t.rt(90)
        t.fd(self.width)
        t.rt(90)
        t.fd(self.width)
        t.rt(90)
        t.fd(self.width*2)
        t.rt(90)
        t.fd(self.width)
        t.setheading(0)
        
    def getWidth(self):
        return super().getWidth()

def drawNum(x):
    x = str(x)
    size = 50
    posX, posY = 0 - (30 * len(x)), 0
    numDict = {"0": Char0(size), "1": Char1(size), "2": Char2(size), "3": Char3(size), "4": Char4(size), "5": Char5(size), "6": Char6(size), "7": Char7(size), "8": Char8(size), "9": Char9(size)}
    for number in x:
        for key in numDict:
            if (key == number):
                numDict[key].draw(posX, posY)
                posX += size * 1.5


drawNum("0123456789")
t.hideturtle()
t.done()