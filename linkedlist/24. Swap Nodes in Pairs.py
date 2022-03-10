# Definition for singly-linked list.
from typing import Optional
from linkedlist.base import create_linked_list

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first_node = ListNode(0, head)
        last = first_node
        while head.next is not None:
            next_node = head.next
            last.next = next_node
            next_head = next_node.next
            last.next = next_node
            next_node.next = head
            last = head
            head = next_head
            if head is None:
                last.next = None
                break
        if next_head is not None:
            last.next = next_head
        return first_node.next



if __name__ == '__main__':
    nums = create_linked_list([1, 2, 3])
    res = Solution().swapPairs(nums)
    while res.next is not None:
        print(res.val)
        res = res.next