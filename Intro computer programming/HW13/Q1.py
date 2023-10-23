def print_btree(tree, depth=0):
    if tree is None:
        return

    node, children = tree
    indent = " " * depth * 3

    print(indent + str(node))

    if children:
        for child in children:
            print_btree(child, depth + 1)


tree = [1, [
    [11, [
        [111, []],
        [112, []]
    ]],
    [12, [
        [121, []],
        [122, [
            [1221, []],
            [1222, []]
        ]]
    ]]
]]

print_btree(tree)
