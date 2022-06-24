def valid_palindrome(s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            break
        l += 1
        r -= 1

    return is_palindrome(s, l + 1, r) or is_palindrome(s, l, r - 1)


def is_palindrome(s, l, r):
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


string = "abca"
print(valid_palindrome(string))
