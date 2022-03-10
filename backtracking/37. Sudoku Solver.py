from typing import List
from copy import deepcopy

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        init = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    board[i][j] = 0
                    init.append((i, j))
                else:
                    board[i][j] = int(board[i][j])
        result = []
        def backtracking(board, index):
            if index == len(init):
                result.append(deepcopy(board))
                return
            x1, y1 = init[index]
            row_num = set(board[x1])
            col_num = set()
            for i in range(9):
                col_num.add(board[i][y1])
            block = [j[(y1 // 3) * 3: (y1 // 3) * 3 + 3] for j in board[(x1 // 3) * 3: (x1 // 3) * 3 + 3]]
            block_num = set([j for i in block for j in i])
            remain_num = row_num.union(col_num.union(block_num))
            whole_num = set(range(1, 10))
            remain_num = whole_num - remain_num
            if len(remain_num) > 0:
                for i in remain_num:
                    board[x1][y1] = i
                    backtracking(board, index+1)
                    board[x1][y1] = 0
            else:
                return
        backtracking(board, 0)
        res_board = result[0]
        for i in range(9):
            for j in range(9):
                board[i][j] = str(res_board[i][j])


if __name__ == '__main__':
    Solution().solveSudoku(
        board=[["5", "3", ".", ".", "7", ".", ".", ".", "."],
               ["6", ".", ".", "1", "9", "5", ".", ".", "."],
               [".", "9", "8", ".", ".", ".", ".", "6", "."],
               ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
               ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
               ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
               [".", "6", ".", ".", ".", ".", "2", "8", "."],
               [".", ".", ".", "4", "1", "9", ".", ".", "5"],
               [".", ".", ".", ".", "8", ".", ".", "7", "9"]])
