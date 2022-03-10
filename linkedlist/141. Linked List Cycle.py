class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        add_dict = {}
        while head is not None:
            if add_dict.get(head) is not None:
                return True
            else:
                add_dict[head] = 1
            head = head.next
        return False


if __name__ == '__main__':
    pass