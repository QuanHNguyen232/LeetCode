class Solution:
    def trap(self, height: List[int]) -> int:
        """use stack
        [1,2,2,1,1,3]
        stack=[1]
        stack=[1]vs[2] -> 1<2 (trap) -> lowest=1, pop til find col>lowest or empty -> end (empty)
            add [2]
        stack=[2]vs[2] -> do nothing
            add [2]
        stack=[2,2]vs[1] -> do nothing
            add [1]
        stack=[2,2,1]vs[1] -> do nothing
            add [1]
        stack=[2,2,1,1]vs[3] -> 1<3 (trap) -> lowest=1, pop til find 2>lowest -> pop 2, h=min(3,2)-1=1, w=5-2-1=2 -> add [2] back
            stack=[2,2]vs[3] -> 2<3 (trap) -> lowest=2, pop til find col>lowest or empty -> end (empty)
            add [3]
        stack=[3]

        [4,2,0,3,2,5]
        stack=[4]
        stack=[4]vs[2] -> add
        stack=[4,2]vs[0] -> add
        stack=[4,2,0]vs[3] -> lowest=0, pop til find 2>0 -> pop 2, h=min(3,2)-0, w=3-1-1=1, add [2] back
            stack=[4,2]vs[3] -> lowest=2, pop til find 4>2 -> pop 4, h=min(3,4)-2=1, w=3-0-1=2, add [4] back
            stack=[4]vs[3] -> do nothing
            add [3]
        stack=[4,3]vs[2] -> do nothing
            add [2]
        stack=[4,3,2]vs[5] -> lowest=2, pop til find 3>2 -> pop 3, h=min(5,3)-2=1, w=5-3-1=1, add [3] back
            stack=[4,3]vs[5] -> lowest=3, pop til find 4>3 -> pop 4, h=min(5,4)-3=1, w=5-0-1=4, add [4] back
            stack=[4]vs[5] -> lowest=4, pop till find col>4 or empty -> end (empty)
            add [5]
        stack=[5]
        """
        ans = 0
        stack = deque()

        for i, right in enumerate(height):

            while stack and stack[-1][0] < right:
                lowest, _ = stack.pop()

                # find left col (prev col that higher than lowest)
                while stack and stack[-1][0] <= lowest:
                    stack.pop()

                # if prev col higher than lowest -> end loop. Otherwise, compute trap rain
                if stack:
                    left, left_idx = stack.pop()
                    h = min(left, right) - lowest
                    w = i - left_idx - 1
                    ans += h*w

                    # add back for next trap consideration. E.g: [4,2,0,3,2,5]
                    stack.append((left, left_idx))

            stack.append((right, i))

        return ans