class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        #prefix prod 
        if k <= 1:
            return 0 
        curr = 1
        res = 0 
        start = 0 
        for i, num in enumerate(nums):
            curr *= num 
            while curr >= k:
                curr /= nums[start]
                start += 1
            res += i - start + 1
        return res 
                
