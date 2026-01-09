# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        deepest_depth = 0

        def get_deepest_nodes(curr, curr_depth, tree_map) -> None:
            nonlocal deepest_depth
            if curr is None: return
            tree_map[curr_depth].append(curr)
            deepest_depth = max(deepest_depth, curr_depth)

            get_deepest_nodes(curr.left, curr_depth + 1, tree_map)
            get_deepest_nodes(curr.right, curr_depth + 1, tree_map)
        
        def LCA_nodes(curr_node: Optional[TreeNode], deepest_nodes: List[TreeNode]) -> Optional[TreeNode]:
            if curr_node is None or any([curr_node == n for n in deepest_nodes]):
                return curr_node
            
            left = LCA_nodes(curr_node.left, deepest_nodes)
            right = LCA_nodes(curr_node.right, deepest_nodes)

            if left and right:
                return curr_node
            elif left:
                return left
            else:
                return right
        
        tree_map = defaultdict(list)
        get_deepest_nodes(root, 0, tree_map)
        deepest_nodes = tree_map[deepest_depth]
        
        return LCA_nodes(root, deepest_nodes)