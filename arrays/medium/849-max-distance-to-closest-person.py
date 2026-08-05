class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        #is this not just number of 0's // 2
        
        curr = 0
        highest = 0
        leftEdge = True
        leftMax = 0
        for i in range(len(seats)):
            if seats[i] == 0:
                curr += 1
                highest = max(highest, curr)
            else:
                if leftEdge:
                    leftMax = curr
                    leftEdge = False
                curr = 0
        return max(leftMax, curr, (highest + 1)// 2)
        