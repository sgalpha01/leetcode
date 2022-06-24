def count_and_say(n: int) -> str:
    res = "1"
    for _ in range(1, n):
        i, j = 0, 1
        curr = ""
        while i < len(res):
            while j < len(res) and res[j] == res[i]:
                j += 1

            curr += f"{j - i}{res[i]}"
            i = j
        res = curr

    return res


for i in range(1, 11):
    print(count_and_say(i))
