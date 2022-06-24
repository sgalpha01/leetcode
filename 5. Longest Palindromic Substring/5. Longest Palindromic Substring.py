def longestPalindrome(s: str) -> str:
    n = len(s)
    best_len = 0
    best_str = ""

    # When palindrome is of odd length
    for mid in range(n):
        x = 0
        while (mid - x >= 0) and (mid + x < n):
            length = 2 * x + 1
            if s[mid - x] != s[mid + x]:
                break
            if length > best_len:
                best_len = length
                best_str = s[mid - x : mid + x + 1]

            x += 1

    # When palindrome is of even length
    for mid in range(n - 1):
        x = 1
        while (mid - x + 1 >= 0) and (mid + x < n):
            length = 2 * x
            if s[mid - x + 1] != s[mid + x]:
                break
            if length > best_len:
                best_len = length
                best_str = s[mid - x + 1 : mid + x + 1]

            x += 1

    return best_str


def modify_str(s):
    mod = "#"
    for i in range(len(s)):
        mod += s[i] + "#"

    return mod


def demodify_str(s):
    demod = ""
    start = 1 if s[0] == "#" else 0
    for i in range(start, len(s), 2):
        demod += s[i]

    return demod


def manacher(s: str) -> str:
    # Insert #s to handle both odd and even cases
    # abba -> #a#b#b#a#
    mod_str = modify_str(s)
    l = 0
    r = -1
    lps = [0] * len(mod_str)
    max_expansion = 0
    best_expansion_idx = 0

    for i in range(len(mod_str)):
        # If current element is beyond the right boundary of
        # palindrome of max len, then current element becomes the center
        # This is the trivial case of naive solution
        if i > r:
            expansion = 0

        # If the palindrome formed with current center stays within the boundary
        # then lps[l + r - i] will be chosen
        # Otherwise r - 1, i.e., boundary
        else:
            expansion = min(lps[l + r - i], r - i)

        while (i - expansion > 0) and (i + expansion) < len(mod_str):
            if mod_str[i - expansion] != mod_str[i + expansion]:
                break

            expansion += 1

        # This case is require so that we don't go out of bound
        # or corner elements of current word are not same
        if (
            (i - expansion < 0)
            or (i + expansion >= len(mod_str))
            or mod_str[i - expansion] != mod_str[i + expansion]
        ):
            expansion -= 1

        lps[i] = expansion

        # Update the previous boundary
        if i + expansion > r:
            r = i + expansion
            l = i - expansion

        if expansion > max_expansion:
            max_expansion = expansion
            best_expansion_idx = i

    return demodify_str(
        mod_str[
            best_expansion_idx - max_expansion : best_expansion_idx + max_expansion + 1
        ]
    )


s = "abaaba"
print(manacher(s))
