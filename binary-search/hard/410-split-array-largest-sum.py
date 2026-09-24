class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:

        def min_subs(max_allowed):
            curr = 0 
            splits = 0

            for num in nums:
                if curr + num <= max_allowed:
                    curr += num
                else:
                    curr = num
                    splits += 1
            return splits + 1
        left = max(nums)
        right = sum(nums)

        while left <= right:
            max_sum = left + (right - left) // 2

            if min_subs(max_sum) <= k:
                right = max_sum - 1
                minimum_largest_split = max_sum
            else:
                left = max_sum + 1
        return minimum_largest_split
        