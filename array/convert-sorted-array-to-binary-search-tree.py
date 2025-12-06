# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        [-10,-3,0,5,9], n=5
        [  0, 1,2,3,4]
        
        [0:4] mid=(0+4)//2=2 -> node=0
            [0:1] mid=(0+1)//2=0 -> node=-10
                [0:-1] -> invalid
                [1:2] mid=(1+2)//2=1 -> node=-3
            [3:4]: mid=(3+4)//2=3 -> node=5
                [3:2] -> invalid
                [4:4] mid=(4+4)//2=4 -> node=9
        """
        def bst_creator(left, right) -> Optional[TreeNode]:
            # base case
            if left > right:
                return None

            # do sth
            mid = (left+right)//2
            node = TreeNode(nums[mid])
            
            # recursion
            node.left = bst_creator(left, mid-1)
            node.right = bst_creator(mid+1, right)
            
            return node

        return bst_creator(0, len(nums)-1)