class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        low = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[low] = nums[low], nums[i]
                low += 1
            
        