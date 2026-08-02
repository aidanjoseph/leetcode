class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #calculate a left product
        #calculate a right product, 
        #then iterate thorugh and mult those left and right prods?
        left = []
        curr = 1
        for l in range(len(nums)):
            curr *= nums[l]
            left.append(curr)
        right = []
        curr = 1
        for r in range(len(nums) -1, -1, -1):
            curr *= nums[r]
            right.append(curr)
        res = []
        right = right[::-1]
        for i in range(len(nums)):
            if i == 0:
                res.append(right[1])
            elif i == len(nums) - 1:
                res.append(left[-2])
            else:
                res.append(left[i-1] * right[i+1])
        return res