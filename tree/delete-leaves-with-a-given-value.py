# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def pruner(curr: Optional[TreeNode]) -> Optional[TreeNode]:
            if curr is None: return curr
                        
            curr.left = pruner(curr.left)
            curr.right = pruner(curr.right)

            if (
                curr.val == target
                and curr.left is None
                and curr.right is None
            ):
                return None
            
            return curr
        
        return pruner(root)
