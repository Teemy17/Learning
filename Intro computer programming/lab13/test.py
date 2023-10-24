def subset(lst, num):
    result = []
    def find(lst, num, path=()):
        if not lst:
            return
        if lst[0] == num:
            result.append(path + (lst[0],))
        else:
            find(lst[1:], num - lst[0], path + (lst[0],))
            find(lst[1:], num, path)
    find(lst, num)
    return result

numbers = [-7, -3, -2, 5, 7]
x = 0
print(subset(numbers,x))

numbers = [2, -3, 5, 8, 11, 23, -1]
x = 0
print(subset(numbers,x))


