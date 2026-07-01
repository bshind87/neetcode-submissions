class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = [0]
        for i in range(len(heights)):
            print(i, "  ", heights[i])
            left, right = i, i
            while True:
                changed = False
                if left - 1 >= 0:
                    if heights[left - 1] >= heights[i]:
                        left = left - 1
                        changed = True
                if right + 1 <= len(heights) - 1:
                    if heights[right + 1] >= heights[i]:
                        right = right + 1
                        changed = True
                if not changed:
                    break
                changed = False
            s.append((right - left + 1) * heights[i])
        return max(s)
        