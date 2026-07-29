class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # count = 0
        # for i in range(len(nums)):
        #     for j in range(i,len(nums)):
        #         sum = 0
        #         for m in range(i,j+1):
        #             sum = sum + nums[m]
        #         if sum == k:
        #             count += 1
        # return count         # O(n^3)     
        
        # Better

        # count = 0
        # for i in range(len(nums)):
        #     sum = 0
        #     for j in range(i,len(nums)):
        #         sum += nums[j]
        #         if sum == k:
        #             count += 1            
        
        # return count    # O(n^2)

        # Optimal
        n = len(nums)

        # Dictionary to store frequency of prefix sums
        prefixSumCount = {}

        # Initialize prefix sum and count of subarrays
        prefixSum = 0
        count = 0

        # Base case: prefix sum 0 has occurred once
        prefixSumCount[0] = 1

        # Traverse through the array
        for i in range(n):
            # Add current element to prefix sum
            prefixSum += nums[i]

            # Calculate the prefix sum that needs to be removed
            remove = prefixSum - k

            # If this prefix sum has been seen before,
            # add its count to the result
            if remove in prefixSumCount:
                count += prefixSumCount[remove]

            # Update the frequency of the current prefix sum
            prefixSumCount[prefixSum] = prefixSumCount.get(prefixSum, 0) + 1

        # Return the total count of subarrays
        return count