"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return
        
        queue = deque()
        queue.append(root)

        while queue:
            prev_node = None

            # go by level
            curr_queue = deque()
            while queue:
                node = queue.popleft()

                # create connection
                if prev_node:
                    prev_node.next = node
                prev_node = node

                # add nodes of next level
                if node.left:
                    curr_queue.append(node.left)
                if node.right:
                    curr_queue.append(node.right)
            
            queue = curr_queue

        return root