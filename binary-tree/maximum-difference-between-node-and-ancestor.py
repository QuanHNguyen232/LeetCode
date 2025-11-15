# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root, ancestorMax: int, ancestorMin: int):
            nonlocal ans
            # get max diff
            diff = max(
                abs(ancestorMax - root.val),
                abs(ancestorMin - root.val),
            )
            ans = max(ans, diff)
            # update max, min
            ancestorMax = max(ancestorMax, root.val)
            ancestorMin = min(ancestorMin, root.val)
            # recursion
            if root.left:
                dfs(root.left, ancestorMax, ancestorMin)
            if root.right:
                dfs(root.right, ancestorMax, ancestorMin)

        ans = 0
        dfs(root, ancestorMax=root.val, ancestorMin=root.val)
        return ans