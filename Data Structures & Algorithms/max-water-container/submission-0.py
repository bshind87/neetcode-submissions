class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_c = 0

        while left < right:
            l = right - left
            h = min(heights[right], heights[left])
            capacity = l * h
            max_c = max(max_c, capacity)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return max_c 