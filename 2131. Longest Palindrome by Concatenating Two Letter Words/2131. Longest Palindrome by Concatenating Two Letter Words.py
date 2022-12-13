from collections import Counter


def longest_palindrome(words):
    count = Counter(words)
    curr_len = 0
    is_middle_done = False
    for word, freq in count.items():
        if word[0] == word[1]:
            if freq & 1:
                freq -= 1
                curr_len += freq * 2 + 2 * (not is_middle_done)
                is_middle_done = True
            else:
                curr_len += freq * 2

        elif word[::-1] in count:
            curr_len += min(freq, count[word[::-1]]) * 2
    return curr_len


words = ["cc", "ll", "xx"]
print(longest_palindrome(words))
