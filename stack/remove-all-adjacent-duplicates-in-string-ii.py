class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        """
        deeedbbcccbdaa
        [d]vs[e]
            tmp=[e]
            tmp[-1]!=stack[-1] -> add tmp to stack=[d,e]
        [d,e]vs[e]
            tmp=[e]
            if stack and tmp: tmp=[-1]==stack[-1] -> stack=[d], tmp=[e,e] < k -> do nothing
            if stack and tmp: tmp=[-1]!=stack[-1] -> stop
            add tmp to stack=[d,e,e]
        [d,e,e]vs[e]
            tmp=[e]
            if stack and tmp: tmp=[-1]==stack[-1] -> stack=[d,e], tmp=[e,e] < k -> do nothing
            if stack and tmp: tmp=[-1]==stack[-1] -> stack=[d], tmp=[e,e,e] == k -> tmp=[]
            not tmp -> stop
            add tmp to stack=[d]
        [d]vs[d]
            tmp=[d]
            if stack and tmp: tmp=[-1]==stack[-1] -> stack=[], tmp=[d,d] < k -> do nothing
            not stack -> stop
            add tmp to stack=[d,d]
        [d,d]vs[b]
            tmp=[b]
            if stack and tmp: tmp=[-1]!=stack[-1] -> stop
            add tmp to stack=[d,d,b]
        [d,d,b]vs[b]
            ...
        [d,d,b,b]vs[b]
            tmp=[b]
            if stack and tmp and tmp=[-1]==stack[-1] -> stack=[d,d,b], tmp=[b,b] < k -> do nothing
            if stack and tmp and tmp=[-1]==stack[-1] -> stack=[d,d], tmp=[b,b,b]==k -> tmp=[]
            no tmp -> stop
            add tmp to stack=[d,d]
        """
        stack = deque()
        for char in s:
            tmp = [char]
            
            while stack and tmp and tmp[-1]==stack[-1]:
                tmp.append(stack.pop())
                if len(tmp) == k:
                    tmp = []
            for ele in tmp:
                stack.append(ele)

        return "".join(stack)