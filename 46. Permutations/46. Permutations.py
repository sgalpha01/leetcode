from time import perf_counter


def permute_backtrack(nums):
    arr = []
    helper_backtrack(arr, nums, 0)
    return arr


def helper_backtrack(arr, nums, depth):
    if depth == len(nums):
        arr.append((nums.copy()))  # be careful to append the copy

    for i in range(depth, len(nums)):
        nums[i], nums[depth] = nums[depth], nums[i]
        helper_backtrack(arr, nums, depth + 1)
        nums[i], nums[depth] = nums[depth], nums[i]


def permute_heap(nums):
    arr = []
    helper_heap(arr, nums, len(nums))
    return arr


def helper_heap(arr, nums, size):
    if size == 1:
        arr.append(nums.copy())

    for i in range(size):
        helper_heap(arr, nums, size - 1)
        if size % 2 != 0:
            nums[0], nums[size - 1] = nums[size - 1], nums[0]
        else:
            nums[i], nums[size - 1] = nums[size - 1], nums[i]


def permute_iter(nums):
    perms = [[]]
    for n in nums:
        new_perms = []
        for perm in perms:
            for i in range(len(perm) + 1):
                new_perms.append(perm[:i] + [n] + perm[i:])
        perms = new_perms
    return perms


for i in range(9, 11):
    tic = perf_counter()
    permute_backtrack(list(range(i)))
    toc = perf_counter()
    print(f"backtracking took {(toc - tic):.4f}s for length {i}")

    tic = perf_counter()
    permute_heap(list(range(i)))
    toc = perf_counter()
    print(f"heap algo took {(toc - tic):.4f}s for length {i}")

    tic = perf_counter()
    permute_iter(list(range(i)))
    toc = perf_counter()
    print(f"iterative algo took {(toc - tic):.4f}s for length {i}")
