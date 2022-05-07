from typing import List

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        total_grid = [(i, j) for i in range(m) for j in range(n)]
        print(total_grid)


if __name__ == '__main__':
    Solution().countUnguarded(m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]])