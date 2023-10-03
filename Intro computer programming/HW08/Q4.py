digits = input("Enter the first 9 digits of an ISBN-10 as a string: ")
sum = 0
for i in range(0, len(digits)):
    sum += int(digits[i]) * (i + 1)

chk = sum % 11

if chk == 10:
    digits += "X"
    print(f"Your ISBN-10 number is: {digits}")
else:
    digits += str(chk)
    print(f"Your ISBN-10 number is: {digits}")