class Solution:
    def myPow(self, x: float, n: int) -> float:
        ret = 1
        for i in range(abs(n)):
            if n >= 0:
                ret = ret * x
            else:
                ret = ret * (1/x)
            print(ret)
        return ret
        