class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Variable to store current count of consecutive 1's
        cnt = 0
        # Variable to store maximum consecutive 1's
        maxi = 0

        # Traverse the array
        for i in range(len(nums)):
            # If current element is 1, increment count
            if nums[i] == 1:
                cnt += 1
            else:
                # If element is 0, reset count
                cnt = 0

            # Update maximum if current count is greater
            maxi = max(maxi, cnt)

        # Return maximum consecutive 1's
        return maxi
        