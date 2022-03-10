from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        pos = 1
        res = head
        before, before_head, new_right = None, None, None
        while head.next is not None:
            if pos == left - 1:
                before_head = head
                new_right = head.next
            elif left <= pos < right:
                next_node = head.next
                head.next = before
                before = head
                head = next_node
            elif pos == right:
                next_node = head.next
                before_head.next = head
                new_right.next = next_node
            else:
                head = head.next
            pos += 1
        return res