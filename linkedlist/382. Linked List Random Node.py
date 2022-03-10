from typing import Optional
import random

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.node_list = []
        while head is not None:
            self.node_list.append(head)
            head = head.next

    def getRandom(self) -> int:
        return random.choice(self.node_list)