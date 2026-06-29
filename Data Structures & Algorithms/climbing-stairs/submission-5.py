import numpy as np
class Solution:
    def climbStairs(self, n: int) -> int:
        d = {}
        def dfs(i):
            if i >= n:
                return 1 if i == n else 0
            if i in d:
                return d[i]
            a = dfs(i + 1)
            b = dfs(i + 2)
            d[i] = a + b
            return d[i]
        return dfs(0)

        
        