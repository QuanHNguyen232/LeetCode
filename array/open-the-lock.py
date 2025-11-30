class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        wheels = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        num_digits = 4
        next_digit_map = {wheels[i]: (wheels[i-1], wheels[(i+1)%10]) for i in range(10)}
        
        def bfs() -> int:
            queue = deque()
            queue.append(("0000", 0))
            visited = set(deadends)
            
            while queue:
                curr_lock, num_steps = queue.popleft()
                
                if curr_lock in visited: continue
                visited.add(curr_lock)
                if curr_lock == target:
                    return num_steps
                
                for i in range(num_digits):
                    tmp = list(curr_lock)
                    for digit in next_digit_map[curr_lock[i]]:
                        tmp[i] = digit
                        next_lock = ''.join(tmp)
                        if next_lock not in visited:
                            queue.append((next_lock, num_steps+1))

            return -1
        
        return bfs()