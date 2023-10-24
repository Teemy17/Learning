def find_duplicates(dict):
    new_dict = {}
    seen_values = {}

    for key, value in dict.items():
        if value in seen_values:
            if value not in new_dict:
                new_dict[value] = [seen_values[value]]
            new_dict[value].append(key)
        else:
            seen_values[value] = key
    
    result = {}

    for value, keys in new_dict.items():
        for key in  keys:
            result[key] = value

    return result



myDict = {
    "s5301" : "Fred", "s5302" : "Harry", "s5303" : "John", "s5304" : "Fred", "s5305" : "Harry",
}
print(find_duplicates(myDict))