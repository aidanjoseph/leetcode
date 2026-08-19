import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def dist(x,y):
            return math.sqrt((x**2)+(y**2))
        heap = []
        heapq.heapify([])
        for point in points:
            x, y = point
            d = dist(x,y)
            heapq.heappush(heap, (-d, x, y))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for item in heap:
            res.append([item[1], item[2]])
        return res