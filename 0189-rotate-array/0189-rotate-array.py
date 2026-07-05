class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
       
        # Function to rverse
        def reverseArr(nums,start,end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start +=1
                end -=1
       #  Base case
        n = len(nums)
        if k==0 and n==0:
            return 0

        k = k % n 

        # Right rotate
        reverseArr(nums,0,n-1)
        reverseArr(nums,0,k-1)
        reverseArr(nums,k,n-1)

        return nums


        