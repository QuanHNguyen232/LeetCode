class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        """
        [(x1,y1),(x2,y2)] -> smallest x=0 y=0
        island1 = [(0,0)(0,1)(1,0)]
        island2 = [(2,4)(3,3)(3,4)] -> minX=2, minY=3 -> [(0,1)(1,0)(1,1)]
        shape = {
        (0,1)(1,0)(1,1)=key: int
        }

        time=space= O(n*m)
        """
        nrows = len(grid)
        ncols = len(grid[0])
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        LAND = 1
        shapes = defaultdict(int)

        def isInBound(r, c) -> bool:
            return 0 <= r < nrows and 0 <= c < ncols

        def bfs(r: int, c: int) -> None:
            queue = deque()
            queue.append([r, c])
            key = []

            while queue:
                r, c = queue.popleft()

                if (r, c) in visited: continue
                visited.add((r, c))
                key.append([r,c])

                for mr, mc in directions:
                    new_r, new_c = r+mr, c+mc
                    if (
                        isInBound(new_r, new_c)
                        and (new_r, new_c) not in visited
                        and grid[new_r][new_c] == LAND
                    ):
                        queue.append([new_r, new_c])
            
            # handle key
            # find min
            minX, minY = key[0]
            for x, y in key:
                minX = min(minX, x)
                minY = min(minY, y)
            # normalize
            for i in range(len(key)):
                x, y = key[i]
                key[i] = f"({x-minX},{y-minY})"
                
            shapes["".join(key)] += 1

        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c] == LAND and (r,c) not in visited:
                    bfs(r, c)

        return len(shapes)
