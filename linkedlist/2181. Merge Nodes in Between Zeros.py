from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = head
        last = head.next
        res = []
        while last.next is not None:
            if last.val == 0:
                first.val = sum(res)
                first.next = last
                first = last
                last = last.next
            else:
                res.append(last.val)
                last = last.next
        return head
