class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0]*n for i in range(m)]
        # positions on same rows/cols as (0, 0) have only 1 path
        for r in range(m):
            grid[r][0] = 1
        for c in range(n):
            grid[0][c] = 1

        # BOTTOM UP
        for r in range(1, m):
            for c in range(1, n):
                grid[r][c] = grid[r][c-1] + grid[r-1][c]

        return grid[m-1][n-1]