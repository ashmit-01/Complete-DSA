class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = -1

        # Decreasing Point 
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                index = i
                break
        
        # If no such index

        if index == -1:
            nums.reverse()
            return      

        # Find just greater element

        for i in range(len(nums)-1,index,-1):
            if nums[i] > nums[index]:
                # Swap them
                nums[i], nums[index] = nums[index], nums[i]
                break
        
        # Reverse part after index
        nums[index + 1:] = reversed(nums[index + 1:])           