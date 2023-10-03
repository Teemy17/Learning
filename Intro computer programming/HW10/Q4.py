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
