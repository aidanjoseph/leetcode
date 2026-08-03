class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         nums[i] = -1
        prefix = 0 
        preSums = {}
        res = 0
        for i in range(len(nums)):
            prefix += nums[i]
            if nums[i] == 0:
                prefix -= 1
            if prefix == 0:
                res = i + 1
            elif prefix in preSums:
                res = max(res, i - preSums[prefix])
            if prefix not in preSums:
                preSums[prefix] = i
        return res