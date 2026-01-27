class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for src, dst, weight in edges:
            graph[src].append((dst, weight))
            graph[dst].append((src, weight*2))
        
        def dijkstra(start, end):
            queue = []
            heappush(queue, (start, 0))
            visited = set()

            while queue:
                curr, cost = heappop(queue)
                if curr in visited: continue
                if curr == end:
                    return cost
                visited.add(curr)

                for neighbor, weight in graph[curr]:
                    if neighbor not in visited:
                        heappush(queue, (neighbor, cost + weight))

            return -1
        
        return dijkstra(0, n-1)