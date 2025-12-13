class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        # use bfs
        # check is_subisland by setB.issubset(setA) -> 
        # 
        count = 0
        nrows = len(grid1)
        ncols = len(grid1[0])
        LAND = 1
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        def is_in_bound(r, c):
            return (0 <= r < nrows) and (0 <= c < ncols)

        def bfs(grid, start_r, start_c, idx: int, id2set: dict) -> set:
            cell_set = set()
            queue = deque()
            queue.append([start_r, start_c])
            while queue:
                r, c = queue.popleft()
                if (r, c) in cell_set: continue
                cell_set.add((r, c))
                grid[r][c] = idx

                for mr, mc in directions:
                    new_r, new_c = mr+r, mc+c
                    if (
                        is_in_bound(new_r, new_c)
                        and (new_r, new_c) not in cell_set
                        and grid[new_r][new_c] == LAND
                    ):
                        queue.append([new_r, new_c])

            id2set[idx] = cell_set
            return cell_set

        # bfs on grid 1 -> store islands
        id2set = {}
        idx = -1
        for r in range(nrows):
            for c in range(ncols):
                if grid1[r][c] == LAND:
                    _ = bfs(grid1, r, c, idx, id2set)
                    idx -= 1

        # bfs on grid 2 -> find if this island is subisland from grid 1
        idx = -1
        for r in range(nrows):
            for c in range(ncols):
                if grid2[r][c] == LAND:
                    curr_island = bfs(grid2, r, c, -1, {})
                    # check curr_island idx on grid1 using (r, c)
                    island_idx = grid1[r][c]
                    # check is subset (subisland)
                    if (island_idx in id2set) and curr_island.issubset(id2set[island_idx]):
                        count += 1

        return count