class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        zero_count = 0
        for n in nums:
            if n != 0:
                p = n * p
            else:
                zero_count += 1
        ret = []
        for n in nums:
            if n != 0 and zero_count == 0:
                ret.append(int(p/n))
            elif n != 0 and zero_count >= 1:
                ret.append(0)
            elif n == 0 and zero_count == 1:
                ret.append(p)
            elif n ==0 and zero_count > 1:
                ret.append(0)
        return ret


        