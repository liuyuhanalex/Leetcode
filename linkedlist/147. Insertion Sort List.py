from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode(head.val, None)
        rec = new_head
        while head is not None:
            while new_head.next is not None:
                if new_head.next.val < head.val:
                    new_head = new_head.next
                else:
                    tmp = new_head.next
                    new_head.next = ListNode(head.val, tmp)
                    break
            new_head = rec
            head = head.next
        return rec