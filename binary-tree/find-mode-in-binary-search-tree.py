# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        most_freq = Counter()

        def dfs(node: TreeNode) -> None:
            if not node: return

            # do sth
            most_freq[node.val] += 1

            # recursion
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        max_freq = max(most_freq.values())
        ans = [key for key in most_freq if most_freq[key] == max_freq]
        return ans