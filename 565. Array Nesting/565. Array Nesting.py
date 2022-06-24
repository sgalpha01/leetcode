def array_nesting(nums):
    visited_arr = [0 for _ in range(len(nums))]
    max_count = 0

    for i in range(len(nums)):
        if not visited_arr[i]:
            start = i
            count = 1
            visited_arr[i] = 1
            curr_pos = i

            while nums[curr_pos] != start:
                curr_pos = nums[curr_pos]
                visited_arr[curr_pos] = 1
                count += 1

            max_count = max(max_count, count)

    return max_count


print(array_nesting([5, 4, 0, 3, 1, 6, 2]))
