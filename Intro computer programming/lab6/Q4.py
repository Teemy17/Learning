def sum_of_digits(n):
    total = 0
    for num in n:
        total += int(num)
    return total
    
i = (input("Enter number: "))
print(f"sum is: {sum_of_digits(i)}")