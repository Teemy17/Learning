def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)
    
print(gcd(24, 16))
print(gcd(255, 25))
print(gcd(420, 0))
print(gcd(0, 69))