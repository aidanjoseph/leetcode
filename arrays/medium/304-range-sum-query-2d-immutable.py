class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix = []
        for r in range(len(self.matrix)):
            new = []
            for c in range(len(self.matrix[0])):
                new.append(0)
            self.prefix.append(new)
        for i in range(len(self.matrix)):
            rowSum = 0
            for j in range(len(self.matrix[0])):
                if i != 0:
                    self.prefix[i][j] = self.prefix[i-1][j] + rowSum + self.matrix[i][j]
                else:
                    self.prefix[i][j] = rowSum + self.matrix[i][j]
                rowSum += self.matrix[i][j]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.prefix[row2][col2]

        if row1 > 0:
            total -= self.prefix[row1 - 1][col2]

        if col1 > 0:
            total -= self.prefix[row2][col1 - 1]

        if row1 > 0 and col1 > 0:
            total += self.prefix[row1 - 1][col1 - 1]
        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)