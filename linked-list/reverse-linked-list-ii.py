# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head: return head

        prev_left, leftNode, _ = self.findNode(head, left)
        _, rightNode, right_after = self.findNode(head, right)
        
        if leftNode and rightNode:
            # reverse
            newLeft, newRight = self.reverse(leftNode, rightNode)
            # merge
            if prev_left:
                prev_left.next = newLeft
            else:
                head = newLeft
            newRight.next = right_after
            return head
        else:
            return head
    
    def reverse(self, nodeStart: Optional[ListNode], nodeEnd: Optional[ListNode]) -> (Optional[ListNode], Optional[ListNode]):
        prev = None
        curr = nodeStart
        while curr:
            tmp = curr.next
            curr.next = prev
            # stop
            if curr == nodeEnd: break
            # go to next node
            prev = curr
            curr = tmp
        return nodeEnd, nodeStart

    def findNode(self, head: Optional[ListNode], val: int) -> (Optional[ListNode], Optional[ListNode], Optional[ListNode]):
        prev = None
        curr = head
        while curr:
            if curr.val == val:
                return prev, curr, curr.next
            prev = curr
            curr = curr.next
        return None, None, None
