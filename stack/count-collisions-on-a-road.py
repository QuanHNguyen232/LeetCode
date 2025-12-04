class Solution:
    def countCollisions(self, directions: str) -> int:
        cnt = 0
        stack = deque()
        for i, curr in enumerate(directions):
            stack.append(curr)
            while len(stack) >= 2:
                curr = stack.pop()
                prev = stack.pop()
                if prev == "R" and curr == "L":
                    cnt += 2
                    stack.append("S")
                elif prev == "S" and curr == "L":
                    cnt += 1
                    stack.append("S")
                elif prev == "R" and curr == "S":
                    cnt += 1
                    stack.append("S")
                else:
                    stack.append(prev)
                    stack.append(curr)
                    break
        return cnt