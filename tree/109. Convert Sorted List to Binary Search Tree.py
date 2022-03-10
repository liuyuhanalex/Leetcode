from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if head is None:
            return None
        if head.next is None:
            return TreeNode(head.val)
        slow, fast, last = head, head, head
        while fast.next and fast.next.next:
            last = slow
            slow = slow.next
            fast = fast.next.next
        fast = slow.next
        last.next = None
        root = TreeNode(slow.val)
        if head != slow:
            root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(fast)
        return root