class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        hash_table = {}
        record = node
        queue = [node]
        while queue:
            n = queue.pop(0)
            if hash_table.get(n) is None:
                new_node = Node(n.val, [])
                hash_table[n] = new_node
                for i in n.neighbors:
                    if hash_table.get(i) is None:
                        queue.append(i)
        for old, new in hash_table.items():
            new.neighbors = [hash_table.get(i) for i in old.neighbors]
        return hash_table.get(record)