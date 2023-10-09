import math

class Calculator:
    def __init__(self, acc = 0.0):
        self.acc = acc

    def set_accumalator(self, a):
        self.acc = a

    def get_accumalator(self):
        return self.acc

    def add(self, x):
        self.acc += x

    def subtract(self, x):
        self.acc -= x

    def multiply(self, x):
        self.acc *= x

    def divide(self, x):    
        if x == 0:
            print("Error: Division by zero")
        else:
            self.acc /= x

    def print_result(self):
        print(f"Result: {self.acc}")

class Sci_calc(Calculator):
    def __init__(self, acc = 0.0):
        super().__init__(acc)
    
    def square(self):
        self.acc *= self.acc

    def exponent(self, x):
        self.acc **= x

    def factorial(self):
        self.acc = math.factorial(self.acc)

    def print_result(self):
        print(f"Result: {self.acc:.1e}")


c = Calculator()
c.set_accumalator(10)
c.get_accumalator()
c.add(5)
c.multiply(2)
c.subtract(1)
c.divide(0)
c.print_result()

sc = Sci_calc()
sc.set_accumalator(10)
sc.get_accumalator()
sc.square()
sc.exponent(3)
sc.print_result()
sc.set_accumalator(5)
sc.factorial()
sc.print_result()

