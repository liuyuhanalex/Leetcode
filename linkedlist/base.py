from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(nums: List[int]) -> ListNode:
    head = ListNode(nums[0], None)
    record_head = head
    for i in nums[1:]:
        next_node = ListNode(i, None)
        head.next = next_node
        head = head.next
    return record_head