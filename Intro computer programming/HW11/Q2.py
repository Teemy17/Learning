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