class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.nrows = len(matrix)
        self.ncols = len(matrix[0])
        # compute perfix sum
        self.preSum = [list(itertools.accumulate(row)) for row in matrix]
        for r in range(1, self.nrows):
            for c in range(self.ncols):
                self.preSum[r][c] += self.preSum[r-1][c]
    
    def is_in_bound(self, r, c):
        return 0 <= r < self.nrows and 0 <= c < self.ncols

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.preSum[row2][col2]
        ans -= self.preSum[row2][col1-1] if col1-1 >= 0 else 0
        ans -= self.preSum[row1-1][col2] if row1-1 >= 0 else 0
        ans += self.preSum[row1-1][col1-1] if row1-1 >= 0 and col1-1 >= 0 else 0
        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)