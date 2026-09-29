class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        marker = [2]
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        def dfs(r,c):
            num = 1
            if grid[r][c] != 1:
                return
            grid[r][c] = marker[0]
            for dr, dc in directions:
                x = dr + r
                y = dc + c
                if x < 0 or x == len(grid) or y < 0 or y == len(grid[0]) or grid[x][y] != 1:
                    continue
                num += dfs(x,y)
            return num
        islands = {}
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    num = dfs(r,c)
                    res = max(res, num)
                    islands[grid[r][c]] = num 
                    marker[0] += 1

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    possible = 1
                    neighs = set()
                    for dr, dc in directions:
                        x = dr + r
                        y = dc + c
                        if x < 0 or x == len(grid) or y < 0 or y == len(grid[0]) or grid[x][y] == 0:
                            continue
                        neighs.add(grid[x][y])
                    for item in neighs:
                        possible += islands[item]
                    res = max(res, possible)
        return res
                        
