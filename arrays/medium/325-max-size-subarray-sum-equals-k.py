class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        preSum = {}
        prefix = 0
        res = 0
        for i in range(len(nums)):
            prefix += nums[i]
            if prefix == k:
                res = i + 1
            elif prefix - k in preSum:
                res = max(res, i - preSum[prefix-k])
            if prefix not in preSum:
                preSum[prefix] = i
        return res