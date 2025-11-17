# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        def inOrder_traverse(root, arr):
            if not root: return
            inOrder_traverse(root.left, arr)
            arr.append(root.val)
            inOrder_traverse(root.right, arr)
        
        def create_BST(arr):
            if len(arr)==0: return None
            mid = len(arr)//2
            root = TreeNode(arr[mid])
            root.left = create_BST(arr[:mid])
            root.right = create_BST(arr[mid+1:])
            return root
        
        
        arr = []
        inOrder_traverse(root, arr)
        return create_BST(arr)