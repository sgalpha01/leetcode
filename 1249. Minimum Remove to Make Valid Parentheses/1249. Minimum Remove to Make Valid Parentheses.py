def make_valid(s):
    ls = []
    num_open = 0
    for char in s:
        if char == ")":
            if num_open <= 0:
                continue
            num_open -= 1
        elif char == "(":
            num_open += 1
        ls.append(char)

    s = "".join(ls[::-1])
    ls.clear()
    num_open = 0
    for char in s:
        if char == "(":
            if num_open <= 0:
                continue
            num_open -= 1
        elif char == ")":
            num_open += 1
        ls.append(char)

    return "".join(ls[::-1])


string = "lee(t(c)o)de)"
print(make_valid(string))
