class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        left = 0
        max_len = 0
        zeroes = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeroes += 1
            while zeroes > 1:
                if nums[left] == 0:
                    zeroes -= 1
                left += 1
            max_len = max(max_len, right - left )
        return max_len


        