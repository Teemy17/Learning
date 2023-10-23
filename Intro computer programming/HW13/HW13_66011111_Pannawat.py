#Q1
def print_btree(tree, depth=0):
    if tree is None:
        return

    node, children = tree
    indent = " " * depth * 3

    print(indent + str(node))

    if children:
        for child in children:
            print_btree(child, depth + 1)


tree = [1, [
    [11, [
        [111, []],
        [112, []]
    ]],
    [12, [
        [121, []],
        [122, [
            [1221, []],
            [1222, []]
        ]]
    ]]
]]

print_btree(tree)
#----------------------------------------------------------
#Q2
def f(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return 2 * f(n // 2) + 1
    else:
        return 0

def display_f(n):
    for i in range(n + 1):
        result = f(i)
        print(f"f({i}) = {result}")


n = int(input("Enter a non-negative integer n: "))
display_f(n)
#----------------------------------------------------------
#Q3
def perm2(t):
    def generate_pairs(t, current_pair, result):
        if len(current_pair) == 2:
            result.append(current_pair)
            return
        for i in range(len(t)):
            new_pair = current_pair + (t[i],)
            remaining = t[:i] + t[i + 1:]
            generate_pairs(remaining, new_pair, result)

    pairs = []
    generate_pairs(t, (), pairs)

    for pair in pairs:
        print(pair, end=" ")

def perm3(t):
    def generate_pairs(t, current_pair, result):
        if len(current_pair) == 3:
            result.append(current_pair)
            return
        for i in range(len(t)):
            new_pair = current_pair + (t[i],)
            remaining = t[:i] + t[i + 1:]
            generate_pairs(remaining, new_pair, result)

    pairs = []
    generate_pairs(t, (), pairs)

    for pair in pairs:
        print(pair, end=" ")

def perm(t, n):
    def generate_pairs(t, current_pair, result):
        if len(current_pair) == n:
            result.append(current_pair)
            return
        for i in range(len(t)):
            new_pair = current_pair + (t[i],)
            remaining = t[:i] + t[i + 1:]
            generate_pairs(remaining, new_pair, result)

    pairs = []
    generate_pairs(t, (), pairs)

    for pair in pairs:
        print(pair, end=" ")


def main():
    t = (1 ,2 ,3)
    print("perm2:")
    perm2(t)
    print()
    t = (1, 2, 3, 4)
    print("perm3:")
    perm3(t)
    print()
    print("perm:")
    perm((1, 2 ,3), 3)

main()
#----------------------------------------------------------
#Q4
def tower_of_hanoi(n, start, end, aux):
    if n == 1:
        print(f"Move disk 1 from tower {start} to tower {end}")
    else:
        tower_of_hanoi(n-1, start, aux, end)
        print(f"Move disk {n} from tower {start} to tower {end}")
        tower_of_hanoi(n-1, aux, end, start)

tower_of_hanoi(3, 'A', 'C', 'B')
#----------------------------------------------------------
#Q5
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


