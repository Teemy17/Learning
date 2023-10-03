def character_frequency(string):
    characters = []
    frequencies = []

    for char in string:
        found = False
        for i in range(len(characters)):
            if characters[i] == char:
                frequencies[i] += 1
                found = True
                break
        if not found:
            characters.append(char)
            frequencies.append(1)

    print("-- Character Frequency Table -")
    print("char\tpercentage")

    total_characters = len(string)
    for i in range(len(characters)):
        char = characters[i]
        frequency = frequencies[i]
        percentage = (frequency / total_characters) * 100
        print(f"{char}\t{percentage:.2f}%")

string = input("Enter some text: ")
character_frequency(string)
