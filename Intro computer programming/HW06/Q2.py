import turtle as t

wn = t.Screen()
wn.tracer(0)
screen = t.Screen()
screen.screensize(2000 ,10000)
t.setup()
t.speed(0)

arr_day = ["Mo","Tu","We","Th","Fr","Sa","Su"]
arr_month =["January", 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

def month(month_no, start_day, no_days, a = 6, b = 7 ):
    
    #title
    for i in range(2):
        t.fd(280)
        t.right(90)
        t.fd(20)
        t.right(90)

    t.right(90)
    t.fd(20)
    t.left(90)
    t.write(f"\t\t    {arr_month[month_no-1]} 2023")
    
    
    for cols in range(len(arr_day)):
        for i in range(2):
            t.fd(40)
            t.right(90)
            t.fd(20)
            t.right(90)

        #table
        t.penup()
        t.right(45)
        t.fd(25)
        t.left(45)
        t.pendown()
        t.write(arr_day[cols])
        t.penup()
        t.right(45)
        t.fd(-25)
        t.left(45)
        t.pendown()
        t.fd(40)
        
    t.fd(-280)
    t.penup()
    t.right(90)
    t.fd(20)
    t.left(90)
    t.pendown()

   
    c = 0
    day = 0
    for i in range(a):
        for cols in range(b):
            for j in range(2):
                t.fd(40)
                t.right(90)
                t.fd(20)
                t.right(90)
            c += 1
            
            if c >= start_day and c <= no_days:
                day += 1

                t.penup()
                t.right(45)
                t.fd(25)
                t.left(45)
                t.pendown()
                t.write(day)
                t.penup()
                t.right(45)
                t.fd(-25)
                t.left(45)
                t.pendown()
                
            t.fd(40)
            
        t.fd(-280)
        t.penup()
        t.right(90)
        t.fd(20)
        t.left(90)
        t.pendown()

def draw_month():
    t.penup()
    t.goto(0, 0)
    t.pendown()
    

def calendar_of_2023(month_no):
    if (month_no == 1):
        draw_month()
        month(1,7,37)

    elif (month_no == 2):
        draw_month()
        month(2,3,30)
    
    elif (month_no == 3):
        draw_month()
        month(3,3,33)

    elif (month_no == 4):
        draw_month()
        month(4,6,35)

    elif (month_no == 5):
        draw_month()
        month(5,1,31)
 
    elif (month_no == 6):
        draw_month()
        month(6,4,33)

    elif (month_no == 7):
        draw_month()
        month(7,6,36)

    elif (month_no == 8):
        draw_month()
        month(8,2,32)

    elif (month_no == 9):
        draw_month()
        month(9,5,34)

    elif (month_no == 10):
        draw_month()
        month(10,7,37)


    elif (month_no == 11):
        draw_month()
        month(11,3,32)

    elif (month_no == 12):
        draw_month()
        month(12,5,35)


    
def main():
    #Enter the number of desired month in the function calendar_of_2023    
    calendar_of_2023(1)
    t.exitonclick()

main()