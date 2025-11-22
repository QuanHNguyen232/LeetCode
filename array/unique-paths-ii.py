class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        OBSTACLE = 1
        SPACE = 0
        
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1: return 0
        
        grid = [[0]*n for i in range(m)]
        # positions on same rows/cols as (0, 0) have only 1 path
        for r in range(m):
            if obstacleGrid[r][0] == OBSTACLE:
                # if see obstacle --> from this to end of 0-th col cannot go
                for j in range(r, m):
                    obstacleGrid[j][0] = OBSTACLE
                break
            grid[r][0] = 1
        for c in range(n):
            if obstacleGrid[0][c] == OBSTACLE:
                # if see obstacle --> from this to end of 0-th row cannot go
                for j in range(c, m):
                    obstacleGrid[0][c] = OBSTACLE
                break
            grid[0][c] = 1

        # BOTTOM UP
        for r in range(1, m):
            for c in range(1, n):
                if obstacleGrid[r][c] == OBSTACLE: continue
                grid[r][c] = grid[r][c-1] + grid[r-1][c]
        
        return grid[m-1][n-1]