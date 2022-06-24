def custom_sort_string(order, string):
    from collections import Counter

    order_set = set(order)
    counter = Counter(string)
    res = ""

    for char in order:
        if char in counter:
            res += char * counter[char]

    for char in string:
        if char not in order_set:
            res += char

    return res
