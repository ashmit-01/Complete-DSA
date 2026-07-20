class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxim = float('-inf')

        sum = 0

        for i in range(len(nums)):
            sum += nums[i]
            
            if sum > maxim:
                maxim = sum

            if sum < 0:
                sum = 0
        return maxim        
