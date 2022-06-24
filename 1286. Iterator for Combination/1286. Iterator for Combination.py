from itertools import combinations, tee

string = "abc"

combs = combinations(string, 2)

print(next(combs))
print(next(combs))
print(next(combs))
combs, combs_copy = tee(combs)
print(next(combs_copy))
