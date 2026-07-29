class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        res = 0
        maps = defaultdict(int)
        for num in nums1:
            for num2 in nums2:
                maps[num + num2] += 1
        
        for num in nums3:
            for num2 in nums4:
                res += maps[-(num+num2)]
        return res
