from turtle import *

left(90)
tracer(0)

def tree(n, l):
    if n == 0:
        return
    forward(l)
    left(45)
    tree(n-1, l*0.6)
    right(90)
    tree(n-1, l*0.6)
    left(45)
    backward(l)

tree(10, 100)
update()
mainloop()
