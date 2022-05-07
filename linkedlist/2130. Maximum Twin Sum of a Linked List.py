from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack = []
        while head is not None:
            stack.append(head.val)
            head = head.next
        max_num = 0
        while stack:
            total = stack.pop(0) + stack.pop()
            if total > max_num:
                max_num = total
        return max_num