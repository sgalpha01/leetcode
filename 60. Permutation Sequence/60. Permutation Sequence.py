def get_permutation(n: int, k: int) -> str:
    nums = [i for i in range(1, n + 1)]
    kth_perm = ""
    k -= 1  # Indexing starts from 1 :)
    fact = 1
    for fact_num in range(1, n):
        fact *= fact_num

    for _ in range(n - 1):  # if n, fact_num will become 0
        idx = k // fact
        k -= idx * fact
        fact //= fact_num
        fact_num -= 1

        kth_perm += str(nums.pop(idx))

    return kth_perm + str(
        nums.pop()
    )  # loop is till (n - 1), so one element is left in nums
