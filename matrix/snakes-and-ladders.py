class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # unweighted graph -> bfs
        n = len(board)
        START_CELL = 1
        NOT_VISITED = -1
        idx2position = {}
        distance = [NOT_VISITED] * (n**2 + 1)

        # reverse Boustrophedon style -> normal board
        top, bot = 0, n-1
        while top < bot:
            board[top], board[bot] = board[bot], board[top]
            top, bot = top + 1, bot - 1
        for r in range(n):
            if r % 2 != 0:
                board[r] = board[r][::-1]

        curr_cell = START_CELL
        for r in range(n):
            for c in range(n):
                idx2position[curr_cell] = (r, c)
                curr_cell += 1

        def bfs():
            queue = deque()
            queue.append([START_CELL, 0])

            while queue:
                curr, curr_dist = queue.popleft()

                if distance[curr] != NOT_VISITED: continue
                distance[curr] = curr_dist

                for next_cell in range(curr + 1, min(curr + 6, n**2) + 1):
                    r, c = idx2position[next_cell]
                    val = board[r][c]
                    # if ladder/snake -> go there without count step
                    # e.g: curr=1, but next=2 has ladder to 15 ==> cost 1 step for 1 -> 15, instad of 2 steps (1 -> 2 -> 15)
                    next_cell = val if val != -1 else next_cell
                    queue.append([next_cell, curr_dist + 1])

        bfs()
        return distance[-1]
