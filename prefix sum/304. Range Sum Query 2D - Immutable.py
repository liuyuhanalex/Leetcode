from typing import List
from copy import copy

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.rec_matrix = copy(matrix)
        for i in range(1, len(matrix[0])):
            self.rec_matrix[0][i] = self.rec_matrix[0][i-1] + self.rec_matrix[0][i]
        for i in range(1, len(matrix)):
            self.rec_matrix[i][0] = self.rec_matrix[i-1][0] + self.rec_matrix[i][0]
        for i in range(1, len(matrix[0])):
            for j in range(1, len(matrix)):
                self.rec_matrix[i][j] = self.rec_matrix[i-1][j] + self.rec_matrix[i][j-1] + self.rec_matrix[i][j] - self.rec_matrix[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        final = 0
        if row1 - 1 >= 0:
            final -= self.rec_matrix[row1 - 1][col2]
        if col1 - 1 >= 0:
            final -= self.rec_matrix[row2][col1 - 1]
        if row1 - 1 >= 0 and col1 - 1 >= 0:
            final += self.rec_matrix[row1 - 1][col1 - 1]
        return self.rec_matrix[row2][col2] + final


if __name__ == '__main__':
    #nm = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
    nm = NumMatrix([[-4, -5]])