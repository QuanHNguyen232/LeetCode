# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # base case
        if not root:
            return root

        # recursion
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        if not (root.left or root.right) and root.val==0:
            return None
        else:
            return root