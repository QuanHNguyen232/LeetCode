class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.nrows = len(matrix)
        self.ncols = len(matrix)
        self.matrix = matrix
        for row in self.matrix: print(row)
        print("-"*20)
        for i, row in enumerate(self.matrix):
            self.matrix[i] = list(itertools.accumulate(row))
        
        for r in range(self.n)
        
        for row in self.matrix: print(row)

    def update(self, row: int, col: int, val: int) -> None:
        pass

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return 0


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)