def composite(dict1, dict2):
    dict3 = {}
    for keydict1 in dict1:
        for keydict2 in dict2:
            if dict1[keydict1] == keydict2:
                dict3[keydict1] = dict2[keydict2]
    return dict3

dict1 = {'a' : 'p', 'b' : 'r', 'c' : 'q', 'd' : 'p', 'e' : 's'}
dict2 = {'p' : 1, 'q' : 2, 'r' : 3}

print(composite(dict1, dict2))