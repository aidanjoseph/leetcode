class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        res = 0

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "0":
                    continue
                if r == "0" or c == "0":
                    dp[r][c] = 1
                else:
                    dp[r][c] = 1 + min(dp[r-1][c], dp[r-1][c-1], dp[r][c-1])
                res = max(res, dp[r][c])
        return res ** 2