class BankAccount:
    def __init__(self, bank_name = "KKK", bank_owner = "lmao", account_number = 69420, balance = 0.0):
        self.bank_name = bank_name
        self.bank_owner = bank_owner
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, n):
        if n < 0:
            print("You can't deposit negative my bro")
        else: 
            self.balance += n
            print(f"deposit: {n}")
    
    def withdrawn(self, n):
        if self.balance >= n:
            self.balance -= n
            print(f"Withdrawn: {n}")
        else:
            print("You're poor bruh")
        
    def remaining_balance(self):
        print(f"Remaining balance: {self.balance}")

s = BankAccount()
s.deposit(100)
s.withdrawn(50)
s.remaining_balance()
s.deposit(200)
s.remaining_balance()




