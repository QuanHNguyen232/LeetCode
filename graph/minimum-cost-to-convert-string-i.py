class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = defaultdict(list)
        for src, dst, c in zip(original, changed, cost):
            graph[src].append((c, dst))

        # using dijkstra only causes TLE --> use memory (DP)
        @cache
        def dijkstra(src: str, dst: str) -> int:
            """
            return min cost (int) to convert from src -> dst
            """
            heap = []
            heapq.heappush(heap, (0, src))
            visited = set()

            while heap:
                curr_cost, node = heapq.heappop(heap)

                if node in visited: continue
                visited.add(node)
                if node == dst:
                    return curr_cost

                for next_cost, neighbor in graph[node]:
                    if neighbor not in visited:
                        heapq.heappush(heap, (curr_cost + next_cost, neighbor))

            return -1 # cannot find path

        n = len(source)
        ans = 0
        for i in range(n):
            if source[i] == target[i]: continue
            # find shortest path to convert char from source[i] -> target[i]
            min_cost = dijkstra(source[i], target[i])
            if min_cost == -1:
                return -1
            ans += min_cost
        
        return ans