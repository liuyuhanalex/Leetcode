# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        record = ListNode(0, head)
        new_head = record
        before = record
        while head is not None:
            if head.val == val:
                before.next = head.next
            else:
                before = before.next
            head = head.next
        return new_head.next
