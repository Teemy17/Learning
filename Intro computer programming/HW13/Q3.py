def perm2(t):
    def generate_pairs(t, current_pair, result):
        if len(current_pair) == 2:
            result.append(current_pair)
            return
        for i in range(len(t)):
            new_pair = current_pair + (t[i],)
            remaining = t[:i] + t[i + 1:]
            generate_pairs(remaining, new_pair, result)

    pairs = []
    generate_pairs(t, (), pairs)

    for pair in pairs:
        print(pair, end=" ")

def perm3(t):
    def generate_pairs(t, current_pair, result):
        if len(current_pair) == 3:
            result.append(current_pair)
            return
        for i in range(len(t)):
            new_pair = current_pair + (t[i],)
            remaining = t[:i] + t[i + 1:]
            generate_pairs(remaining, new_pair, result)

    pairs = []
    generate_pairs(t, (), pairs)

    for pair in pairs:
        print(pair, end=" ")

def perm(t, n):
    def generate_pairs(t, current_pair, result):
        if len(current_pair) == n:
            result.append(current_pair)
            return
        for i in range(len(t)):
            new_pair = current_pair + (t[i],)
            remaining = t[:i] + t[i + 1:]
            generate_pairs(remaining, new_pair, result)

    pairs = []
    generate_pairs(t, (), pairs)

    for pair in pairs:
        print(pair, end=" ")


def main():
    t = (1 ,2 ,3)
    print("perm2:")
    perm2(t)
    print()
    t = (1, 2, 3, 4)
    print("perm3:")
    perm3(t)
    print()
    print("perm:")
    perm((1, 2 ,3), 3)

main()