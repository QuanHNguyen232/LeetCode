class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.nrows = len(matrix)
        self.ncols = len(matrix)
        self.original = matrix
        self.prefix = deepcopy(matrix)

        for i, row in enumerate(self.prefix):
            self.prefix[i] = list(itertools.accumulate(row))
        
        for r in range(1, self.nrows):
            for c in range(0, self.ncols):
                self.prefix[r][c] += self.prefix[r-1][c]
        
    def update(self, row: int, col: int, val: int) -> None:
        diff = val - self.original[row][col]
        self.original[row][col] = val

        for r in range(row, self.nrows):
            for c in range(col, self.ncols):
                self.prefix[r][c] += diff

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.prefix[row2][col2]
        ans -= self.prefix[row1-1][col2] if row1>0 else 0
        ans -= self.prefix[row2][col1-1] if col1>0 else 0
        ans += self.prefix[row1-1][col1-1] if (row1>0 and col1>0) else 0
        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)