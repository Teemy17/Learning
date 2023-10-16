def cartesian_product(*sets):
    if len(sets) == 1:
        return sets[0]
    else:
        return set([(x, y) for x in sets[0] for y in cartesian_product(*sets[1:])])
    
s1 = set([1, 2, 3])
s2 = set(['p', 'q'])
s3 = set(['a', 'b', 'c'])

print("s1, s2: ")
print(cartesian_product(s1, s2))
print("s1, s2, s3: ")
print(cartesian_product(s1, s2, s3))
print("s1: ")
print(cartesian_product(s1))
