class Solution:
    def pathSum(self, nums: List[int]) -> int:
        """
        depth
        1               0
        2          0         0
        3        0   0     0   0
        4       00   00   00   00
        """
        tree = [[None]*(2**i) for i in range(0, 4)]
        
        for node in nums:
            d = (node//100)%10
            p = (node//10)%10
            v = node % 10
            tree[d-1][p-1] = v
        
        def go_left(d, p):
            # given current d, p --> get left node (by d, p)
            return d+1, p*2
        
        def go_right(d, p):
            return d+1, (p*2)+1
        
        ans = []
        def backtrack(root: [int, int], curr_path: List):
            d, p = root
            val = tree[d][p]
            
            # base case
            if val is None:
                return
            
            # do sth
            curr_path.append(val)
            left_d, left_p = go_left(*root)
            right_d, right_p = go_right(*root)
            if (
                not tree[left_d][left_p] and
                not tree[right_d][right_p]
            ):
                ans.append(sum(curr_path))

            # recursion
            backtrack(root=(left_d, left_p), curr_path=curr_path)
            backtrack(root=(right_d, right_p), curr_path=curr_path)

            curr_path.pop()

        backtrack(root=(0, 0), curr_path=[])
        return sum(ans)