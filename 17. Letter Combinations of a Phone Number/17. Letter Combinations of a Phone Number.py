# def letterCombinations(digits: str) -> list:
#     mapping = {
#         "2": "abc",
#         "3": "def",
#         "4": "ghi",
#         "5": "jkl",
#         "6": "mno",
#         "7": "pqrs",
#         "8": "tuv",
#         "9": "wxyz",
#     }
#     if not digits:
#         return []
#     arr = []
#     helper(digits, arr, 0, "", mapping)
#     return arr


# def helper(digits, arr, curr, combi, mapping):
#     if curr == len(digits):
#         arr.append(combi)
#         return

#     for c in mapping[digits[curr]]:
#         combi += c
#         helper(digits, arr, curr + 1, combi, mapping)
#         combi = combi[:-1]


def letterCombinations(digits):
    if not digits:
        return []

    mapping = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    ans = [""]
    for digit in digits:
        extend_combination = []
        for current_combination in ans:
            for new_char in mapping[digit]:
                extend_combination.append(current_combination + new_char)

        ans = extend_combination

    return ans


print(letterCombinations("23"))
