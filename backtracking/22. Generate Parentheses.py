from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path = []
        result = []
        def backtracking(n: int, left_num:int, right_num:int):
            if len(path) == 2*n:
                result.append(''.join(path))
                return
            for i in ["(", ")"]:
                if i == ')':
                    if right_num < left_num:
                        path.append(i)
                        backtracking(n, left_num, right_num + 1)
                        path.pop()
                else:
                    if left_num < n:
                        path.append(i)
                        backtracking(n, left_num+1, right_num)
                        path.pop()
        backtracking(n, 0, 0)
        return list(set(result))