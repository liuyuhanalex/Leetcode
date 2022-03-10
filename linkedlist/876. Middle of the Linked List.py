# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer1, pointer2 = head, head
        while pointer2.next and pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next.next
        return pointer1


if __name__ == '__main__':
    Solution().middleNode()