from collections import Counter


def bulls_and_cows(secret, guess):
    counter_s = Counter(secret)
    counter_g = Counter(guess)
    bulls, cows = 0, 0
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            counter_s[secret[i]] -= 1
            counter_g[guess[i]] -= 1
            bulls += 1
    for k, v in counter_g.items():
        if v and k in counter_s:
            cows += min(v, counter_s[k])
    return f"{bulls}A{cows}B"
