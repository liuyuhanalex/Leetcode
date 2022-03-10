from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = [board[i][j] for j in range(9) if board[i][j] != '.']
            col = [board[j][i] for j in range(9) if board[j][i] != '.']
            if len(set(row)) != len(row) or len(set(col)) != len(col):
                return False
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                block = [board[x][y] for x in range(i, i+3) for y in range(j, j+3) if board[x][y] != '.']
                if len(set(block)) != len(block):
                    return False
        return True


if __name__ == '__main__':
    print(Solution().isValidSudoku(board=
                             [["5", "3", ".", ".", "7", ".", ".", ".", "."]
                                 , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                                 , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                                 , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                                 , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                                 , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                                 , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                                 , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                                 , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
