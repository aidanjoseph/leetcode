class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        res = 0
        for num in freq:
            if k > 0 and num + k in freq:
                res += 1
            elif k == 0 and freq[num] > 1:
                res += 1
        return res