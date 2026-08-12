class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i, h in enumerate(heights):
            start = i 
            while stack and stack[-1][1] > h:
                index, num = stack.pop()
                res = max(res, num * (i - index))
                start = index
            stack.append((start, h))
        while stack:
            index, num = stack.pop()
            res = max(res, num * (len(heights) - index))
        return res