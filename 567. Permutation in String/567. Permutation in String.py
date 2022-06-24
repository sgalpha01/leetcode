from collections import Counter


def check_perm(s1, s2):
    s1_counter = Counter(s1)
    s2_counter = Counter(s2[: len(s1) - 1])
    s2_counter[s2[-1]] += 1
    for i in range(len(s1) - 1, len(s2)):
        s2_counter[s2[i - len(s1)]] -= 1
        if s2_counter[s2[i - len(s1)]] == 0:
            del s2_counter[s2[i - len(s1)]]
        s2_counter[s2[i]] += 1
        if s1_counter == s2_counter:
            return True

    return False


s1 = "ab"
s2 = "eidbaooo"
print(check_perm(s1, s2))
