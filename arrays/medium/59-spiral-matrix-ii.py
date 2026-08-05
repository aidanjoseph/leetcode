class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = []
        for i in range(n):
            res.append([])
            for j in range(n):
                res[i].append(0)
        num = 1
        left, top = 0, 0
        bottom, right = n, n 

        while left < right and top < bottom:
            #top spiral
            for i in range(left, right):
                res[top][i] = num 
                num += 1
            top += 1

            #right col
            for i in range(top, bottom):
                res[i][right-1] = num
                num += 1
            right -= 1
            if not (left < right and top < bottom):
                return res
            
            #bottom row
            for i in range(right-1, left-1, -1):
                res[bottom-1][i] = num
                num += 1
            bottom -= 1 
            #left col
            for i in range(bottom-1, top-1, -1):
                res[i][left] = num 
                num += 1
            left += 1
        return res