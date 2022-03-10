from typing import List
from copy import copy


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_num = [0] * numCourses
        hash_table = {}
        for i in prerequisites:
            in_num[i[1]] = in_num[i[1]] + 1
            hash_table.setdefault(i[0], []).append(i[1])
        q = [index for index, item in enumerate(in_num) if item == 0]
        res = []
        cnt  = 0
        while q:
            num = q.pop(0)
            cnt += 1
            res.append(num)
            for i in hash_table.get(num, []):
                in_num[i] = in_num[i] - 1
                if in_num[i] == 0:
                    q.append(i)
        res = reversed(res)
        if cnt == numCourses:
            return res
        else:
            return []





if __name__ == '__main__':
    Solution().findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]])