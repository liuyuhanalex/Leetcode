from typing import List
from copy import copy


from copy import copy
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        hash_table = {}
        for i in edges:
            hash_table.setdefault(i[1], []).append(i[0])
        final = []
        for i in range(n):
            q = copy(hash_table.get(i, []))
            rec_set = set()
            while q:
                q_len = len(q)
                for _ in range(q_len):
                    num = q.pop(0)
                    if num not in rec_set:
                        rec_set.add(num)
                        q += copy(hash_table.get(num, []))
            final.append(copy(sorted(list(rec_set))))
        return final






if __name__ == '__main__':
    print(Solution().getAncestors(n = 8, edges = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]))