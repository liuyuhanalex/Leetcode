class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        add_dict = {}
        while head is not None:
            if add_dict.get(head) is not None:
                return head
            else:
                add_dict[head] = 1
            head = head.next
        return None
