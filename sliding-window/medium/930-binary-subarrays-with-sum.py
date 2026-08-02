class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        def helper(num):
            if num < 0:
                return 0
            res = 0            
            left, curr = 0, 0
            for right in range(len(nums)):
                curr += nums[right]
                while curr > num:
                    curr -= nums[left]
                    left += 1
                res += (right - left + 1)
            return res
        return helper(goal) - helper(goal - 1)