class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        q = [root]
        while q:
            q_len = len(q)
            level_list = []
            for _ in range(q_len):
                node = q.pop()
                if node.left:
                    level_list.append(node.left)
                if node.right:
                    level_list.append(node.right)
            for i in range(len(level_list) - 1):
                level_list[i].next = level_list[i+1]
        return root