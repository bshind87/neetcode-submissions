class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []

        def explore(start, csum):
            if csum == target:
                res.append(path[:])   # copy the current path
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                n = candidates[i]
                if csum + n > target:
                    break  # nums isn't sorted here, so don't break, just skip
                path.append(n)
                explore(i + 1, csum + n)   # 'i' not 'i+1': reuse same number allowed
                path.pop()             # backtrack

        explore(0, 0)
        return res
        