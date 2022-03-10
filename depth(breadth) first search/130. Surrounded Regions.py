from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        width, height = len(board[0]), len(board)
        init = []
        visited = set()
        for i in range(height):
            for j in range(width):
                if board[i][j] == 'O':
                    init.append((i, j))
        while init:
            length = len(init)
            for _ in range(length):
                x, y = init.pop(0)
                for item in [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]:
                    if item not in visited and 0 <= item[0] < width and y <= item[1] < height:
                        visited.add(item)
                        init.append(item)
        print(visited)





if __name__ == '__main__':
    Solution().solve(board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])