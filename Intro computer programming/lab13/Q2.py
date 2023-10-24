def list_reverse(lst):
    if not lst:
        return []
    else:
        return list_reverse(lst[1:]) + [lst[0]]
    
print(list_reverse([1, 2, 3]))
print(list_reverse([1, 2, 3, 4, 5]))