class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        c = []
        r = []
        for i in range(m):
            if 0 in matrix[i]:
                r.append(i)
            for j in range(n):
                if matrix[i][j] == 0:
                    c.append(j)
        for i in r:
            matrix[i] = [0] * n
        for j in c:
            for i in range(m):
                matrix[i][j] = 0
        
        