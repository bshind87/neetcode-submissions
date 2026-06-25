class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cmin = prices[0]
        max_profit = 0
        for p in prices:
            cprofit = p - cmin if cmin <= p else 0
            max_profit = max(cprofit, max_profit)
            cmin = min(cmin, p)
            print(cmin, " ", p, " ", max_profit)
        return max_profit
            

        