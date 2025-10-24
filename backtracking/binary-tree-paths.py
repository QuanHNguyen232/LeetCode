# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        if not root: return ans

        def backtrack(currNode: TreeNode, curr_path: list):
            if not currNode:
                return
            
            curr_path.append(str(currNode.val))
            
            if currNode.left is None and currNode.right is None:
                ans.append("->".join(curr_path))
            
            backtrack(currNode.left, curr_path)
            backtrack(currNode.right, curr_path)
            
            curr_path.pop()
        backtrack(root, [])
        return ans
