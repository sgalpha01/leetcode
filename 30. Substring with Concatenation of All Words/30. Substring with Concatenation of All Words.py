def findSubstring(s: str, words: list) -> list:
    from collections import Counter, defaultdict

    word_bag = Counter(words)
    word_len = len(words[0])
    num_words = len(words)
    total_len = word_len * num_words
    res = []

    for i in range(len(s) - total_len + 1):
        # For each i, determine if s[i:i+totalLen] is valid
        match = True
        seen = defaultdict(int)
        for j in range(i, i + total_len, word_len):
            curr_word = s[j : j + word_len]
            if curr_word in word_bag:
                seen[curr_word] += 1
                if seen[curr_word] > word_bag[curr_word]:
                    # s[i:i+totalLen] has matching word, but
                    # word_bag can't be exhausted this way
                    match = False
                    break
            else:
                # s[i:i+totalLen] has some word which is not in word_bag
                match = False
                break

        if match:
            res.append(i)

    return res


s = "barfoothefoobarman"
words = ["foo", "bar"]
print(findSubstring(s, words))
