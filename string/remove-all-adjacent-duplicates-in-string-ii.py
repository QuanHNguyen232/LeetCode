class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = deque()
        for i in s: # O(n)
            if stack and i == stack[-1][0]:
                # update the count
                stack[-1][1] += 1
                
                # rm immediately if count>=k
                if stack[-1][1] >= k:
                    stack.pop()
            else:
                stack.append([i, 1])

        return "".join([char*cnt for char, cnt in stack])
    
    def time_limit_exceed(self, s: str, k: int) -> str:
        stack = deque()
        for char in s: #O(n)
            tmp = [char]
            
            while stack and tmp and tmp[-1]==stack[-1]: # O(k)
                tmp.append(stack.pop())
                if len(tmp) == k:
                    tmp = []
            for ele in tmp:
                stack.append(ele)

        # TOTAL: O(n*k)
        return "".join(stack)