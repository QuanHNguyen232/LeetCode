# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        if not root:
            return ans

        def backtrack(root: TreeNode, curr_path: List, targetSum: int):
            # base case
            if not root:
                return
            
            # do sth
            targetSum -= root.val
            curr_path.append(root.val)
            if (
                targetSum == 0 and
                not root.left and
                not root.right
            ):
                ans.append(curr_path.copy())
            
            # recursion
            backtrack(root.left, curr_path, targetSum)
            backtrack(root.right, curr_path, targetSum)
            
            curr_path.pop()
        
        backtrack(root, [], targetSum)
        
        return ans