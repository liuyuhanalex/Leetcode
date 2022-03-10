from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        new_head = ListNode(-1, head)
        first, second = new_head, new_head.next
        flag = first.val
        while second.next is not None:
            if second.next.val != second.val and flag != second.val:
                first.next = second
                first = first.next
                second = second.next
            else:
                flag = second.val
                second = second.next
        if second.val != flag:
            first.next = second
        return new_head.next





