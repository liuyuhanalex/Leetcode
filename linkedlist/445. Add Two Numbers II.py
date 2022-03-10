from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1, stack2 = [], []
        while l1 is not None:
            stack1.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            stack1.append(l2.val)
            l2 = l2.next
        res = []
        digit = 0
        while stack1 or stack2:
            total = 0
            if stack1:
                total += stack1.pop(0)
            if stack2:
                total += stack2.pop(0)
            if digit:
                total += digit
            digit = total//10
            res.append(total)
        print(res)

