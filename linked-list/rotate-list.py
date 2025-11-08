# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        # create ring & get list_len
        list_len = 0
        end = curr = head
        while curr:
            # get last node
            list_len += 1
            end = curr
            curr = curr.next

        # get idx to become next head
        next_head_idx = list_len - (k % list_len)
        if next_head_idx == 0:
            return head

        # create ring
        end.next = head
        curr = head
        curr_idx = 0
        new_head = head
        while curr:
            if curr_idx == next_head_idx-1:
                new_head = curr.next
                curr.next = None
                break
            curr = curr.next
            curr_idx += 1
        
        return new_head