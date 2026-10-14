class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxAr = 0
        l = 0
        r = len(height) - 1

        while l < r:
            h = min(height[l],height[r])
            width = r - l
            area = h * width

            maxAr = max(maxAr,area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxAr


        