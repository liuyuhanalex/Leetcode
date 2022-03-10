from typing import Optional, List
import math

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        rec_head = head
        cnt = 0
        while head is not None:
            cnt += 1
            head = head.next
        avg_number = cnt//k
        remain = cnt - (cnt//k)*k
        result = []
        while k > 0:
            k -= 1
            new_head = rec_head
            if new_head is None:
                result.append(None)
                continue
            result.append(new_head)
            if remain > 0:
                total_num = avg_number
                remain -= 1
            else:
                total_num = avg_number - 1
            for i in range(total_num):
                rec_head = rec_head.next
            old_rec = rec_head
            rec_head = rec_head.next
            old_rec.next = None
        return result
