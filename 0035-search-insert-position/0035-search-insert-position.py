class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        n = len(nums)

        while left < n:
            if nums[left] >= target:
                return left
            left += 1

        return n