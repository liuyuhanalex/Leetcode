from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            row = [i for i in row if i != '.']
            if len(set(row)) != len(row):
                return False
        for i in range(len(board)):
            col = []
            for j in range(len(board)):
                col.append(board[j][i])
            col = [i for i in col if i != '.']
            if len(set(col)) != len(col):
                return False
        for i in [3, 6, 9]:
            for j in [3, 6, 9]:
                block = [board[wid][high] for wid in range(i-3, i) for high in range(j-3, j) if board[wid][high] != '.']
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
