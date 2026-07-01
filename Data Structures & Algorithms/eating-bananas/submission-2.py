class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = high
        while low <= high:
            mid = (low + high) // 2
            
            cur_h = 0
            for p in piles:
                cur_h += (p + mid -1) // mid
            
            if cur_h <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans