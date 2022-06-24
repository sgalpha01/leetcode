from functools import cache


def partition(s):
    res = []

    def backtrack(start, curr):
        if start == len(s):
            res.append(curr.copy())

        for i in range(start, len(s)):
            curr_str = s[start : i + 1]
            if curr_str == curr_str[::-1]:
                curr.append(curr_str)
                backtrack(i + 1, curr)
                curr.pop()

    backtrack(0, [])
    return res


s = "aabaabaaababababbbbbbbbbaaa"
print(partition(s))
