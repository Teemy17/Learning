#Q1
import matplotlib.pyplot as plt

def list_to_string(input_list):
    string = ""
    for num in input_list:
        string = string + str(num)
    return string

def find_occurance(string):
    result = {}
    for number in string:
        if number.isdigit():
            result[number] = result.get(number,0) + 1
    return result

def autopct_format(l):   
    result = find_occurance(list_to_string(l))
    values = list(result.values())
    total = sum(values)
    def my_format(pct):
        absolute = int(pct/100.*total)
        return f"({absolute})"
    return my_format

def draw_pie_chart(l):
    result = find_occurance(list_to_string(l))
    num = list(result.keys())
    value = list(result.values())
    plt.pie(value, labels=num, autopct= autopct_format(l), startangle=180)
    plt.show() 

l = [3,1,3,3,2,3,3,2,3,2,4,3,3,3,3,4,3,4,3,3,3,4,3]
draw_pie_chart(l)

#---------------------------------------------------------------------------------------

#Q2
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

#---------------------------------------------------------------------------------------

#Q3
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

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

print(my_union(list1, list2))
print(my_intersection(list1, list2))
print(my_difference(list1, list2))

#---------------------------------------------------------------------------------------

#Q4
def print_table(list):
    for i in range(len(list)):
        for j in range(len(list[i])):
            print(list[i][j], end="\t")
        print()
    return


list1 = [["X", "Y"], [0, 0], [10, 10], [200, 200]]

list2 = [
    ["ID", "Name", "Surname"],
    ["001", "Guido", "van Rossum"],
    ["002", "Donald", "Knuth"],
    ["003", "Gordon", "Moore"],
]

print_table(list1)
print()
print_table(list2)

#---------------------------------------------------------------------------------------

#Q5
def isAnagram(String1, String2):
    if sorted(String1) == sorted(String2):
        return True
    else:
        return False

print(isAnagram("listen", "silent"))
print(isAnagram("triangle", "integral"))
print(isAnagram("cat", "dog"))
