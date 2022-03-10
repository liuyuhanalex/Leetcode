from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rec = head
        new_head = ListNode(-1, None)
        rec_new = new_head
        while head.next is not None:
            new_head.next = ListNode(head.val, None)
            head = head.next.next
            new_head = new_head.next
        head = rec.next
        while head and head.next:
            new_head.next = ListNode(head.val, None)
            head = head.next.next
            new_head = new_head.next
        return rec_new




