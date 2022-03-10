from typing import List
from copy import copy


class Solution:
    def shortestPathBinaryMatrix2(self, grid: List[List[int]]) -> int:
        res = []
        path = [(0, 0)]
        if grid[0][0] != 0:
            return -1
        def backtracking(last_pos):
            if len(res) >0 and len(path) > min(res):
                return
            if last_pos == (len(grid[0]) -1, len(grid) - 1):
                res.append(len(path))
                return
            x, y = last_pos
            for pos1 in [(x+1, y), (x+1, y-1), (x+1, y+1), (x-1, y), (x-1, y+1), (x-1, y-1), (x, y+1), (x, y-1)]:
                x1, y1 = pos1
                if(x1, y1) not in path and 0 <= x1 < len(grid[0]) and 0<= y1 < len(grid) and grid[x1][y1] == 0:
                    path.append((x1, y1))
                    backtracking((x1, y1))
                    path.pop()
        backtracking((0, 0))
        if len(res) == 0:
            return -1
        return min(res)

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1
        q = [(0, 0)]
        w, h = len(grid[0]), len(grid)
        level = 1
        total_set =set()
        while q:
            level += 1
            q_len = len(q)
            for _ in range(q_len):
                (x, y) = q.pop(0)
                if (x, y) == (w-1, h-1):
                    return level - 1
                for i in [(x + 1, y), (x + 1, y - 1), (x + 1, y + 1), (x - 1, y), (x - 1, y + 1), (x - 1, y - 1),
                          (x, y + 1), (x, y - 1)]:
                    x1, y1 = i
                    if 0 <= x1 < len(grid[0]) and 0 <= y1 < len(grid) and grid[x1][y1] == 0:
                        if (x1, y1) not in q and (x1, y1) not in total_set:
                            if (x1, y1) == (w - 1, h - 1):
                                return level
                            total_set.add((x1, y1))
                            q.append((x1, y1))
        return -1






if __name__ == '__main__':
    print(Solution().shortestPathBinaryMatrix([[0]]))