long = input("Enter long string: ")
short = input("Enter short string: ")

is_substring = False

if len(long) < len(short):
    print("Please enter the correct length")
    exit(1)


for i in range(len(long) - len(short) + 1):
    if long[i:i + len(short)] == short:
        is_substring = True
        break

if is_substring:
    print("short substring is a substring of a long string")
else:
    print("short string is not a substring of a long string")
