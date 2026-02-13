class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        directions = {
        	1: (0, 1),
            2: (0, -1),
            3: (1, 0),
            4: (-1, 0)
        }
        nrows = len(grid)
        ncols = len(grid[0])
        cost_map = [
        	[float('inf')]*ncols
        	for _ in range(nrows)
        ]
        target = (nrows-1, ncols-1)
        
        def is_in_bound(r, c):
        	return (0 <= r < nrows) and (0 <= c < ncols)
        
        def bfs_01():
            ROWS, COLS = len(grid), len(grid[0])
            INF = float('inf')
            
            # Map grid values to directions
            direction_map = {
                1: (0, 1),   # right
                2: (0, -1),  # left
                3: (1, 0),   # down
                4: (-1, 0)   # up
            }
            
            # dist = [[INF] * COLS for _ in range(ROWS)]
            dist = cost_map
            dist[0][0] = 0
            
            dq = deque()
            dq.append((0, 0))
            
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            
            while dq:
                x, y = dq.popleft()
                curr_dir = direction_map[grid[x][y]]
                
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < ROWS and 0 <= ny < COLS:
                        # Cost is 0 if moving in preferred direction, else 1
                        cost = 0 if (dx, dy) == curr_dir else 1
                        if dist[x][y] + cost < dist[nx][ny]:
                            dist[nx][ny] = dist[x][y] + cost
                            if cost == 0:
                                dq.appendleft((nx, ny))  # 0-cost move first
                            else:
                                dq.append((nx, ny))      # 1-cost move later
                                
            return dist[ROWS - 1][COLS - 1]

        def dijkstra():
            arr = []
            heapq.heappush(arr, (0, 0, 0))
            while arr:
                cost, r, c = heapq.heappop(arr)
                
                # if cost_map[r][c] < cost: continue # this line causes TLE
                if cost_map[r][c] > cost:
                    cost_map[r][c] = cost
                    if (r, c) == target: return
                    curr_dir = grid[r][c]
                    
                    for id, (mr, mc) in directions.items():
                        new_r, new_c = r+mr, c+mc
                        new_cost = cost if id==curr_dir else cost+1
                        if (
                            is_in_bound(new_r, new_c)
                            and new_cost < cost_map[new_r][new_c]
                        ): 
                            heapq.heappush(arr, (new_cost, new_r, new_c))
        
        # dijkstra()
        bfs_01()
        return cost_map[nrows-1][ncols-1]