class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        curr = 0
        for num in gain:
            curr += num
            res = max(curr, res)
        return res




