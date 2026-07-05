class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
       ## BRUTE FORCE
        # temp = []
        # n = len(nums)
        # for i in range(n):
        #     if nums[i] != 0:
        #         temp.append(nums[i])

        # for i in range(len(temp)):
        #     nums[i] = temp[i]

        # for i in range(len(temp),n):
        #     nums[i] = 0            
        # return nums

        # OPTIMAL

        j = -1
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                j = i
                break   
        if j == -1:
            return 
        for i in range(j+1,n):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
            
        return nums            