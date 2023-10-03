integer = int(input("Please enter an integer: "))
string = ""

if integer == 0:
    print("Integer is 0")
elif integer < 0:
    print("The integer is negative")
else:
    while integer > 0:
        string = str(integer % 2) + string
        integer = int(integer / 2)
    print("The binary is:", string)

    length = len(string) - 1
    sum = 0
    for i in range(0, len(string)):
        sum += (2 ** length) * int(string[i])
        length -= 1
    print("The converted integer is:", sum)


    