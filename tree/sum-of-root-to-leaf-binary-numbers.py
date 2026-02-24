# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans = []
        curr_soln = []

        # backtrack
        def choose(node):
            # base case: node is leaf
            if not node.left and not node.right:
                tmp = curr_soln[:] + [node.val]
                tmp = [str(val) for val in tmp]
                ans.append(''.join(tmp))
                return
            
            # recursion
            curr_soln.append(node.val)
            if node.left:
                choose(node.left)
            if node.right:
                choose(node.right)
            curr_soln.pop()
        
        choose(root)
        ans = [int(val, 2) for val in ans]
        return sum(ans)
