class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        
        ret_list = []
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        
        while top <= bottom and left <= right:
            # traverse top row, left to right
            for j in range(left, right + 1):
                ret_list.append(matrix[top][j])
            top += 1
            
            # traverse right column, top to bottom
            for i in range(top, bottom + 1):
                ret_list.append(matrix[i][right])
            right -= 1
            
            # traverse bottom row, right to left (only if a row remains)
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    ret_list.append(matrix[bottom][j])
                bottom -= 1
            
            # traverse left column, bottom to top (only if a column remains)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ret_list.append(matrix[i][left])
                left += 1
        
        return ret_list