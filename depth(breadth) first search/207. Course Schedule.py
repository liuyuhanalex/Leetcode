from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hash_table = {}
        for i in prerequisites:
            hash_table.setdefault(i[0], []).append(i[1])
        total_visited = set()
        for i in range(numCourses):
            if len(total_visited) == numCourses:
                return True
            if hash_table.get(i) is None:
                pass
            else:
                if i in total_visited:
                    continue
                path = []
                res = []
                visited = set()
                def backtracking(num):
                    visited.add(num)
                    if len(path) > len(set(path)):
                        res.append(1)
                        return
                    if hash_table.get(num) is not None:
                        for z in hash_table.get(num):
                            if len(res) > 0:
                                return
                            if z not in total_visited:
                                path.append(z)
                                backtracking(z)
                                path.pop()
                backtracking(i)
                if len(res) > 0:
                    return False
                total_visited = total_visited.union(visited)
        return True



if __name__ == '__main__':
    print(Solution().canFinish(numCourses = 5, prerequisites =[[1,4],[2,4],[3,1],[3,2]]))