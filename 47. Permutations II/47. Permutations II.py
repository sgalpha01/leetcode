def permute_unique_iter(nums):
    perms = [[]]
    for n in nums:
        new_perms = []
        for perm in perms:
            print("\n")
            for i in range(len(perm) + 1):
                new_perms.append(perm[:i] + [n] + perm[i:])
                print(f"inserting {n} at pos {i} in permutation {perm}")
                print(f"resulting permutation: {new_perms[-1]}")
                if i < len(perm) and perm[i] == n:
                    print(
                        f"duplicate ({n}) found at pos {i}! breaking the innermost for loop."
                    )
                    break
        perms = new_perms

    print(f"\nfinal list of permutations:\n{perms}")
    return perms


def permute_unique_bt(nums):
    from collections import Counter

    counter = Counter(nums)
    perm = [None] * len(nums)
    perms = []

    def helper(depth):
        if depth == len(perm):
            perms.append(perm.copy())
            return

        for num in counter:
            if counter[num] == 0:
                continue
            perm[depth] = num
            counter[num] -= 1
            helper(depth + 1)
            counter[num] += 1

    helper(0)
    return perms


permute_unique_iter([1, 2, 3, 1])
