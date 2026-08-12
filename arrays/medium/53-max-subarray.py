class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        currSub = nums[0]

        for i in range(1, len(nums)):
            currSub = max(nums[i], nums[i] + currSub)
            maxSub = max(currSub, maxSub)
        return maxSub