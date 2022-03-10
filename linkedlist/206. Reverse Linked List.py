from typing import Optional
from typing import List
from linkedlist.base import create_linked_list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        last = None
        while head.next is not None:
            next_node = head.next
            head.next = last
            last = head
            head = next_node
        head.next = last
        return head



if __name__ == '__main__':
    test_case = create_linked_list([1, 2, 3, 4, 5])
    re_ls = Solution().reverseList(test_case)
    while re_ls.next is not None:
        print('re', re_ls.val)
        re_ls = re_ls.next
