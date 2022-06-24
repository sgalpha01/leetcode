def get_smallest_string(n, k):
    mapping = {i - 96: chr(i) for i in range(97, 97 + 26)}
    res = ""
    for i in range(n - 1, -1, -1):
        for j in range(1, 27):
            if i * 26 + j >= k:
                break
        res += mapping[j]
        k -= j

    return res


print(get_smallest_string(3, 10))
