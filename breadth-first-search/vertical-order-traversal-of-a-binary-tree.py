# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        col_map = defaultdict(list)
        
        def dfs(node, row, col):
            if not node: return
            col_map[col].append([row, node.val])

            dfs(node.left, row+1, col-1)
            dfs(node.right, row+1, col+1)
        
        dfs(root, 0, 0)
        ans = []
        keys = list(col_map.keys())
        for col in sorted(keys):
            ans.append(
                [val for row, val in sorted(col_map[col], key=lambda x: (x[0],x[1]))]
            )
        return ans