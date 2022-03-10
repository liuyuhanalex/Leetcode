# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_than, greater_than = ListNode(-1, None), ListNode(-1, None)
        less_than_move, greater_than_move = less_than, greater_than
        while head.next is not None:
            next_node = head.next
            if head.val < x:
                less_than_move.next = head
                less_than_move.next.next = None
                less_than_move = less_than_move.next
            else:
                greater_than_move.next = head
                greater_than_move.next.next = None
                greater_than_move = greater_than_move.next
            head = next_node
        less_than_move.next = greater_than.next
        return less_than.next
