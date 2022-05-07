from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 每条边都可以使用上，每个点都被连接，已经用过的点不能重复使用
        p_hash = {}
        for edge in edges:
            p_hash.setdefault(edge[0], []).append(edge[1])
            p_hash.setdefault(edge[1], []).append(edge[0])
        if set(p_hash.keys()) != set(range(n)):
            return False
        path = [0]
        all_node = set()
        result = []
        def backtracking(node, pre):
            if node not in all_node:
                all_node.add(node)
            else:
                result.append(1)
                return
            if p_hash.get(node) is None:
                return
            for i in p_hash.get(node):
                if i != pre:
                    path.append(i)
                    backtracking(i, node)
                    path.pop()
        backtracking(0, None)
        if len(result) > 0 or all_node != set(range(n)):
            return False
        return True







if __name__ == '__main__':
    #print(Solution().validTree(n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]))
    print(Solution().validTree(4, [[0,1],[2,3]]))
