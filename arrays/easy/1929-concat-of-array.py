class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        res = []
        for num in nums:
            res.append(num)
        for num in nums:
            res.append(num)
        return res
        