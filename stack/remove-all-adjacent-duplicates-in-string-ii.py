class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = deque()
        for i in s:
            if stack and i == stack[-1][0]:
                # update the count
                stack[-1][1] += 1
                
                # rm immediately if count>=k
                if stack[-1][1] >= k:
                    stack.pop()
            else:
                stack.append([i, 1])

        return "".join([char*cnt for char, cnt in stack])