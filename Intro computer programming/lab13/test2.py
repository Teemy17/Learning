def find_subsets_with_sum_zero(lst):
    def find_subsets_recursive(subset, start):
        if sum(subset) == 0 and subset:
            subsets.append(tuple(subset))
        
        for i in range(start, len(lst)):
            subset.append(lst[i])
            find_subsets_recursive(subset, i + 1)
            subset.pop()

    subsets = []
    find_subsets_recursive([], 0)
    return subsets

# Example usage:
input_list = [2, -3, 5, 8, 11, 23, -1]
input_list2 = [-7, -3, -2, 5, 7]
zero_sum_subsets = find_subsets_with_sum_zero(input_list)
zero_sum_subsets2 = find_subsets_with_sum_zero(input_list2)

if not zero_sum_subsets:
    print("No")
else:
    for subset in zero_sum_subsets:
        print(subset, end=" ")

if not zero_sum_subsets2:
    print("No")
else:
    print("Yes")
    for subset in zero_sum_subsets2:
        print(subset, end=" ")
