class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        grid = [[0]*n for i in range(m)]
        # positions on same rows/cols as (0, 0) have only 1 path
        for r in range(m):
            if obstacleGrid[r][0] == 1: continue
            grid[r][0] = 1
        for c in range(n):
            if obstacleGrid[0][c] == 1: continue
            grid[0][c] = 1

        # BOTTOM UP
        for r in range(1, m):
            for c in range(1, n):
                if obstacleGrid[r][c] == 1: continue
                grid[r][c] = grid[r][c-1] + grid[r-1][c]
        
        return grid[m-1][n-1]