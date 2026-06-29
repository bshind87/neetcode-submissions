class Solution:
    def isHappy(self, n: int) -> bool:
        vis = []
        cn = n
        while True:
            res = 0
            while cn > 0:
                d = cn % 10
                cn = int(cn / 10)
                res += (d * d)
            if res == 1:
                return True
            elif res in vis:
                return False
            else:
                vis.append(res)
                cn = res
        