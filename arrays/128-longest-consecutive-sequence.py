class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #find number start counting down from it
        # check set, if one less exists continue counting down
        # once find smallest
        #set a min and max 
        # if a number we find is already in that min max range 
        # skip it
        # if we find something that is larger than range and doesn have 1 less
        # count down until we reach max then we just mix with our range
        nums = set(nums)
        res = 0
        for num in nums:
            if (num - 1) not in nums:
                length = 0
                while (num + length) in nums:
                    length += 1
                res = max(length, res)
        return res




        
