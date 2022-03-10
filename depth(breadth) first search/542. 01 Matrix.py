from typing import List
import numpy as np


class Solution:
    def updateMatrix_old(self, mat: List[List[int]]) -> List[List[int]]:
        R = len(mat) - 1
        C = len(mat[0]) - 1
        new_mat = np.zeros_like(mat)
        def search(r, c, level):
            queue = [(r, c)]
            while queue:
                q_len = len(queue)
                for _ in range(q_len):
                    x, y = queue.pop(0)
                    if mat[x][y] == 0:
                        return level
                    if x+1<=R: queue.append((x+1, y))
                    if x-1>=0: queue.append((x-1, y))
                    if y+1<=C: queue.append((x, y+1))
                    if y-1>=0: queue.append((x, y-1))
                level += 1

        for i in range(R+1):
            for j in range(C+1):
                if mat[i][j] == 1:
                    new_mat[i][j] = search(i, j, 0)
        return new_mat

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        R = len(mat) - 1
        C = len(mat[0]) - 1
        queue = []
        for i in range(R+1):
            for j in range(C+1):
                if mat[i][j] == 0:
                    queue.append((i, j))
        level = 1
        new_mat = np.zeros_like(mat)
        r_set = set(queue)
        while queue:
            q_len = len(queue)
            for _ in range(q_len):
                x, y = queue.pop(0)
                if x-1>=0 and new_mat[x-1][y] == 0 and (x-1, y) not in r_set:
                    new_mat[x-1][y] = level
                    r_set.add((x-1, y))
                    queue.append((x-1, y))
                if x+1<=R and new_mat[x+1][y] == 0 and (x+1, y) not in r_set:
                    new_mat[x+1][y] = level
                    r_set.add((x+1, y))
                    queue.append((x +1, y))
                if y-1>=0 and new_mat[x][y-1] == 0 and (x, y-1) not in r_set:
                    new_mat[x][y-1] = level
                    r_set.add((x, y-1))
                    queue.append((x , y-1))
                if y+1<=C and new_mat[x][y+1] == 0 and (x, y+1) not in r_set:
                    new_mat[x][y+1] = level
                    r_set.add((x, y+1))
                    queue.append((x , y+1))
            level += 1
        return new_mat





if __name__ == '__main__':
    Solution().updateMatrix(mat = [[0,0,0],[0,1,0],[1,1,1]])






