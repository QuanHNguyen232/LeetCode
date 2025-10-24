# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = True
        def dfs(currNode) -> int:
            nonlocal ans

            # base case
            if not currNode:
                return 0

            # recursion
            left_depth = dfs(currNode.left)
            right_depth = dfs(currNode.right)
            if abs(left_depth - right_depth) > 1:
                ans = False
            return max(left_depth, right_depth) + 1

        dfs(root)
        return ans