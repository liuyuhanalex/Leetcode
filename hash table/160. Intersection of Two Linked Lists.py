from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hash_set = set()
        while headA is not None:
            hash_set.add(headA)
            headA = headA.next
        while headB is not None:
            if headB in hash_set:
                return headB
            else:
                headB = headB.next
        return None