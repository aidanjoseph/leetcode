'''
Not my best solution, needed bit of help
better solution utilizes while q and fresh > 0
tht way we don't need this little ugly if rotted check
'''

from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def checkFresh():
            fresh = 0 
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 1:
                        fresh += 1
            return fresh
        if checkFresh() == 0:
            return 0
        q = collections.deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
        minutes = 0
        while q:
            rotted = False
            for _ in range(len(q)):
                r, c = q.popleft()
                directions = ([0,1],[1,0],[0,-1],[-1,0])
                for dr, dc in directions:
                    if dr + r < 0 or dc + c < 0 or c + dc == cols:
                        continue
                    if r + dr == rows:
                        continue 
                    if grid[r+dr][c+dc] == 2 or grid[r+dr][c+dc] == 0:
                        continue
                    q.append((r+dr, c + dc))
                    grid[r+dr][c+dc] = 2
                    rotted = True
            if rotted:
                minutes += 1
                rotted = False
        if checkFresh() == 0:
            return minutes
        return -1
        

        