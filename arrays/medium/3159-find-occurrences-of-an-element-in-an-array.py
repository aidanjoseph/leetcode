class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        #modified counter
        ind = {}

        for i in range(len(nums)):
            if x in ind and nums[i] == x:
                ind[nums[i]].append(i)
            elif nums[i] == x:
                ind[nums[i]] = [i]
        res = []
        for num in queries:
            if x not in ind:
                res.append(-1)
            elif len(ind[x]) < num:
                res.append(-1)
            # in range
            else:
                res.append(ind[x][num-1])
        return res
        