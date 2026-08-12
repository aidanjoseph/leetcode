class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        res.append(intervals[0][:])
        for i in range(1, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            #outside of range
            if start > res[-1][1]:
                res.append([start, end])
            #else in range
            else:
                res[-1][1] = max(res[-1][1], end)
        return res
            
        