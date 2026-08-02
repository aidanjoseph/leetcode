class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                nums[i] = 1
            else:
                nums[i] = 0
        prefix = 0 
        prefixMap = collections.defaultdict(int)
        res = 0
        for num in nums:
            prefix += num
            if prefix == k:
                res += 1
            if prefix - k in prefixMap:
                res += prefixMap[prefix - k]
            prefixMap[prefix] += 1
        return res
        