from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pointer1 = ListNode(0, head)
        record = pointer1
        pointer2 = pointer1
        for i in range(n+1):
            pointer2 = pointer2.next
        while pointer2 is not None:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        if pointer1.next.next is not None:
            pointer1.next = pointer1.next.next
        else:
            pointer1.next = None
        return record.next




if __name__ == '__main__':
    Solution().removeNthFromEnd()