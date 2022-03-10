from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        while head is not None:
            stack.append(head.val)
            head = head.next
        start, end = 0, len(stack) - 1
        while start < end:
            if stack[start] != stack[end]:
                return False
            start +=1
            end -=1
        return True
