class Solution:
    def maxDepth(self, s: str) -> int:
        n = len(s)
        stack = deque()
        ans = 0
        for i in range(n):
            if s[i] == "(":
                stack.append(s[i])
                ans = max(ans, len(stack))
            elif s[i]==")":
                if stack and stack[-1]=="(":
                    stack.pop()
        return ans