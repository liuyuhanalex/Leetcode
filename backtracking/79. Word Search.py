from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        result = []
        path = []
        board_x = len(board)
        board_y = len(board[0])
        memory = []
        def backtracking(board, choices):
            if len(path) == len(word):
                result.append("".join(path))
                return True
            for i in choices:
                x, y = i
                if 0 <= x < board_x and 0 <= y < board_y and board[x][y] == word[len(path)]:
                    path.append(board[x][y])
                    memory.append((x, y))
                    if backtracking(board, list(set([(x, y+1), (x, y-1), (x-1, y), (x+1, y)]) - set(memory))):
                        break
                    path.pop()
                    memory.pop()
        original_list = [(i, j) for i in range(board_x) for j in range(board_y) if board[i][j]==word[0]]
        backtracking(board, original_list)
        if len(result) > 0:
            return True
        return False