# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaves(root: TreeNode, arr: List):
            if not root: return
            if not root.left and not root.right:
                arr.append(root.val)
            get_leaves(root.left, arr)
            get_leaves(root.right, arr)
        
        leaves1 = []
        leaves2 = []
        get_leaves(root1, leaves1)
        get_leaves(root2, leaves2)
        return leaves1==leaves2