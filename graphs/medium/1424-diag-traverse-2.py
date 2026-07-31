class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diags = collections.defaultdict(list)

        for i in range(len(nums)):
            for j in range(len(nums[i])):
                diags[i+j].append(nums[i][j])
        res = []
        curr = 0
        while curr in diags:
            res.extend(diags[curr][::-1])
            curr += 1
        return res
        