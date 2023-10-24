words = "book,dog,drink,rain,pen"
for _ in range(len(words)):
    if words[_] == ",":
        print("")
    else:
        print(words[_], end = "")