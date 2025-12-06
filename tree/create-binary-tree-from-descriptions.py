# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        hashmap = {}
        root = None
        for desc in descriptions:
            parent, child, isLeft = desc
            if parent not in hashmap:
                root = parent
                hashmap[parent] = TreeNode(parent)
            if child not in hashmap:
                hashmap[child] = TreeNode(child)
            
            if isLeft:
                hashmap[parent].left = hashmap[child]
            else:
                hashmap[parent].right = hashmap[child]
        
        return hashmap[root]