def inverse(dict):
    new_dict = {}
    for key, value in dict.items(): 
        if value not in new_dict: 
            new_dict[value] = [key]
        else:
            new_dict[value].append(key)
    return new_dict

dict = {'a':1, 'b':2, 'c':1, 'd':3, 'e':1, 'f':2}
print(inverse(dict))

