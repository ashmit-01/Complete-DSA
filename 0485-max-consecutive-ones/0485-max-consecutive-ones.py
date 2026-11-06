class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        result = 0
        current = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                current += 1    
            else:
                current = 0
            result = max(current,result)        
        return result