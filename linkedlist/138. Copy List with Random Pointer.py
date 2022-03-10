class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        new_head = Node(head.val)
        record, record_old = new_head, head
        res_dict = {}
        while head.next is not None:
            new_head.next = Node(head.next.val)
            res_dict[head] = new_head
            new_head, head = new_head.next, head.next
        res_dict[head] = new_head
        new_head = record
        while record_old is not None:
            new_head.random = res_dict.get(record_old.random)
            record_old, new_head = record_old.next, new_head.next
        return record

if __name__ == '__main__':
    Solution().copyRandomList()