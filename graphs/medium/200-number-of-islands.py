'''
Both dfs and bfs solution here
just practice
bfs is a bit rusty
if we are going to change the input REMEMBER to do it after adding to queue
otherwise some neighbors may double add it
'''
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        dfs solution
        '''
        # rows, cols = len(grid), len(grid[0])
        # res = 0
        # seen = set()
        
        # def dfs(r, c):
        #     if (r, c) in seen or r < 0:
        #         return
        #     if c < 0 or r == rows or c == cols:
        #         return
        #     if grid[r][c] == "0":
        #         return
        #     seen.add((r,c))
        #     dfs(r+1, c)
        #     dfs(r, c+1)
        #     dfs(r-1, c)
        #     dfs(r, c-1)
        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == "1" and (r,c) not in seen:
        #             res += 1
        #             dfs(r, c)
        # return res
        rows, cols = len(grid), len(grid[0])
        directions = ((0,1), (0,-1), (1,0), (-1, 0))
        q = collections.deque([])
        def bfs(r, c):
            q.append((r,c))
            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()
                    for dr, dc in directions:
                        newR, newC = row + dr, col + dc
                        if newR < 0 or newR == rows or newC < 0 or newC == cols:
                            continue
                        if grid[newR][newC] == "0":
                            continue
                        q.append((newR, newC))
                        grid[newR][newC] = "0"
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r, c)
                    res += 1
        return res






