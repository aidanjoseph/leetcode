class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        preSum = {0:-1}
        prefix_Mod = 0 
        for i in range(len(nums)):
            prefix_Mod = (prefix_Mod + nums[i]) % k
            if (prefix_Mod) in preSum:
                if i - preSum[prefix_Mod] > 1:
                    return True
            else:
                preSum[prefix_Mod] = i
            
        return False