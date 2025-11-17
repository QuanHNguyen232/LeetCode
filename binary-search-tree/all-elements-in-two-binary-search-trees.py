# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        def dfs(root, arr):
            if not root:
                return

            dfs(root.left, arr)
            arr.append(root.val)
            dfs(root.right, arr)
        
        arr1 = []
        arr2 = []
        dfs(root1, arr1)
        dfs(root2, arr2)

        # merge: merge_sort or binary_search+array.insert
        ans = []
        if len(arr1) < len(arr2):
            # arr1 always longer
            arr1, arr2 = arr2, arr1
        len1 = len(arr1)
        len2 = len(arr2)
        print("len", len1, len2)
        ptr1, ptr2 = 0, 0
        while ptr1 < len1 and ptr2 < len2:
            val1, val2 = arr1[ptr1], arr2[ptr2]
            if val1 <= val2:
                ans.append(val1)
                ptr1 += 1
            else:
                ans.append(val2)
                ptr2 += 1
        
        ptr_remain = ptr1 if ptr1 < len1 else ptr2
        arr_remain = arr1 if ptr1 < len1 else arr2
        ans = ans + arr_remain[ptr_remain:]
        return ans