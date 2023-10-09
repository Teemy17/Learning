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