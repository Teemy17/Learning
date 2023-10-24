first = input("Enter your first name: ")
last = input("Enter your last name: ")
gender = input("Enter your gender (m/f): ")

print(f"Your username: {gender.upper()}{last[0].upper()}{first[:6].upper()}")

