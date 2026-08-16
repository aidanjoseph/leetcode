class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []
        def backtrack(i):
            if len(nums) == i:
                res.append(sub[:])
                return
            sub.append(nums[i])
            backtrack(i+1)

            sub.pop()
            backtrack(i+1)

        backtrack(0)
        return res