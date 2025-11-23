# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        
        n = len(postorder)
        root = TreeNode(postorder[-1])
        if n < 2: return root

        # inor: left, root, right
        # post: left, right, root
        rootIdx = inorder.index(root.val)

        inorderLeft = inorder[:rootIdx] # len must same as inorderLeft
        inorderRight = inorder[rootIdx+1:]

        postorderLeft = postorder[0 : len(inorderLeft)] # postorder[:rootIdx]
        postorderRight = postorder[len(postorderLeft) : -1]

        root.left = self.buildTree(inorderLeft, postorderLeft)
        root.right = self.buildTree(inorderRight, postorderRight)

        return root