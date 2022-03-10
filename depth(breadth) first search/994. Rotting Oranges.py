from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R = len(grid) - 1
        C = len(grid[0]) - 1
        queue = []
        orange = set({})
        for i in range(R+1):
            for j in range(C+1):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    orange.add((i, j))

        seen = set(queue)
        level = 0
        while queue:
            q_len = len(queue)
            for _ in range(q_len):
                x, y = queue.pop(0)
                for i, j in {(x-1 ,y), (x+1, y), (x, y-1), (x, y+1)}:
                    if 0 <= i <= R and 0 <= j <= C and grid[i][j]==1 and (i, j) not in seen:
                        queue.append((i, j))
                        seen.add((i, j))
            level += 1
        if orange.intersection(seen) != orange:
            return -1
        return level - 1






if __name__ == '__main__':
    print(Solution().orangesRotting(grid=[[2,1,1],[0,1,1],[1,0,1]]))