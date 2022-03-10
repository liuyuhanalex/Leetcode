from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        path = []
        def backtracking(remain_position):
            if len(path) == n:
                r = [['.' for _ in range(n)] for _ in range(n)]
                for j in path:
                    r[j[0]][j[1]] = 'Q'
                r = [''.join(j) for j in r]
                result.append(r)
                return
            for index, i in enumerate(remain_position):
                path.append(i)
                new_remain = [j for j in remain_position[index+1:] if j[0]!= i[0] and j[1]!=i[1] and j[0]-j[1]!=i[0]-i[1] and j[0]+j[1]!= i[0]+i[1]]
                backtracking(new_remain)
                path.pop()
        init = [[i, j] for i in range(n) for j in range(n)]
        backtracking(init)
        return result


if __name__ == '__main__':
    print(Solution().solveNQueens(n=5))
