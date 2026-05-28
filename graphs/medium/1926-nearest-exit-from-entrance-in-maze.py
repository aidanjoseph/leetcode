'''
Brushing off rust, not too bad
Note: bfs uses popleft() , don't forget that
'''
from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        res = float('inf')
        found = False
        q = collections.deque()
        q.append((entrance[0], entrance[1]))
        steps = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if maze[r][c] == "+":
                    continue
                maze[r][c] = "+"
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    if r != entrance[0] or c != entrance[1]:
                        return steps
                if r - 1 >= 0:
                    q.append((r-1, c))
                if r + 1 <= rows -1:
                    q.append((r+1, c))
                if c - 1 >= 0:
                    q.append((r, c-1))
                if c + 1 <= cols - 1:
                    q.append((r, c+1))
            steps += 1
        if not found:
            return -1
        return res

        
