from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        new_head = head
        for i in range(k):
            new_head = new_head.next
        rec = head
        while rec.next is not None:
            if rec.next == new_head:
                rec.next = None
                return new_head
            rec = rec.next
        return new_head
