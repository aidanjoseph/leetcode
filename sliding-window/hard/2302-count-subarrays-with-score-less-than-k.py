class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        curr = 0 
        res = 0 
        start = 0 
        for i, num in enumerate(nums):
            curr += num
            score = curr * (i - start + 1)
            while score >= k:
                curr -= nums[start]
                start += 1
                score = curr * (i - start + 1)
            res += i - start + 1
        return res
        