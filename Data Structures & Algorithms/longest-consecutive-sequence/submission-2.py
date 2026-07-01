class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        checks = [0]
        for n in nums:
            small = n
            large = n
            while True:
                change = False
                if large + 1 in nums:
                    large = large + 1
                    change = True
                if small - 1 in nums:
                    small = small - 1
                    change = True
                if not change:
                    break
                change = False
            checks.append(large - small + 1)
        
        return max(checks)
                

        