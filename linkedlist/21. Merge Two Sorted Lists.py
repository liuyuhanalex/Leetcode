# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode(0)
        record = new_head
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                new_head.next = l1
                l1 = l1.next
            else:
                new_head.next = l2
                l2 = l2.next
            new_head = new_head.next
        if l1 is not None:
            new_head.next = l1
        if l2 is not None:
            new_head.next = l2
        return record.next