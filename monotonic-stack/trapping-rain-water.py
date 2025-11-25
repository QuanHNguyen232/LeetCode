class Solution:
    def trap(self, height: List[int]) -> int:
        """use stack
        [0,1,0,2,1,0,1,3,2,1,2,1]
        stack=[0]
        stack=[0]vs[1] -> 0<1 (trap) -> lowest=0, pop until find col>lowest or empty -> cannot find (empty) -> add [1]
        stack=[1]vs[0] -> 1>=0 -> add
        stack=[1,0]vs[2] -> 0<2 (trap) -> lowest=0, pop til find 1>0 -> pop 1, h=min(2,1)-lowest(=1-0=1), w=idx2-idx1-1(=3-1-1=1) -> add [2]
        stack=[2]vs[1] -> 2>=1 -> add
        stack=[2,1]vs[0] -> 1>=0 -> add
        stack=[2,1,0]vs[1] -> 0<1 (trap) -> lowest=0, pop til find 1>0 -> pop 1, h=min(1,1)-0=1, w=6-4-1=1 -> add [1]
        stack=[2,1]vs[3] -> 1<3 (trap) -> lowest=1, pop till find 2>1 -> pop 2, h=min(2,3)-1=1, w=7-3-1=3 -> add [3]
        stack=[3]vs[2] -> 3>=2 -> add
        stack=[3,2]vs[1] -> 2>=1 -> add
        stack=[3,2,1]vs[2] -> 1<2 (trap) -> lowest=1, pop til find 2>1 -> pop 2, h=min(2,2)-1=1, w=10-8-1=1 -> add [2]
        stack=[3,2]vs[1] -> 2>=1 -> add
        stack=[3,2,1]

        [1,2,2,1,1,3]
        stack=[1]
        stack=[1]vs[2] -> 1<2 (trap) -> lowest=1, pop til find col>lowest or empty -> add [2]
        stack=[2]vs[2] -> 2>=2 -> add
        stack=[2,2]vs[1] -> 2>=1 -> add
        stack=[2,2,1]vs[1] -> 1>=1 -> add
        stack=[2,2,1,1]vs[3] -> 1<3 (trap) -> lowest=1, pop til find 2>lowest or empty -> pop 2, h=min(3,2)-1=1, w=5-2-1=2 -> add [3]
        stack=[2,3]

        [4,2,0,3,2,5]
        stack=[4]
        stack=[4]vs[2] -> add
        stack=[4,2]vs[0] -> add
        stack=[4,2,0]vs[3] -> lowest=0, pop til find 2>0 -> pop 2, h=min(3,2)-0, w=3-1-1=1, add [2]
            stack=[4,2]vs[3] -> lowest=2, pop til find 4>2 -> pop 4, h=min(3,4)-2=1, w=3-0-1=2, add [4]
            stack=[4]vs[3] -> add
        """
        ans = 0
        stack = deque()
        for i, right in enumerate(height):
            # print(f"i={i}, right={right}, stack={stack}")
            
            if stack and stack[-1][0] < right:
                # print("find trap water")

                while stack and stack[-1][0] < right:
                    lowest, _ = stack.pop() # 0
                    while stack and stack[-1][0] <= lowest:
                        stack.pop()
                    
                    if stack:
                        left, left_idx = stack.pop()
                        h = min(left, right) - lowest
                        w = i - left_idx - 1
                        ans += h*w

                        stack.append((left, left_idx))
                        # print(f"find lowest={lowest}, left={left}, right={right} --> add {h*w}. stack={stack}")

            # print(f"append {right}")
            stack.append((right, i))

        return ans