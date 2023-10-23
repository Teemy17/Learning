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
