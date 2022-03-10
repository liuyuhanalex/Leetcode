from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        queue = []
        while head.next is not None:
            queue.append(head)
            head = head.next
        cur = 0
        new_head = ListNode(-1, None)
        rec = new_head
        while len(queue) > 0:
            if cur == 0:
                node = queue.pop(0)
                cur = -1
            else:
                node = queue.pop(-1)
                cur = 0
            new_head.next = node
            new_head = new_head.next
        return rec.next