class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        d = Counter(nums)
        n = 0
        for i in range(len(nums)):
            if i not in d:
                return i
            else:
                n = i

        return n+1