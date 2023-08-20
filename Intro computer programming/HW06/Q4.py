def countCurrency(amount):
    money_types = [1000, 500, 100, 50, 20, 10, 5, 2, 1]
    Count = {}
     
    for i in money_types:
        if amount >= i:
            Count[i] = amount // i
            amount = amount % i
             
    for type, value in Count.items():
        if type > 10:
            print(f"{type}-Baht notes: {value}")
        else:
            print(f"{type}-Baht coins: {value}")


amount = int(input("Input your amount of money: "))
countCurrency(amount)


