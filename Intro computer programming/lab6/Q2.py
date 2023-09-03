import turtle as t
t.speed(0)
def square(x):
    for i in range(4):
        t.fd(x)
        t.rt(90)

def square_pattern(x):
    for j in range(4):
        square(x)
        for k in range(5):
            square(x * k)
        t.lt(90)
        
    
      
      

square_pattern(40)