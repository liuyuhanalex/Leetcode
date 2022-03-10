# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        record = head
        last = None
        last_val = 0
        while head is not None:
            if head.val == last_val:
                last.next = head.next
            else:
                pass
            last_val = head.val
            head = head.next
        return record