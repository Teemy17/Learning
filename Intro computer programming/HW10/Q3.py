def my_union(list1, list2):
    result = []
    for i in list1:
        if i not in result:
            result.append(i)
    for j in list2:
        if j not in result:
            result.append(j)
    return result

def my_intersection(list1, list2):
    result = []
    for i in list1:
        if i in list2:
            result.append(i)
    return result

def my_difference(list1, list2):
    result = []
    for i in list1:
        if i not in list2:
            result.append(i)
    return result

list1 = [3, 1, 2, 7]
list2 = [4, 1, 2, 5]

print(my_union(list1, list2))
print(my_intersection(list1, list2))
print(my_difference(list1, list2))