def count_vowel_strings(n):
    res = 0
    chars = {"a", "e", "i", "o", "u"}

    def count(n, last_char):
        nonlocal res
        if n == 0:
            return 1

        for char in chars:
            if char >= last_char:
                res += count(n - 1, char)

        return 0

    count(n, " ")
    return res


print(count_vowel_strings(2))
