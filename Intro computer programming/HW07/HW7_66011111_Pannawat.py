#Q1
import time


class Clock:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def set_time(self, hr, min, sec):
        self.hour = hr
        self.minute = min
        self.second = sec

    def display_time(self):
        if self.hour > 12:
            return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d} PM"
        elif self.hour >= 12:
            return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d} PM"
        else:
            return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d} AM"

    def get_time(self):
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"

    def tick(self):
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
        if self.minute == 60:
            self.minute = 0
            self.hour += 1
        if self.hour == 24:
            self.hour = 0


c = Clock(13, 49, 55)
while True:
    print(c.display_time())
    c.tick()
    time.sleep(1)

#Q3
class LinearEquation:
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f
    
    def get_a(self):
        return f"a = {self.__a}"

    def get_b(self):
        return f"b = {self.__b}"

    def get_c(self):
        return f"c = {self.__c}"
    
    def get_d(self):
        return f"d = {self.__d}"

    def get_e(self):
        return f"e = {self.__e}"

    def get_f(self):
        return f"f = {self.__f}"
    
    def is_solvable(self):
        if (self.__a * self.__d) - (self.__b * self.__c) != 0 :
            return True
        else:
            return False

    def getX(self):
        if self.is_solvable() == True:
            x = ((self.__c * self.__d) - (self.__b * self.__f)) / ((self.__a * self.__d) - (self.__b * self.__c))
            return f"The value of X is: {x:.3f}"
        else:
            return "Not Solvable"

    def getY(self):
        if self.is_solvable() == True:
            y = ((self.__a * self.__f) - (self.__e * self.__c)) / ((self.__a * self.__d) - (self.__b * self.__c)) 
            return f"The value of Y is: {y:.3f}"
        else:
            return "Not Solvable"

e = LinearEquation(3, 6, 21, 12, 4, 8)
print(e.get_a())
print(e.get_b())
print(e.get_c())
print(e.get_d())
print(e.get_e())
print(e.get_f())
print(e.is_solvable())
print(e.getX())
print(e.getY())
