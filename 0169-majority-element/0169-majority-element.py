class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        for i in range(n):
            if cnt == 0:
                El = nums[i]
                cnt += 1
            elif nums[i] == El:
                cnt += 1
            else:
                cnt -= 1
        return El        
        # cnt = 0
        # for i in range(n):
        #     if nums[i] == El:
        #         cnt += 1
        #     if cnt > n // 2:
        #         return El               
        