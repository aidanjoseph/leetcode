class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        seen = {}
        prefix = 0
        res = float('-inf')

        for num in nums:
            if num - k in seen:
                res = max(res, prefix + num - seen[num - k])
            elif num + k in seen:
                res = max(res, prefix + num - seen[num+k])

            if num not in seen:
                seen[num] = prefix
            else:
                seen[num] = min(seen[num], prefix)
            prefix += num
        return res