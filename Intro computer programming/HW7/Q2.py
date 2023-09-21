class Poly:
    def __init__(self, x):
        self.x = list(x)

    
    def add(self, poly):
        for i in range(len(self.x)):
            self.x[i] += poly[i]
        return self.x

    
    def scalar_multiply(self, c):
        for i in range(len(self.x)):
            self.x[i] *= c
        return self.x

    def print_poly(self):
        for i in range(len(self.x)):
            if self.x[i] >= 0:
                sign = "+"
            else:
                sign = "-"
        if i == 0:
                sign = ""
                print(f"{sign}{self.x[i]} ", end = "")
            
        else: 
            if self.x[i] != 0: 
                if i == 1: 
                    print(f"{sign} {self.x[i]}x ", end = "")
                elif self.x[i] == 1:
                    print(f"{sign} x^{i} ", end = "")
                else:
                    print(f"{sign} {self.x[i]}x^{i} ", end = "")
            else:
                print("")


    


        