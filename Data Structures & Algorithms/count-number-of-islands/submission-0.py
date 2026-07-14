class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        cnt = 0
        def checkNum(i,j):
            if grid[i][j] == '0':
                print("Zero", i," ",j)
                return
            if grid[i][j] == '1':
                print("Recursion", i," ",j)
                grid[i][j] = '2'
                if i+1 < m:
                    checkNum(i+1, j)
                if i-1 >= 0:
                    checkNum(i-1, j)
                if j+1 < n:
                    checkNum(i, j+1)
                if j-1 >= 0:
                    checkNum(i, j-1)
                return
        
        for ii in range(m):
            for jj in range(n):
                if grid[ii][jj] == '1':
                    #print(grid[ii][jj])
                    cnt += 1
                    checkNum(ii,jj)
                    print(grid)
        return cnt
        