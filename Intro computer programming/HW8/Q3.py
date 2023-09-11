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
    turtle.hideturtle()
    screen.exitonclick()

string = input("Enter a string: ")
bar_character(string)

