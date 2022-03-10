from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        path = []
        r_max, r_min = m, 0
        c_max, c_min = n, 0
        while len(path) < m*n:
            for c in range(c_min, c_max):
                path.append(matrix[r_min][c])
            if len(path) == m*n:
                break
            for r in range(r_min+1, r_max):
                path.append(matrix[r][c_max-1])
            if len(path) == m*n:
                break
            for c in range(c_max-2, c_min, -1):
                path.append(matrix[r_max-1][c])
            if len(path) == m*n:
                break
            for r in range(r_max-1, r_min, -1):
                path.append(matrix[r][c_min])
            c_max, c_min = c_max - 1, c_min + 1
            r_max, r_min = r_max - 1, r_min + 1
        return path




if __name__ == '__main__':
    Solution().spiralOrder(matrix=[[3],[2]])
