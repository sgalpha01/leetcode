def min_height_trees(n, edges):
    if n == 1:
        return [0]

    adj = [set() for _ in range(n)]

    for i, j in edges:
        adj[i].add(j)
        adj[j].add(i)

    leaves = [i for i in range(n) if len(adj[i]) == 1]

    print(adj)
    print(leaves)

    while n > 2:
        n -= len(leaves)
        new_leaves = []
        for leaf in leaves:
            new_leaf = adj[leaf].pop()
            adj[new_leaf].remove(leaf)
            if len(adj[new_leaf]) == 1:
                new_leaves.append(new_leaf)
        leaves = new_leaves

    return leaves


n, edges = 4, [[1, 0], [1, 2], [1, 3]]
print(min_height_trees(n, edges))
