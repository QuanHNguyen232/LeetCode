# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return root
        node = root
        
        if node.left is None and node.right is None:
            pass
        elif node.left is None and node.right is not None:
            self.flatten(node.right)
        elif node.left is not None and node.right is None:
            node.right = node.left
            node.left = None
            self.flatten(node.right)
        else:
            node_left = node.left
            node_right = node.right
    
            self.flatten(node_left)
            
            node.left = None
            node.right = node_left
            left_rightmost = self.find_rightmost(node.right)
            left_rightmost.right = node_right


    def find_rightmost(self, node: TreeNode) -> TreeNode:
        while node.right:
            node = node.right
        return node