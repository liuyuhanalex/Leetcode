from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        index_list = []
        res_list = []
        index = 0
        while head is not None:
            index_list.append(head.val)
            res_list.append(0)
            if not stack or head.val <= index_list[stack[-1]]:
                stack.append(index)
            else:
                while stack and head.val > index_list[stack[-1]]:
                    p_index = stack.pop()
                    res_list[p_index] = head.val
                stack.append(index)
            head = head.next
            index += 1
        return res_list




