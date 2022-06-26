def max_score(cards, k):
    res = curr_score = sum(cards[:k])
    for i in range(k):
        curr_score += cards[-i - 1] - cards[k - i - 1]
        res = max(res, curr_score)

    return res


cardPoints = [1, 2, 3, 4, 5, 6, 1]
k = 3
print(max_score(cardPoints, k))
