def character_frequency(string):
    frequency_dict = {}

    for char in string:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1

    print("-- Character Frequency Table -")
    print("char\tpercentage")
    
    for char, frequency in frequency_dict.items():
        percentage = (frequency / len(string)) * 100
        print(f"{char}\t{percentage:.2f}%")

string = input("Enter some text: ")
character_frequency(string)

