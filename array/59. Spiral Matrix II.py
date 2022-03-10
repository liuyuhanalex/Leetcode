from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        r_max, r_min = n-1, 0
        c_max, c_min = n-1, 0
        path = list(range(1, n*n+1))
        while len(path) > 0:
            for c in range(c_min, c_max+1):
                matrix[r_min][c] = path.pop(0)
            r_min += 1
            for r in range(r_min, r_max+1):
                matrix[r][c_max] = path.pop(0)
            c_max -= 1
            for c in range(c_max, c_min-1, -1):
                matrix[r_max][c] = path.pop(0)
            r_max -= 1
            for r in range(r_max, r_min-1, -1):
                matrix[r][c_min] = path.pop(0)
            c_min += 1
        return matrix


if __name__ == '__main__':
    print(Solution().generateMatrix(n=3))
