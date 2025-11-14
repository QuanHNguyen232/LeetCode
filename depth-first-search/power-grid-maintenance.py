class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        # create graph
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        grids = defaultdict(list)
        station2grid = defaultdict(int)
        visited = set()

        def dfs(station_idx, grid_idx):
            # base case
            if station_idx in visited:
               return

            visited.add(station_idx)
            heapq.heappush(grids[grid_idx], station_idx)
            station2grid[station_idx] = grid_idx

            # recursion
            for point in graph[station_idx]:
                dfs(point, grid_idx)
        
        # run DFS and group by grid
        curr_grid = 0
        for i in range(1, c+1):
            if i in visited: continue
            dfs(station_idx=i, grid_idx=curr_grid)
            curr_grid += 1

        # run queries
        is_off = set()
        res = []
        for op, station_id in queries:
            if op == 1:
                if station_id not in is_off:
                    res.append(station_id)
                else:
                    # if station_id in station2grid:
                    grid_idx = station2grid[station_id]
                    while (
                        grids[grid_idx] # there are stations still ON
                        and grids[grid_idx][0] in is_off
                    ):
                        heapq.heappop(grids[grid_idx]) # pop until next smallest that is not turned-off
                    res.append(grids[grid_idx][0]) if grids[grid_idx] else res.append(-1)
            else:
                is_off.add(station_id)
        
        return res