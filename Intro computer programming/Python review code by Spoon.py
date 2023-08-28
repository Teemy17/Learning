
#----------------------------------------------------------------------------------------------------------------------------------
print("Please enter a time in 24 hour format.")
hour = int(input("Hours: "))
minute = int(input("Minutes: "))
second = int(input("Seconds: "))

if hour < 12:
    period = "AM"
else:
    period = "PM"

if hour > 12:
    hour -= 12

print("The time you just entered in 12 hour format is " + str("{:02d}".format(hour)) + ":" + str("{:02d}".format(minute)) + ":" + str("{:02d}".format(second)) + " " + period)
#----------------------------------------------------------------------------------------------------------------------------------
import turtle
turtle.showturtle()
while True:
    cmd = input("Enter turtle command: ")
    if cmd == "fd":
        arg = int(input("Enter its argument: "))
        turtle.forward(arg)
    elif cmd == "back":
        arg = int(input("Enter its argument: "))
        turtle.backward(arg)
    elif cmd == "lt":
        arg = int(input("Enter its argument: "))
        turtle.left(arg)
    elif cmd == "rt":
        arg = int(input("Enter its argument: "))
        turtle.right(arg)
    elif cmd == "pu":
        turtle.penup()
    elif cmd == "pd":
        turtle.pendown()
    elif cmd == "reset":
        turtle.reset()
    elif cmd == "quit":
        exit(0)
        break
    else:
        print("Wrong command, try again.")
#----------------------------------------------------------------------------------------------------------------------------------
import turtle

def draw_square(n):
    for _ in range(4):
        turtle.forward(n)
        turtle.left(90)

def draw_nested_squares(s, g):
    if s < g:
        return
    
    draw_square(s)
    turtle.penup()
    turtle.forward(g)
    turtle.left(90)
    turtle.forward(g)
    turtle.right(90)
    turtle.pendown()
    draw_nested_squares(s - 2 * g, g)
    

# Set up the turtle
turtle.speed(0) # Fastest drawing speed
turtle.bgcolor("white")  # Set background color

# Call the nested squares function
turtle.penup()
turtle.goto(-100, 100)  # Position the turtle at the starting point
turtle.pendown()
draw_nested_squares(1000, 20)

# Close the turtle graphics window when clicked
turtle.exitonclick()
    
#----------------------------------------------------------------------------------------------------------------------------------
try:
    number = eval(input("Enter a number: "))
    if isinstance(number, float):
        type = (input("Type of number you want to display: Enter f: floating point, s: scientific format: "))
        if type == "f":
            print(float(number))
        elif type == "s":
            print(format(number, "10.2e"))
            
    elif isinstance(number, int):
        type1 = str(input("Display binary(b), octal(o), hexadecimal(h), decimal(d): "))
        if type1 == "b":
            print("Binary: ", bin(number))
        elif type1 == "o":
            print("Octal: ", oct(number))
        elif type1 == "h":
            print("Hexadecimal: ", hex(number))
        elif type1 == "d":
            print("Decimal", format(number, "5.1f"))
except:
    print("Plaese input real number or integer")
#----------------------------------------------------------------------------------------------------------------------------------
while True:
    try:
        ascii_value = ord(input("Please enter a character: "))
        if 0x30 <= ascii_value <= 0x39:
            print("It's a numeric character")
        elif 0x41 <= ascii_value <= 0x5A:
            print("It's a capital letter")
        elif 0x61 <= ascii_value <= 0x7A:
            print("It's a small case letter")
        elif ascii_value == 0x2E:
            break
        else:
            print("It's a special character")
    except:
        print("Please enter only one character")
        continue
    
import random
user = int(input("scissor(0), rock(1), paper(2): "))
game = ["scissor", "rock", "paper"]
computer = random.choice(game)

#----------------------------------------------------------------------------------------------------------------------------------
if computer == "scissor":
    if user == 0:
        print("The computer is scissor. You are scissor. It is a draw.")
    elif user == 1:
        print("The computer is scissor. You are rock. You won.")
    elif user == 2:
        print("The computer is scissor. You are paper. You lost.")
elif computer == "rock":
    if user == 0:
        print("The computer is rock. You are scissor. You lost.")
    elif user == 1:
        print("The computer is rock. You are rock. It is a draw.")
    elif user == 2:
        print("The computer is rock. You are paper. You won.")
elif computer == "paper":
    if user == 0:
        print("The computer is paper. You are scissor. You won.")
    elif user == 1:
        print("The computer is paper. You are rock. You lost.")
    elif user == 2:
        print("The computer is paper. You are paper. It is a draw.")

#----------------------------------------------------------------------------------------------------------------------------------
number = eval(input("Enter a number: "))

if isinstance(number, float):
    type = (input("Type of number you want to display: Enter f: floating point, s: scientific format: "))
    if type == "f":
        print(float(number))
    elif type == "s":
        print(format(number, "10.2e"))
        
elif isinstance(number, int):
    type1 = str(input("Display binary(b), octal(o), hexadecimal(h), decimal(d): "))
    if type1 == "b":
        print("Binary: ", bin(number))
    elif type1 == "o":
        print("Octal: ", oct(number))
    elif type1 == "h":
        print("Hexadecimal: ", hex(number))
    elif type1 == "d":
        print("Decimal", number, "5d")
else:
    print("Plaese input real number or integer")

#----------------------------------------------------------------------------------------------------------------------------------

A = int(input("Enter an integer"))

if A % 2 == 0:
    for x in range(1, (A - (A // 2)) + 1):
        num = 1
        row_values = []
        for y in range(x):
            row_values.append(num)
            num *= 2
        row_values.reverse()
        for value in row_values:
            print(value, end=" ")
        print()

    for x in range((A - (A // 2)), 0, -1):
        num = 1
        row_values = []
        for y in range(x):
            row_values.append(num)
            num *= 2
        row_values.reverse()
        for value in row_values:
            print(value, end=" ")
        print()

if A % 2 != 0:
    for x in range(1,(A - ((A+1) // 2)) + 1):
        num = 1
        row_values = []
        for y in range(x):
            row_values.append(num)
            num *= 2
        row_values.reverse()
        for value in row_values:
            print(value, end=" ")
        print()

    for x in range((A - ((A-1) // 2)), 0, -1):
        num = 1
        row_values = []
        for y in range(x):
            row_values.append(num)
            num *= 2
        row_values.reverse()
        for value in row_values:
            print(value, end=" ")
        print()

#----------------------------------------------------------------------------------------------------------------------------------

def sum_of_digits(n):
    new = []
    for x in str(n):
        new.append(int(x))
    result = sum(new)
    return result, new
print(sum_of_digits(234))

#----------------------------------------------------------------------------------------------------------------------------------
try:
    num = int(input("How much do you want to withdraw: "))
    if num % 100 == 0:
        if num // 1000 != 0:
            thousand = num//1000
            num %= 1000
        else:
            thousand = 0
        if num // 500 != 0:
            fivehun = num//500
            num %= 500
        else:
            fivehun = 0
        if num //100 != 0:
            hun = num//100
        print("You get " + str(thousand) + " notes of 1,000 Bahts")
        print("You get " + str(fivehun) + " notes of 500 Bahts")
        print("You get " + str(hun) + " notes of 100 Bahts")
    else:
        print("Number should be xxx.x00 only")
except:
    print("Please put an integer")

#----------------------------------------------------------------------------------------------------------------------------------

for num in range(49, 0, -1):
    if num % 3 != 0 and num % 5 != 0:
        if num == 1:
            print(num, end=".")
        else:
            print(num, end=", ")

#----------------------------------------------------------------------------------------------------------------------------------


