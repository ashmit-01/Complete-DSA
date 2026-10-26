class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        n = len(nums)

        while left < n :
            if nums[left] == target:
                return left
            elif nums[left] > target:
                return left
            elif target < nums[0]:
                return "0"
            elif target > nums[n-1]:
                return n
            left += 1             
            

        