def generate(numRows):
    pascal = [[1]]
    for _ in range(1, numRows):
        curr = [1]
        for i in range(len(pascal[-1]) - 1):
            curr.append(pascal[-1][i] + pascal[-1][i + 1])
        curr.append(1)
        pascal.append(curr)
    return pascal


print(generate(4))
