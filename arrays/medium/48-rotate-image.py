class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #reverse rows

        rows, cols = len(matrix), len(matrix[0])

        for i in range(rows):
            for j in range(i+1, rows):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        for r in range(rows):
            left, right = 0, cols - 1
            while left < right:
                matrix[r][left], matrix[r][right] = matrix[r][right], matrix[r][left]
                left += 1
                right -= 1
        return matrix
        