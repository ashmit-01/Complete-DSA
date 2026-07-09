class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        lsc = [-1] * n
        rsc = [n] * n
        stack = []

        # Previous Smaller
        for i in range(n):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()

            if stack:
                lsc[i] = stack[-1]

            stack.append(i)

        stack.clear()

        # Next Smaller
        for i in range(n - 1, -1, -1):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()

            if stack:
                rsc[i] = stack[-1]

            stack.append(i)

        maxi = 0

        for i in range(n):
            width = rsc[i] - lsc[i] - 1
            area = heights[i] * width
            maxi = max(maxi, area)

        return maxi