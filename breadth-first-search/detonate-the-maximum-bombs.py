class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # bfs
        
        def get_distance(x1,y1, x2,y2):
            return sqrt((x1-x2)**2 + (y1-y2)**2)
        
        graph = defaultdict(list)
        for i, bomb1 in enumerate(bombs):
            for j, bomb2 in enumerate(bombs):
                if i==j: continue
                distance = get_distance(bomb1[0],bomb1[1], bomb2[0],bomb2[1])
                if distance <= bomb1[2]:
                    graph[i].append(j)
        
        def bfs(i):
            visited = set()
            queue = deque()
            queue.append(i)
            cnt = 0
            while queue:
                cur_bomb = queue.popleft()

                if cur_bomb in visited: continue
                visited.add(cur_bomb)
                cnt += 1

                for next_bomb in graph[cur_bomb]:
                    if next_bomb not in visited:
                        queue.append(next_bomb)

            return cnt

        ans = 0
        for i, bomb1 in enumerate(bombs):
            num_bombs = bfs(i)
            ans = max(ans, num_bombs)

        return ans