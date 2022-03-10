"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        queue = [root]
        while queue:
            q_len = len(queue)
            small_list = []
            for _ in range(q_len):
                node = queue.pop(0)
                if node is not None:
                    small_list.append(node)
                    if node.left is not None:
                        queue.append(node.left)
                    if node.right is not None:
                        queue.append(node.right)
            for index, item in enumerate(small_list):
                if index < len(small_list) -1:
                    item.next = small_list[index+1]
        return root