class Solution:
    def latestDayToCross(self, row: int, col: int, cells: list[list[int]]) -> int:
        def bfs(row, col, cells, day):
            grid = [[0] * col for _ in range(row)]
            q = collections.deque([])
            for r, c in cells[:day]:
                grid[r-1][c-1] = 1
            for i in range(col):
                if not grid[0][i]:
                    q.append((0,i))
                    grid[0][i] = -1
            while q:
                r, c = q.popleft()
                if r == row - 1:
                    return True
                directions = [[0,1],[1,0],[-1,0],[0,-1]]
                for dr, dc in directions:
                    x, y = r + dr, c + dc
                    if 0 <= x < row and 0 <= y < col and grid[x][y] == 0:
                        grid[x][y] = -1
                        q.append((x,y))
            return False
        left, right = 1, row * col
        while left <= right:
            mid = left + (right - left) // 2
            if bfs(row, col, cells, mid):
                left = mid + 1
            else:
                right = mid - 1
        return right