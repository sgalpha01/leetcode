def word_pattern(pattern, s):
    forward, backward = {}, set()
    s = s.split()
    if len(pattern) != len(s):
        return False

    for i in range(len(pattern)):
        if pattern[i] not in forward:
            if s[i] in backward:
                return False

            forward[pattern[i]] = s[i]
            backward.add(s[i])

        elif forward[pattern[i]] != s[i]:
            return False

    return True


pattern = "abc"
s = "dog cat dog"
print(word_pattern(pattern, s))
