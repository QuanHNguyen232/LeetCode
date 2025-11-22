"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Same as https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
        if not head: return head
        
        node = head

        if node.next is None and node.child is None:
            # last node (do nothing)
            return node
        elif node.next is not None and node.child is None:
            node.next = self.flatten(node.next)
            return node
        elif node.next is None and node.child is not None:
            child = node.child
            node.child = None
            node.next = child
            child.prev = node
            
            node.next = self.flatten(node.next)
            return node
        else:
            # flatten
            # flatten child
            # connect child's tail.next = node.next
            # connect node.next -> child
            node_next = node.next
            node_child = node.child

            # bind node <--> child
            node.child = None
            node.next = node_child
            node_child.prev = node

            # bind child <--> node's next
            child_tail = self.find_tail(node_child)
            child_tail.next = node_next
            node_next.prev = child_tail

            node.next = self.flatten(node.next)
            return node

    def find_tail(self, node) -> 'Optional[Node]':
        while node.next:
            node = node.next
        return node
            