from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_set = set()
        h = len(matrix)
        w = len(matrix[0])
        for i in range(h):
            flag = 0
            for j in range(w):
                if matrix[i][j] == 0:
                    zero_set.add(j)
                    flag = 1
            if flag:
                matrix[i] = [0 for _ in range(w)]
        for j in zero_set:
            for i in range(h):
                matrix[i][j] = 0


if __name__ == '__main__':
    Solution().setZeroes([[1, 1, 1],
                          [1, 0, 1],
                          [1, 1, 1]])
