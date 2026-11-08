class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        # n = len(nums)
        # count = 0

        # for i in range(n):
        #     prod = 1

        #     for j in range(i, n):
        #         prod *= nums[j]

        #         if prod < k:
        #             count += 1
        #         else:
        #             break

        # return count

        if k <= 1:
            return 0

        left = 0
        prod = 1
        count = 0

        for right in range(len(nums)):
            prod *= nums[right]

            while prod >= k:
                prod //= nums[left]
                left += 1

            count += right - left + 1

        return count