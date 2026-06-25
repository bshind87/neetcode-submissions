class Solution:
    def trap(self, height: List[int]) -> int:
        left = []
        right = []

        cmax = 0
        for h in height:
            cmax = max(cmax, h)
            left.append(cmax)
        cmax = 0
        for i in height[::-1]:
            cmax = max(cmax, i)
            right.insert(0, cmax)
        #print(left)
        #print(right)
        max_water = 0
        for i in range(len(height)):
            max_water += min(left[i], right[i]) - height[i]
        return max_water



        