from bisect import bisect_left


def russian_doll(envelopes):
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    lis = []

    for envelop in envelopes:
        idx = bisect_left(lis, envelop)
        if idx == len(lis):
            lis.append(envelop)
        else:
            lis[idx] = envelop

    return len(lis)


envelopes = [[1, 1], [1, 1], [1, 1]]
print(russian_doll(envelopes))
