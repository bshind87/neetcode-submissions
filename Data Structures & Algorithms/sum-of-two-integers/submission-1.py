class Solution:
    def getSum(self, a: int, b: int) -> int:
        ret = []
        for i in range(abs(a)):
            if a >= 0:
                ret.append(1)
            else:
                ret.append(-1)
        print(ret)
        for j in range(abs(b)):
            if b >= 0:
                ret.append(1)
            else:
                ret.append(-1)
        return sum(ret)
        