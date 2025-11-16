# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
               dummy
              /
             0
            / \
          -2   2
          /\   /\
        -3 -1 1  3
        """
        dummy = TreeNode(val=math.inf, left=root)
        
        def find_rm_node(root, key) -> [TreeNode, TreeNode]:
            prev = dummy
            curr = root
            while curr:
                if curr.val == key:
                    print(f'find: prev={prev.val if prev else prev}, curr={curr.val if curr else curr}')
                    return prev, curr
                elif key < curr.val:
                    prev = curr
                    curr = curr.left
                else:
                    prev = curr
                    curr = curr.right
            return (None, None)

        def find_replace_node(node: TreeNode, is_right=True) -> [TreeNode]:
            prev = node
            if is_right:
                curr = node.left
            else:
                curr = node.right
            while curr:
                if is_right and curr.right:
                    prev = curr
                    curr = curr.right
                elif not is_right and curr.left:
                    prev = curr
                    curr = curr.left
                else:
                    break

            # rm connect bw prev & curr
            if curr == prev.left:
                prev.left = curr.left
            else:
                prev.right = curr.right
            print(f'replace: prev={prev.val if prev else prev}, curr={curr.val if curr else curr}')
            return curr

        prev_node, rm_node = find_rm_node(root, key)

        if rm_node is None:
            return root
        
        # find replace
        if prev_node.left == rm_node:
            replace_node = find_replace_node(rm_node, is_right=True)
        else:
            replace_node = find_replace_node(rm_node, is_right=False)

        # connect new node
        if prev_node.left == rm_node:
            prev_node.left = replace_node
        else:
            prev_node.right = replace_node
        
        # print("prev_node", prev_node)
        # print("replace_node", replace_node)
        
        if replace_node is not None:
            # update new node's left and right
            replace_node.left = rm_node.left
            replace_node.right = rm_node.right
        
        # rm node
        rm_node.left = rm_node.right = None

        return dummy.left