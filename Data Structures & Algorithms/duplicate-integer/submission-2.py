class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False
        d = Counter(nums)
        if max(list(d.values())) > 1:
            return True
        else:
            return False
        