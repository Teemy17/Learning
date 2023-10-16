#Q1
import time

class Clock:
    def __init__(self, hh, mm, ss):
        self.hh = int(hh)
        self.mm = int(mm)
        self.ss = int(ss)

    def run(self):
        while True:
            self.ss += 1
            if self.ss == 60:
                self.ss = 0
                self.mm += 1
            if self.mm == 60:
                self.mm = 0
                self.hh += 1
            if self.hh == 24:
                self.hh = 0
            print(f"{self.hh:02d}:{self.mm:02d}:{self.ss:02d}")
            time.sleep(1)

    def setTime(self, h, m, s):
        self.hh = int(h)
        self.mm = int(m)
        self.ss = int(s)

class Alarmclock(Clock):
    def __init__(self, hh, mm, ss):
        super().__init__(hh, mm, ss)  # Call the constructor of the parent class
        self.alarm_hh = int(hh)
        self.alarm_mm = int(mm)
        self.alarm_ss = int(ss)
        self.alarm_on_off = False

    def setAlarmTime(self, h, m, s):
        self.alarm_hh = int(h)
        self.alarm_mm = int(m)
        self.alarm_ss = int(s)

    def alarmOn(self):
        self.alarm_on_off = True

    def alarmOff(self):
        self.alarm_on_off = False

    def run(self):
        while True:
            self.ss += 1
            if self.ss == 60:
                self.ss = 0
                self.mm += 1
            if self.mm == 60:
                self.mm = 0
                self.hh += 1
            if self.hh == 24:
                self.hh = 0
            print(f"{self.hh:02d}:{self.mm:02d}:{self.ss:02d}")
            if self.alarm_on_off:
                if self.hh == self.alarm_hh and self.mm == self.alarm_mm and self.ss == self.alarm_ss:
                    print("Alarm!")
                    break
            time.sleep(1)


alarm_clock = Alarmclock(12, 1, 50)

alarm_clock.setAlarmTime(12, 2, 5)
alarm_clock.alarmOn()
alarm_clock.run()
#------------------------------------------------------------------------------------------------------------------
#Q2
import turtle 
import math

def RobotBattle():
    #robotList stores the list of robots in the battle
    robotList = []

    while True:
        #Clear the screen and draw the robots
        turtle.clear()
        for robot in robotList:
            robot.draw()
        
        #Display the status of each robot
        print("==== Robots ====")
        i = 0
        for robot in robotList:
            print(i, " : ")
            robot.displayStatus()
            i += 1
        print("================")
            
        #Ask user which robot to command or to create a new robot
        choice = input("Enter which type of robot to order, 'c' to create new robot, 'q' to quit: ")
        if choice == "q":
            break
        elif choice == "c":
            print("Enter which type of robot to create")
            robotType = input("'r' for Robot, 'm' for Medicbot, 's' for StrikerBot: ")
            if robotType == "r":
                newRobot = Robot()
            elif robotType == "m":
                newRobot = MedicBot()
            elif robotType == "s":
                newRobot = StrikerBot()
            robotList = robotList + [newRobot]
        else:
            n = int(choice)
            robotList[n].command(robotList)

        #Delete all the robots with health <= 0 from the list
        i = 0
        for robot in robotList:
            if(robot.health <= 0):
                del robotList[i]
            i += 1

class Robot(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.health = 100
        self.energy = 100

    def move(self, x, y):
        if self.energy > 0:
            self.x = x
            self.y = y
            self.energy -= 10

    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.circle(30)
    
    def displayStatus(self):
        print("x:", self.x)
        print("y:", self.y)
        print("Health:", self.health)
        print("Energy:", self.energy)

    def command(self, robotList):
        print("Possible actions: move")
        newX = int(input("Enter new x-coordinate: "))
        newY = int(input("Enter new y-coordinate: "))
        self.move(newX, newY)

class MedicBot(Robot):
    def __init__(self):
        super().__init__()

    def heal(self, r):
        if self.energy >= 20 and math.sqrt((r.x - self.x)**2 + (r.y - self.y)**2) <= 10:
            r.health += 10
            self.energy -= 20
        elif self.energy < 20:
            print("Not enough energy!")
        elif math.sqrt((r.x - self.x)**2 + (r.y - self.y)**2) > 10:
            print("The targeted robot is too far away!")            

    def displayStatus(self):
        print("x:", self.x)
        print("y:", self.y)
        print("Health:", self.health)
        print("Energy:", self.energy)

    def command(self, robotList):
        print("Possible actions: move, heal")
        choice = str(input("Enter which action to perform: "))
        if choice == "heal":
            robot = int(input("Enter which robot to heal: "))
            self.heal(robotList[robot])
        elif choice == "move":
            newX = int(input("Enter new x-coordinate: "))
            newY = int(input("Enter new y-coordinate: "))
            self.move(newX, newY)
        else:
            print("Invalid action! Try again.")

    def draw(self):
        super().draw()
        turtle.lt(90)
        turtle.fd(30)
        turtle.rt(90)
        turtle.fd(30)
        turtle.lt(180)
        turtle.fd(60)
        turtle.rt(180)
        turtle.fd(30)
        turtle.lt(90)
        turtle.fd(30)

class StrikerBot(Robot):
    def __init__(self):
        super().__init__()
        self.missile = 5

    def strike(self, r):
        if self.energy >= 20 and math.sqrt((r.x - self.x)**2 + (r.y - self.y)**2) <= 10 and self.missile > 0:
            r.health -= 50
            self.energy -= 20
            self.missile -= 1
        elif self.energy < 20:
            print("Not enough energy!")
        elif math.sqrt((r.x - self.x)**2 + (r.y - self.y)**2) > 10:
            print("The targeted robot is too far away!")
        elif self.missile <= 0:
            print("No more missiles!")           

    def displayStatus(self):
        print("x:", self.x)
        print("y:", self.y)
        print("Health:", self.health)
        print("Energy:", self.energy)

    def command(self, robotList):
        print("Possible actions: move, strike")
        choice = str(input("Enter which action to perform: "))
        if choice == "strike":
            robot = int(input("Enter which robot to strike: "))
            self.strike(robotList[robot])
        elif choice == "move":
            newX = int(input("Enter new x-coordinate: "))
            newY = int(input("Enter new y-coordinate: "))
            self.move(newX, newY)
        else:
            print("Invalid action! Try again.")

    def draw(self):
        super().draw()
        turtle.pu()
        turtle.lt(90)
        turtle.fd(2)
        turtle.pd()
        turtle.rt(90)
        turtle.circle(30, 360, 4)
        

RobotBattle()

#------------------------------------------------------------------------------------------------------------------
#Q3
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        self.x_coord = x
        self.y_coord = y

    def draw(self):
        plt.plot(self.x_coord, self.y_coord, 'ro', markersize=6)

    def get_position(self):
        return f"{self.x_coord}, {self.y_coord}"

class Rectangle2D(Point):
    def __init__(self, max_x, max_y, min_x, min_y):
        super().__init__((max_x + min_x) / 2, (max_y + min_y) / 2)
        self.max_x = max_x
        self.max_y = max_y
        self.min_x = min_x
        self.min_y = min_y

    def draw(self):
        plt.plot([self.min_x, self.max_x, self.max_x, self.min_x, self.min_x], 
                 [self.max_y, self.max_y, self.min_y, self.min_y, self.max_y], 'b-')

    def get_width(self):
        return self.max_x - self.min_x

    def get_height(self):
        return self.max_y - self.min_y

def get_rectangle(points):
    x_coords = [float(points[i]) for i in range(0, len(points), 2)]
    y_coords = [float(points[i]) for i in range(1, len(points), 2)]

    points_list = [Point(x_coords[i], y_coords[i]) for i in range(min(len(x_coords), len(y_coords)))]

    for point in points_list:
        point.draw()
        point.get_position()

    bounding_rectangle = Rectangle2D(max(x_coords), max(y_coords), min(x_coords), min(y_coords))
    bounding_rectangle.draw()
    
    print(f"The bounding rectangle is centered at ({bounding_rectangle.get_position()}) with width {bounding_rectangle.get_width()} and height {bounding_rectangle.get_height()}")

def main():
    user_input = input("Enter the points: ").split()
    get_rectangle(user_input)
    plt.show()

main()

#------------------------------------------------------------------------------------------------------------------
#Q4
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
    numDict = {"0": Char0(size), "1": Char1(size), "2": Char2(size), "3": Char3(size), "4": Char4(size), "5": Char5(size), 
               "6": Char6(size), "7": Char7(size), "8": Char8(size), "9": Char9(size)}
    for num in x:
        for key in numDict:
            if (key == num):
                numDict[key].draw(posX, posY)
                posX += size * 1.5


drawNum("0123456789")
t.hideturtle()
t.done()

#------------------------------------------------------------------------------------------------------------------
#Q5
from abc import ABC, abstractmethod

class Goods(ABC):
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def get_price(self):
        pass

class Stationary(Goods):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    def get_price(self):
        return self.price * self.quantity
    
class Books(Goods):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    def get_price(self):
        return self.price * self.quantity * 0.9
    
class Magazine(Goods):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    def get_price(self):
        return self.price * self.quantity
    
class Ribbon(Goods):
    def __init__(self, length, color):
        super().__init__(length, 5, color)

    def get_price(self):
        return self.price * self.quantity 
    
class Basket:
    def __init__(self):
        self.goods = []

    def add(self, good):
        self.goods.append(good)

    def get_total_price(self):
        total_price = 0
        for good in self.goods:
            total_price += good.get_price()
        return f"The total price is {total_price:.2f} baht"

    def print_receipt(self):
        print("Items in the basket:")
        for good in self.goods:
            print(f"{good.name} - {good.get_price()} baht")

cart = Basket()
cart.add(Stationary("Pen", 10, 2))
cart.add(Books("Windows 7 for Beginners Book", 50, 2))
cart.add(Magazine("Computer World Magazine", 70, 3))
cart.add(Ribbon("Blue ribbons", 10))
cart.print_receipt()
print(cart.get_total_price())