# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def LCA(root: 'TreeNode') -> 'TreeNode':
            if (root is None) or (root==p) or (root==q):
                return root
            
            left = LCA(root.left)
            right = LCA(root.right)
            if left is not None and right is not None:
                return root
            if left is not None:
                return left
            else:
                return right
        
        return LCA(root)