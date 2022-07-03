from collections import Counter


def top_k(words, k):
    words.sort()
    return (a[0] for a in Counter(words).most_common(k))
