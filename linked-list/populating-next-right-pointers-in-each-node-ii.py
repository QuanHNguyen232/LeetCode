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
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root

        # bfs by level
        def bfs(root):
            queue = deque()
            queue.append(root)

            while queue:
                next_queue = deque()
                
                while queue:
                    node = queue.popleft()

                    # create right connection
                    if queue:
                        node.next = queue[0]

                    # prep next iteration
                    if node.left:
                        next_queue.append(node.left)
                    if node.right:
                        next_queue.append(node.right)

                queue = next_queue

        bfs(root)
        return root