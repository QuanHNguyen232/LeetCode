class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for src, dst, weight in edges:
            graph[src].append((dst, weight))
            graph[dst].append((src, weight*2))
        
        def dijkstra(start, end):
            queue = []
            heappush(queue, (0, start))
            visited = set()

            while queue:
                cost, curr = heappop(queue)
                if curr in visited: continue
                if curr == end:
                    return cost
                visited.add(curr)

                for neighbor, weight in graph[curr]:
                    if neighbor not in visited:
                        heappush(queue, (cost + weight, neighbor))

            return -1
        
        return dijkstra(0, n-1)