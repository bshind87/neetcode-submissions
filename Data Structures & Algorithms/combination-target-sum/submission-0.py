class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        l = []
        path = []

        def explore(start, csum):
            if csum == target:
                l.append(path[:])   # copy the current path
                return
            if csum > target:
                return
            for i in range(start, len(nums)):
                n = nums[i]
                if csum + n > target:
                    continue  # nums isn't sorted here, so don't break, just skip
                path.append(n)
                explore(i, csum + n)   # 'i' not 'i+1': reuse same number allowed
                path.pop()             # backtrack

        explore(0, 0)
        return l
                    
        