nodes = [3, 2, 1]
a = -1

for i in range(len(nodes) - 1):
    if nodes[i] > nodes[i + 1]:
        if a == -1:
            a = i
        b = i + 1

print(a, b)
