print("Please enter a time in 24 hour format")
hours = int(input("Hours: "))
minutes = int(input("Minutes: "))
seconds = int(input("Seconds: "))

if hours > 12:
	hours -= 12
	print(f"The time you just entered in 12 hour format is {hours:02d}:{minutes:02d}:{seconds:02d} PM.")
elif hours == 12:
	print(f"The time you just entered in 12 hour format is {hours:02d}:{minutes:02d}:{seconds:02d} PM.")
else:
	print(f"The time you just entered in 12 hour format is {hours:02d}:{minutes:02d}:{seconds:02d} AM.")
	
#----------------------------------------------------------------------------------------------------------------
	
import turtle as t
print("Hello, welcome to turtle world!")
t.pendown()
while True:
	cmd = input("turtle|>")
	if cmd == "fd":
		arg = int(input("Please enter its argument: "))
		t.forward(arg)
	elif cmd == "back":
		arg = int(input("Please enter its argument: "))
		t.backward(arg)
	elif cmd == "lt":
		arg = int(input("Please enter its argument: "))
		t.left(arg)
	elif cmd == "rt":
		arg = int(input("Please enter its argument: "))
		t.right(arg)
	elif cmd == "pu":
		t.penup()
	elif cmd == "pd":
		t.pendown()
	elif cmd == "reset":
		t.reset()
	elif cmd == "quit":
		exit(0)
	else:
		print("Wrong command, please try again.")
		
#-----------------------------------------------------------------------------------------------------------

n = 3
for i in range(0, n):
    for j in range(0, i + 1):
        print("*", end = " ")
    print("")

for i in range(n, 0 , -1):
    for j in range(0, i - 1):
        print("*", end = " ")
    print(" ")

# Output
# * 
# * * 
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
#----------------------------------------------------------------------------------------------------------------

n = 0
while n < 1:
    n = int(input("Input: "))
    chk = n
for i in range(n):
    for j in range(n): 
        for k in range(j + 1):
            print("*", end = "")
        print()
    for j in range(n):
        for k in range((n - j) - 1):
            if (n - j) - 1 != 1:
                print("*", end = "")
        if j < n - 2:
            print()
    n -= 1
if chk != 1:
    print("*")

# Output when n = 5
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
# **
# ***

#----------------------------------------------------------------------------------------------------------------







		
	
	
