def find_word_positions(word, list_of_words):
    # Convert the word and list of words to lowercase for case-insensitive comparison
    word = word.lower()
    list_of_words_lower = [w.lower() for w in list_of_words]

    # Initialize a list to store positions where the word occurs
    positions = []

    for index, w in enumerate(list_of_words):
        if word == list_of_words_lower[index]:
            positions.append(index)

    if len(positions) > 0:
        return positions
    else:
        return 0

# Example usage:
word_to_find = "iOS"
words_list = ["Programming", "is", "important", "for", "science", "engineering", "Is", "ios"]

# result = find_word_positions(word_to_find, words_list)
# if result == 0:
#     print("0")
# else:
#     print(result)
#-----------------------------------------------------------------------------------------------------------------

popularity_scores = {"c++": 99.7, "c": 96.7, "Java": 97.5, 
                    "Python": 100, "C#": 89.4}

def get_rankings(scores):
    return dict(sorted(scores.items(), key=lambda element: element[1],
                reverse=True))

# print(get_rankings(popularity_scores))
#-----------------------------------------------------------------------------------------------------------------

def find_word_positions(word, list_of_words):
    pos = []
    for index, element in enumerate(list_of_words):
        if element.lower() == word.lower():
            pos.append(index)
    if pos:
        return pos
    else:
        return 0

# print(find_word_positions("Python",["python","java", "c","PYTHON","Prolog"]))
# print(find_word_positions("iOS",["Windows","macOS","Linux"]))

#-----------------------------------------------------------------------------------------------------------------
def find_numbers_occurence(lst):
    d = {}
    for i in lst:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

# print(find_numbers_occurence([1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6]))
#-----------------------------------------------------------------------------------------------------------------

class SavingsAccount:
    def __init__(self, bank_name, acc_name, acc_id, balance, transaction_history):
        self.bank_name = bank_name
        self.acc_name = acc_name
        self.acc_id = acc_id
        self.balance = balance
        self.transaction_history = transaction_history

    def deposit(self, money, person, date):
        self_balace += money
        self.transaction_history.append(f"Money deposit: {money}, Person: {person}, date: {date}")

    def withdrawn(self, money, person, date):
        if self.balance - money < 0:
            print("Not enough money to withdrawn")
        else:
            self.balance -= money
            self.transaction_history.append(f"Money withdrwan: {money}, Person: {person}, date: {date}")

    def get_balance(self):
        return self.balance
    
    def print_statement(self):
        return self.transaction_history
    
class OverdrawnAccount(SavingsAccount):
    def __init__(self, bank_name, acc_name, acc_id, balance, transaction_history, overdrawn_limit):
        super.__init__(self, bank_name, acc_name, acc_id, balance, transaction_history)
        self.overdrawn_limit = overdrawn_limit

    def withdrawn(self, money, person, date):
        if self.balance - self.money < self.overdrawn_limit:
            print("The money exceeds the withdrown limit!")
        else:
            self.balance -= money
            self.transaction_history.append(f"Money withdrwan: {money}, Person: {person}, date: {date}")

#-----------------------------------------------------------------------------------------------------------------

def count_operands_in_expr(expr):
    operands = ["+", "-", "*", "/", "%", "**", "//"]
    expr = str(expr)
    if not expr:
        return 0
    else:
        operand = count_operands_in_expr(expr[1:])
        if expr[0] in operands:
            return operand + 1
        else:
            return operand

# print(count_operands_in_expr((3,'**',4)))
# print(count_operands_in_expr(((((2, '+', 4), '/', 3), '*', 2), '+', (3, '**', 4))))

#-----------------------------------------------------------------------------------------------------------------

def find_member_positions(number, list_of_numbers):
    pos = []
    for index, element in enumerate(list_of_numbers):
        if element == number:
            pos.append(index)
    if pos:
        return pos
    else:
        return 0

# print(find_member_positions(2,[2,5,3,2,4]))  
# print(find_member_positions(1,[2,5,3,2,4]))  

#-----------------------------------------------------------------------------------------------------------------

class Ewallet:
    def __init__(self, owner, max_money):
        self.owner = owner
        self.max_money = max_money
        self.balance = 0

    def deposit(self, amount):
        if self.balance + amount <= self.max_money :
            self.balance += amount
            print(f"Deposit: {amount}, balance: {self.balance}")
        else:
            print("The money exceeds the limit")

    def withdrawn(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            print(f"withdrawn: {amount}, balance: {self.balance}")
        else:
            print("Not enough money to withdrawn")

    def get_balance(self):
        return self.balance
    
class SmartEwallet(Ewallet):
    def __init__(self, owner, max_money, history): #history is a list
        super().__init__(owner, max_money)
        self.history = history
    
    def set_max_money(self, max):
        self.max_money = float(max)

    def deposit(self, amount):
        if self.balance + amount <= self.max_money :
            self.balance += amount
            self.history.append(f"Owner: {self.owner}, Deposit: {amount}, balance: {self.balance}")
        else:
            print("The money exceeds the limit")

    def withdrawn(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            self.history.append(f"Owner: {self.owner}, withdrawn: {amount}, balance: {self.balance}")
        else:
            print("Not enough money to withdrawn")

    def get_balance(self):
        return self.balance

    def display_history(self):
        return self.history
    
# test = SmartEwallet("Teem", 100, [])
# test.set_max_money(500)
# test.deposit(200)
# print(test.get_balance())
# test.deposit(200)
# print(test.get_balance())
# print(test.display_history())

#-----------------------------------------------------------------------------------------------------------------

from abc import ABC, abstractmethod

class Sale_item(ABC):   
    @abstractmethod
    def get_cost(self):
        return self.cost

class Food(ABC):  
    @abstractmethod
    def get_cost(self):
        return self.cost

class Book(Sale_item):
    def __init__(self, name, cost, quantity = 1):
        self.name = name
        self.cost = ((cost * 75) / 100) * quantity
        self.quantity = quantity
    
    def get_cost(self):
        pass

class Appliance(Sale_item):
    def __init__(self, name, cost, quantity = 1):
        self.name= name
        self.cost = ((cost * 107) / 100) * quantity
        self.quantity = quantity

    def get_cost(self):
        pass

class Itemized_food(Food):
    def __init__(self, name, cost, quantity = 1):
        self.name = name
        self.cost = cost * quantity
        self.quantity = quantity

    def get_cost(self):
        pass

class Measured_food(Food):
    def __init__(self, name, cost, weight = 1):
        self.name = name
        self.cost = cost * weight
        self.quantity = weight

    def get_cost(self):
        pass

purchased_item = [Itemized_food("vegetable oil", 40, 2), Measured_food("mango", 70, 1.8), Book("Python", 200, 1), Appliance("rice cooker", 1200, 1)]

def calculate():
    food = 0; book = 0; appliance = 0
    for item in purchased_item:
        if (type(item) == Itemized_food or type(item) == 
            Measured_food):
            food += Food.get_cost(item)
        elif type(item) == Book:
            book += Sale_item.get_cost(item)
        elif type(item) == Appliance:
            appliance += Sale_item.get_cost(item)
    
    print(f"Total cost: {(food + book + appliance):.2f} Bahts")

calculate()