class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        seen = set()
        def dfs(r,c):
            num = 1
            if (r,c) in seen or grid[r][c] == 0:
                return 0 
            seen.add((r,c))
            directions = [[0,1], [0,-1], [1,0],[-1,0]]
            for dr, dc in directions:
                x = dr + r
                y = dc + c
                if x < 0 or x == len(grid) or y < 0 or y == len(grid[0]) or (x,y) in seen: 
                    continue
                num += dfs(x,y)
            return num 
        res = 0 
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    res = max(dfs(row,col),res)
        return res

            
        