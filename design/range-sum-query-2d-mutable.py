class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.nrows = len(matrix)
        self.ncols = len(matrix[0])
        self.original = deepcopy(matrix)
        self.prefix = matrix
        for i, row in enumerate(self.prefix):
            self.prefix[i] = list(itertools.accumulate(row))
        
        for r in range(1, self.nrows):
            for c in range(0, self.ncols):
                self.prefix[r][c] += self.prefix[r-1][c]
        
        # print("original")
        # for row in self.original: print(row)
        # print("prefix")
        # for row in self.prefix: print(row)
        
    def update(self, row: int, col: int, val: int) -> None:
        diff = val - self.original[row][col]
        # print(f"update with ({row},{col}) val={val} --> change={diff}")
        
        self.original[row][col] += diff
        for r in range(row, self.nrows):
            for c in range(col, self.ncols):
                self.prefix[r][c] += diff
        
        
        # print("original")
        # for row in self.original: print(row)
        # print("prefix")
        # for row in self.prefix: print(row)

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