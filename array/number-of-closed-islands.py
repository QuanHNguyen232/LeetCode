class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        """
        as long as island does not touch boundary (row=0 or col=0) -> closed island
        init isClosed = True. if, at grid[r][c], r=0 or c=0 -> isClosed=False
        if isClosed -> ans += 1
        """
        nrows = len(grid)
        ncols = len(grid[0])
        LAND = 0
        WATER = 1
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ans = 0
        visited = set()
        
        def isInBound(r, c):
            return (0<= r < nrows) and (0 <= c < ncols)

        def bfs(r, c) -> bool:
            isClosed = True
            queue = deque()
            queue.append((r, c))

            while queue:
                r, c = queue.popleft()

                if (r, c) in visited: continue
                visited.add((r, c))
                if (
                    r==0 or r==nrows-1
                    or c==0 or c==ncols-1
                ): # touch grid boundary
                    isClosed = False
                
                for mr, mc in directions:
                    newR, newC = mr+r, mc+c
                    if (
                        isInBound(newR, newC)
                        and (newR, newC) not in visited
                        and grid[newR][newC] == LAND
                    ):
                        queue.append((newR, newC))
            
            return isClosed

        
        for r in range(nrows):
            for c in range(ncols):
                if (r, c) not in visited and grid[r][c]==LAND:
                    is_island_closed = bfs(r, c)
                    ans += 1 if is_island_closed else 0
        return ans