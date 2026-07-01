class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        transposed = [list(row) for row in zip(*board)]
        
        #row check
        for l in board:
            seen = []
            for i in l:
                if i in seen and i != '.':
                    return False
                else:
                    seen.append(i)

        #column check
        for l in transposed:
            seen = []
            for i in l:
                if i in seen and i != '.':
                    return False
                else:
                    seen.append(i)
        
        #3x3 sub box check
        for i in [1, 4, 7]:
            for j in [1, 4, 7]:
                v = []
                for ii in [-1, 0, 1]:
                    for jj in [-1, 0, 1]:
                        #print("i=",i," j=",j," ii=",ii, " jj=", jj)
                        #print("board[i+ii][j+jj] = ", board[i+ii][j+jj])
                        if board[i+ii][j+jj] != '.' and board[i+ii][j+jj] not in v:
                            v.append(board[i+ii][j+jj])
                        elif board[i+ii][j+jj] in v:
                            return False

        return True