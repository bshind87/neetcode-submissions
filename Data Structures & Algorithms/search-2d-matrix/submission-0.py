class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for r in matrix:
            if target >= r[0] and target <= r[len(r)-1]:
                for i in r:
                    if i == target:
                        return True
        return False