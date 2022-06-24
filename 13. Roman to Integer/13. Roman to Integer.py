def romanToInt(s: str) -> int:
    mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    num = 0

    for i in range(len(s) - 1):
        if mapping[s[i]] < mapping[s[i + 1]]:
            num -= mapping[s[i]]
        else:
            num += mapping[s[i]]

    num += mapping[s[-1]]

    return num


print(romanToInt("IX"))
