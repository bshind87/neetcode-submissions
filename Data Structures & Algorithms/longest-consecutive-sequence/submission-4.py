class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0

        for n in nums:
            if (n-1) not in num_set:
                cur_num = n
                cur_len = 1

                while (cur_num + 1) in num_set:
                    cur_num += 1
                    cur_len += 1
                max_len = max(max_len, cur_len)
        return max_len


        # checks = [0]
        # for n in nums:
        #     small = n
        #     large = n
        #     while True:
        #         change = False
        #         if large + 1 in nums:
        #             large = large + 1
        #             change = True
        #         if small - 1 in nums:
        #             small = small - 1
        #             change = True
        #         if not change:
        #             break
        #         change = False
        #     checks.append(large - small + 1)

        # return max(checks)
