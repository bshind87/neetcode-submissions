class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #temp, ind

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                popT, popInd = stack.pop()
                res[popInd] = i - popInd
            stack.append([temp, i])
        return res
        