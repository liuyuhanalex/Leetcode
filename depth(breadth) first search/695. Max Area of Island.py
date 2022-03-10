from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid)-1, len(grid[0]) - 1
        finish_set = set()
        max_len = 0
        for i in range(R+1):
            for j in range(C+1):
                if grid[i][j] == 1 and (i, j) not in finish_set:
                    queue = [(i, j)]
                    small_finish_set = {(i, j)}
                    while len(queue) > 0:
                        x, y = queue.pop()
                        if x-1>=0 and grid[x-1][y] == 1 and (x-1,y) not in small_finish_set:
                            queue.append((x-1, y))
                            small_finish_set.add((x-1, y))
                        if x+1<=R and grid[x+1][y] == 1 and (x+1, y) not in small_finish_set:
                            queue.append((x+1, y))
                            small_finish_set.add((x+1, y))
                        if y-1 >= 0 and grid[x][y-1] == 1 and (x, y-1) not in small_finish_set:
                            queue.append((x, y-1))
                            small_finish_set.add((x, y-1))
                        if y+1 <= C and grid[x][y+1] == 1 and (x, y+1) not in small_finish_set:
                            queue.append((x, y+1))
                            small_finish_set.add((x, y+1))
                    if len(small_finish_set) > max_len:
                        max_len = len(small_finish_set)
                    finish_set = finish_set.union(small_finish_set)
        return max_len


    def maxAreaOfIsland_ans(self, grid):
        seen = set()

        def area(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
                    and (r, c) not in seen and grid[r][c]):
                return 0
            seen.add((r, c))
            return (1 + area(r + 1, c) + area(r - 1, c) +
                    area(r, c - 1) + area(r, c + 1))

        return max(area(r, c)
                   for r in range(len(grid))
                   for c in range(len(grid[0])))


if __name__ == '__main__':
    Solution().maxAreaOfIsland(grid=
                               [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                                [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]])
