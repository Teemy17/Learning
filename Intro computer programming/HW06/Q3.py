def number_to_words(number):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if 0 < number < 10:
        return ones[number]
    elif 10 <= number < 20:
        return teens[number - 10]
    elif 20 <= number < 100:
        return (f"{tens[number // 10]} {ones[number % 10]}")
    elif 100 <= number < 1000:
        return (f"{ones[number // 100]} hundred and {number_to_words(number % 100)}")
    elif number == 0:
        return "zero"
    else:
        return "I don't know"


number = int(input("Enter a number: "))
print(number_to_words(number))

