# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1: return l2
        if not l2: return l1

        ans = ListNode(0) # dummy head
        curr = ans
        carry = 0
        p1 = l1
        p2 = l2

        while p1 and p2:
            curr, p1, p2, carry = self.get_next(curr, p1, p2, carry)

        p = p1 if p1 else p2
        while p:
            curr, p, _, carry = self.get_next(curr, p, None, carry)

        if carry > 0:
            curr.next = ListNode(carry)
        return ans.next

    def get_next(self, curr, p1, p2, carry):
        total = carry
        total += p1.val if p1 else 0
        total += p2.val if p2 else 0

        curr.next = ListNode(total % 10)
        carry = total // 10

        return curr.next, p1.next if p1 else None, p2.next if p2 else None, carry
