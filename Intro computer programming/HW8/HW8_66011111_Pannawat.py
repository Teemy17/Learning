#Q1
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

#Q2
def character_frequency(string):
    frequency_dict = {}

    for char in string:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1

    print("-- Character Frequency Table -")
    print("char\tpercentage")
    
    for char, frequency in frequency_dict.items():
        percentage = (frequency / len(string)) * 100
        print(f"{char}\t{percentage:.2f}%")

string = input("Enter some text: ")
character_frequency(string)

#Q3
import turtle

def bar_character(string):
    frequency_dict = {}

    for char in string:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1

    screen = turtle.Screen()
    screen.bgcolor("white")

    turtle.penup()
    turtle.speed(0)

    max_frequency = max(frequency_dict.values())

    x = -300
    y = -150
    
    for char, frequency in frequency_dict.items():
        percentage = (frequency / len(string)) * 100
        bar_height = (frequency / max_frequency) * 200
        
        turtle.goto(-350,-150)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(bar_height)
        turtle.right(90)
        turtle.penup()
        turtle.goto(-350,-150)
        turtle.pendown()
        
        turtle.goto(x, y)
        turtle.pendown()
        turtle.forward(30)
        turtle.left(90)
        turtle.forward(bar_height)
        turtle.left(90)
        turtle.forward(30)
        turtle.left(90)
        turtle.forward(bar_height)
        turtle.left(90)
        turtle.penup()

        turtle.goto(x + 15, y - 30)
        turtle.write(char, align="center", font=("Times New Roman", 15, "bold"))

        x += 75

    screen.exitonclick()

string = input("Enter a string: ")
bar_character(string)

#Q4
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



    