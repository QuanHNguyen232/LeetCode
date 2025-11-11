class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # return self.bfs_binarySearch(grid)
        return self.dijkstra(grid)
    
    def dijkstra(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ans = 0
        GOAL = (n-1, n-1)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def isInBound(r, c):
            return (0 <= r < n) and (0 <= c < n)
        
        def bfs_dijkstra():
            nonlocal ans
            visited = set()
            minHeap = [[grid[0][0], 0, 0]]
            
            while minHeap:
                elevation, r, c = heappop(minHeap)
                
                if (r, c) in visited: continue
                ans = max(ans, elevation)
                if (r, c) == GOAL: return ans
                visited.add((r, c))

                for mr, mc in directions:
                    newR, newC = mr + r, mc + c
                    if (
                        isInBound(newR, newC)
                        and (newR, newC) not in visited
                        # and grid[newR][newC] <= ans
                    ):
                        heappush(minHeap, [grid[newR][newC], newR, newC])
        
        bfs_dijkstra()
        return ans

    def bfs_binarySearch(self, grid: List[List[int]]) -> int:
        n = len(grid)
        N = n*n
        GOAL = (n-1, n-1)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def isInBound(r, c):
            return (0 <= r < n) and (0 <= c < n)

        def bfs(t: int) -> bool:
            visited = set()
            queue = deque()
            if grid[0][0] <= t:
                queue.append((0, 0))

            while queue:
                r, c = queue.popleft()

                if (r, c) in visited: continue
                if (r, c) == GOAL: return True
                visited.add((r, c))

                for mr, mc in directions:
                    newR, newC = mr + r, mc + c
                    if (
                        isInBound(newR, newC) and
                        (newR, newC) not in visited and
                        grid[newR][newC] <= t
                    ):
                        queue.append((newR, newC))
            
            return False
            
        left = 0
        right = N
        """
        1, 2, 3,   4, 5
        N, N, N, [Y], Y
        """
        while left < right:
            mid = left + (right-left) // 2
            ans = bfs(mid)
            # print(f"t={mid}, {ans}")
            if ans:
                right = mid
            else:
                left = mid+1

        return left