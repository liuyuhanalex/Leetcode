from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        height, width = len(grid), len(grid[0])
        init = []
        for i in range(height):
            for j in range(width):
                if grid[i][j] == '1':
                    init.append((i, j))
        visited = set()
        cnt = 0
        for i in init:
            if i not in visited:
                cnt += 1
                q = [i]
                while q:
                    length = len(q)
                    for _ in range(length):
                        x, y = q.pop(0)
                        for item in [(x-1, y), (x+1, y), (x, y+1), (x, y-1)]:
                            if 0<=item[0]<height and 0<=item[1]<width and grid[item[0]][item[1]] == '1' and item not in visited:
                                visited.add(item)
                                q.append(item)
        return cnt






if __name__ == '__main__':
    Solution().numIslands(grid = [["1","1","0","0","0"],
                                  ["1","1","0","0","0"],
                                  ["0","0","1","0","0"],
                                  ["0","0","0","1","1"]])
