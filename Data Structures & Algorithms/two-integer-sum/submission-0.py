class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c = {}
        for i, num in enumerate(nums):
            req = target - num
            if req in c:
                return [c[req], i]
            c[num] = i
        