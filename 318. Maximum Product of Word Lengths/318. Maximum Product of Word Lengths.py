def max_product(words):
    count = [set(word) for word in words]
    max_prod = 0
    for i in range(len(words) - 1):
        for j in range(i, len(words)):
            if not count[i] & count[j]:
                max_prod = max(max_prod, len(words[i]) * len(words[j]))

    return max_prod


words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
print(max_product(words))
