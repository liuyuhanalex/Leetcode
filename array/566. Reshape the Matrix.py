from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        high = len(mat)
        length = len(mat[0])
        if high*length != r*c:
            return mat
        flatten_list = [mat[i][j] for i in range(len(mat)) for j in range(len(mat[0]))]
        new_mat = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                new_mat[i][j] = flatten_list.pop(0)
        return new_mat


if __name__ == '__main__':
    Solution().matrixReshape( mat = [[1,2],[3,4]], r = 1, c = 4)