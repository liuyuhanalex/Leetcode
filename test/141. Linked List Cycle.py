# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        m_map = set()
        while head.next is not None:
            head = head.next
            if head in m_map:
                return True
            m_map.add(head)
        return False



if __name__ == '__main__':
    Solution().hasCycle()