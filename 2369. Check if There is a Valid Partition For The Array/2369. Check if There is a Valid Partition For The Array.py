from typing import List


class Solution:
    def validPartition_memo(self, nums: List[int]) -> bool:
        def dfs(i):
            if i <= 0:
                return False
            if i == 1:
                return self.is_valid((nums[i - 1], nums[i]))
            if i == 2:
                return self.is_valid((nums[i - 2], nums[i - 1], nums[i]))

            two = self.is_valid((nums[i - 1], nums[i])) and dfs(i - 2)
            three = self.is_valid((nums[i - 2], nums[i - 1], nums[i])) and dfs(i - 3)

            return two or three

        return dfs(len(nums) - 1)

    def is_valid(self, arr):
        if len(arr) == 2 and arr[0] == arr[1]:
            return True
        if len(arr) == 3 and (
            arr[0] == arr[1] == arr[2] or arr[2] - arr[1] == arr[1] - arr[0] == 1
        ):
            return True
        return False

    def validPartition(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return self.is_valid(nums)
        n = len(nums)
        two = [False] * n
        three = [False] * n
        two[1] = self.is_valid((nums[0], nums[1]))
        three[2] = self.is_valid((nums[0], nums[1], nums[2]))
        for i in range(3, n):
            two[i] = self.is_valid((nums[i - 1], nums[i])) and (
                two[i - 2] or three[i - 2]
            )
            three[i] = self.is_valid((nums[i - 2], nums[i - 1], nums[i])) and (
                two[i - 3] or three[i - 3]
            )
        return two[-1] or three[-1]


obj = Solution()
nums = [1, 1, 1, 2]
print(obj.validPartition(nums))
