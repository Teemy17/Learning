import turtle as t
t.speed(0)

def draw(x, y):
    if y == 0:
        t.dot(3)
        return

    t.forward(x)
    draw(x / 2, y - 1)
    t.backward(x * 2)
    draw(x / 2, y - 1)
    t.forward(x)

    t.left(90)

    t.forward(x)
    draw(x / 2, y - 1)
    t.backward(x * 2)
    draw(x / 2, y - 1)
    t.forward(x)

    t.right(90)

def main():
    draw(100, 4)
    t.mainloop()

main()