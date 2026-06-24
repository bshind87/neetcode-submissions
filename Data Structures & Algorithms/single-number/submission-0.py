class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ret = []
        for n in nums:
            if n in ret:
                ret.remove(n)
            else:
                ret.append(n)
        return ret[0]
        