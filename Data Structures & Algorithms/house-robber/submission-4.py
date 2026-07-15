class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
            
        cost = [0] * len(nums)
        cost[0] = nums[0]
        cost[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            cost[i] = max(cost[i-1], nums[i] + cost[i-2])
            
        return cost[-1]

        