class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = set(nums)
        res = 0
        for num in nums:
            if (num - 1) not in nums:
                curr = num + 1
                length = 1
                while curr in nums:
                    length +=1
                    curr += 1
                res = max(res, length)
        return res