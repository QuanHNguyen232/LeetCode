# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        hashmap = defaultdict(list)
        min_col = max_col = root_col = root_row = 0

        def dfs(node: Optional[TreeNode], row_id: int, col_id: int) -> None:
            nonlocal min_col, max_col
            if not node: return
            
            min_col = min(min_col, col_id)
            max_col = max(max_col, col_id)
            hashmap[col_id].append((node.val, row_id))
            
            dfs(node.left, row_id+1, col_id-1)
            dfs(node.right, row_id+1, col_id+1)
        
        dfs(root, root_row, root_col)

        ans = []
        for col in range(min_col, max_col+1):
            hashmap[col].sort(key=lambda x : x[1])
            ans.append([val for val, row_idx in hashmap[col]])
        
        return ans