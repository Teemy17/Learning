def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list)-1-i):
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
    return list

list = [5,4,3,2,1]
print(bubble_sort(list))

list2 = [3, 2, 9, 7, 8]
print(bubble_sort(list2))