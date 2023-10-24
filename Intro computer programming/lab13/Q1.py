def list_member(num, lst):
    if not lst:
        return False
    elif num == lst[0]:
        return True
    else:
        return list_member(num, lst[1:])
    
print(list_member(2, [1, 2, 3]))
print(list_member(4, [1, 2, 3]))
print(list_member(1, [2, 3, 44, 5]))