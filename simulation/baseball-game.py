class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = deque()
        for op in operations:
            if op == "+":
                curr = stack[-1]
                prev = stack[-2]
                new = curr + prev
                stack.append(new)
            elif op == "D":
                curr = stack[-1]
                new = curr * 2
                stack.append(new)
            elif op == "C":
                stack.pop()
            else:
                sign = 1
                if op.startswith("-"):
                    sign = -1
                    op = op[1:]
                new = int(op) * sign
                stack.append(new)
        
        return sum(stack)