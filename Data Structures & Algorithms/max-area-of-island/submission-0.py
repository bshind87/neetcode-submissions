class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        mx = 0
        def visit(i, j, cnt):
            if grid[i][j] == 1:
                grid[i][j] = 2
                cnt += 1
            else:
                return cnt
            if i < len(grid) - 1:
                cnt = visit(i+1,j, cnt)
            if i > 0:
                cnt = visit(i-1, j, cnt)
            if j < len(grid[0]) - 1:
                cnt = visit(i,j+1,cnt)
            if j > 0 :
                cnt = visit(i,j-1,cnt)
            return cnt
        ct = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    print(i," ",j)
                    ct = max(ct, visit(i, j, 0))
        return ct


        