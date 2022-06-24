# Delete elements
def removeDuplicates1(nums) -> int:
    i, n = 1, len(nums)
    while i < n:
        if nums[i - 1] == nums[i]:
            del nums[i]
            n -= 1
        else:
            i += 1

    return n


# overwrite element
def removeDuplicates2(nums) -> int:
    duplis = 0
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            duplis += 1
        else:
            nums[i - duplis] = nums[i]

    return len(nums) - duplis


arr1 = [1, 1, 2, 2, 2, 3, 4, 5, 5, 6, 7, 8, 8]
arr2 = arr1.copy()

removeDuplicates1(arr1)
removeDuplicates2(arr2)

print(arr1)
print(arr2)
