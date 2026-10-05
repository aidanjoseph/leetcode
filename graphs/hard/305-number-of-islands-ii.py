class Solution:
    def numIslands2(self, m: int, n: int, positions: list[list[int]]) -> list[int]:
        pars = [i for i in range(m*n)]
        rank = [1] * (m*n)
        graph = [[0] * n for _ in range(m)]
        def find(n1):
            res = n1
            while res != pars[res]:
                pars[res] = pars[pars[res]]
                res = pars[res]
            return res
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0 
            if rank[p2] > rank[p1]:
                pars[p1] = p2
                rank[p2] += rank[p1]
            else:
                pars[p2] = p1
                rank[p1] += rank[p2]
            return 1
        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        res = []
        islands = 0
        for r, c in positions:
            if graph[r][c] == 1:
                res.append(islands)
                continue
            graph[r][c] = 1
            islands += 1
            for dr, dc in directions:
                x = r + dr
                y = c + dc
                if x < 0 or x == m or y < 0 or y == n:
                    continue
                if graph[x][y] == 1:
                    curr = r * n + c
                    neighbor = x * n + y
                    islands -= union(curr, neighbor)
            res.append(islands)
        return res
                
