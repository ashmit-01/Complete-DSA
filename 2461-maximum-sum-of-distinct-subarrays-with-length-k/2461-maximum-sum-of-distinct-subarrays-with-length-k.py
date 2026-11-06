
class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:

        n = len(nums)
        left = 0
        current_sum = 0
        max_sum = 0
        freq = {}

        for right in range(n):

            current_sum += nums[right]
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            if right - left + 1 > k:

                outgoing = nums[left]
                current_sum -= outgoing

                freq[outgoing] -= 1

                if freq[outgoing] == 0:
                    del freq[outgoing]

                left += 1

            if right - left + 1 == k and len(freq) == k:
                max_sum = max(max_sum, current_sum)

        return max_sum
