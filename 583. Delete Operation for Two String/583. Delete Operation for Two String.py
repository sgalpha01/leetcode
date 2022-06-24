def min_dist(word1, word2):
    m, n = len(word1), len(word2)
    prev, curr = [0] * (n + 1), [0] * (n + 1)
    for i in range(m):
        for j in range(n):
            curr[j + 1] = max(curr[j], prev[j + 1], prev[j] + (word1[i] == word2[j]))
        prev, curr = curr, prev
    return m + n - 2 * prev[n]


print(min_dist("leetcode", "etco"))
