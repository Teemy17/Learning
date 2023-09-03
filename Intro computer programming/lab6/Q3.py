import turtle as t
t.speed(0)
def draw_polygon(x, y, side = 4, size = 100):
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    for i in range(side):
          t.fd(size)
          t.rt(360 / side)
        
draw_polygon(0,0)
draw_polygon(10,10,5)
draw_polygon(10,10,5,200)