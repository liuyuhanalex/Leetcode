from typing import List
from copy import copy

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        path = [0]
        def backtracking(index):
            if path[-1] == len(graph)-1:
                result.append(copy(path))
                return
            for i in graph[index]:
                path.append(i)
                backtracking(i)
                path.pop()
        backtracking(0)
        return result


if __name__ == '__main__':
    print(Solution().allPathsSourceTarget(graph=[[2], [], [1]]))