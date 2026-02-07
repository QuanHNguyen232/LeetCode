class Solution:
    def minimumDeletions(self, s: str) -> int:
        cnt = 0
        stack = deque()
        for i in range(len(s)):
            c = s[i]
            if c == 'a' and len(stack)>0 and stack[-1] == 'b':
                cnt += 1
                stack.pop()
            else:
                stack.append(c)
        return cnt