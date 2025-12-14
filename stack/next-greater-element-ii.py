class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        [1,5,3,2,4,3]
        add curr (1) to stack, stack=[1]
        1 vs 5 -> next bigger for 1 is 5, add curr (5) to stack, stack=[5]
        5 vs 3 -> add curr (3) to stack, stack=[5,3]
        5,3 vs 2 -> add curr (3) to stack, stack=[5,3,2]
        5,3,2 vs 4 -> next bigger for 2 is 4, next bigger for 3 is 4, add curr (4) to stack, stack=[5,4]
        5,4 vs 3 -> add curr (3) to stack, stack=[5,4,3]
        (new circle)
        5,4,3 vs 1 -> add curr (1) to stack, stack=[5,4,3,1]
        5,4,3,1 vs 5 -> next bigger for 1 is 5, next bigger for 3 is 5, next bigger for 4 is 5, add curr (5), stack=[5,5]
        5,5 vs 3
        5,5,3 vs 2
        5,5,3,2 vs 4 -> next bigger for 2 is 4, next bigger for 3 is 4, add curr (4) to stack, stack=[5,5,4]
        5,5,4 vs 3 -> 5,5,4,3
        END
        5 not update -> init w/ ans = [-1]*n
        """
        nums.extend(nums) # create circle
        n = len(nums)//2
        ans = [-1]*n
        stack = deque()
        for i, curr in enumerate(nums):
            idx = i % n
            while stack and stack[-1][0] < curr:
                prev, prev_idx = stack.pop()
                ans[prev_idx] = curr

            stack.append([curr, idx])

        return ans