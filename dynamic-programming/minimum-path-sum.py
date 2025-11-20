class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        for r in range(m):
            for c in range(n):
                if r == 0 and c==0: continue
                upper = grid[r-1][c] if r-1>=0 else math.inf
                left = grid[r][c-1] if c-1>=0 else math.inf
                grid[r][c] += min(upper, left)
        
        return grid[-1][-1]