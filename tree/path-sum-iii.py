# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        self.ans, self.targetSum = 0, targetSum
        self.visited = defaultdict(int)
        self.visited[0] = 1 # 1 way to get 0 sum (aka starting point)

        self.dfs(root, 0)
        return self.ans

    def dfs(self, root, currSum):
        if not root: return

        currSum += root.val

        self.ans += self.visited[currSum - self.targetSum]

        # backtrack
        self.visited[currSum] += 1

        self.dfs(root.left, currSum)
        self.dfs(root.right, currSum)

        self.visited[currSum] -= 1
