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
          
        def dijkstra():
            arr = []
            heapq.heappush(arr, (0, 0, 0))
            while arr:
                cost, r, c = heapq.heappop(arr)
                
                if cost_map[r][c] < cost: continue
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
        
        dijkstra()
        return cost_map[nrows-1][ncols-1]