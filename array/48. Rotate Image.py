from typing import List
from math import ceil


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if j <= i:
                    tmp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = tmp
                else:
                    break
        for i in range(len(matrix)):
            for j in range(int(len(matrix)/2)):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[i][len(matrix)-1-j]
                matrix[i][len(matrix)-1 - j] = tmp

if __name__ == '__main__':
    Solution().rotate([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]])
