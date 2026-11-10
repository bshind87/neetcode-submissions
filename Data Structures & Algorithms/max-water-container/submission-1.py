class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        res = 0

        while left < right:
            h = min(heights[left], heights[right])
            w = right - left 
            res = max(res, h * w)

            if heights[left] > heights[right]:
                right -= 1
            else: 
                left += 1
        return res