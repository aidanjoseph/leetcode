class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        seen = {}
        def reverse(num):
            reversed = 0
            while num != 0:
                digit = num % 10
                reversed = (reversed * 10) + digit
                num = num // 10 
            return reversed 
        res = float('inf')
        for i, num in enumerate(nums):
            reversed = reverse(num)
            if num in seen:
                res = min(i - seen[num], res)
            seen[reversed] = i
        if res == float('inf'):
            return -1
        return res

        