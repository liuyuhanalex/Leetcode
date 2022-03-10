from typing import List
from copy import copy

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0:
            return False
        side_length = sum(matchsticks) // 4
        if max(matchsticks) > side_length:
            return False
        result = [0, 0, 0, 0]
        final_result = []
        matchsticks = sorted(matchsticks, reverse=True)
        def backtracking(index):
            if len(final_result) > 0:
                return
            if index == len(matchsticks):
                if set(result) == {side_length}:
                    final_result.append(copy(result))
                    return
                return
            for i in range(4):
                if result[i] + matchsticks[index] <= side_length:
                    result[i] += matchsticks[index]
                    backtracking(index + 1)
                    result[i] -= matchsticks[index]
        backtracking(0)
        if len(final_result) > 0:
            return True
        return False




if __name__ == '__main__':
    print(Solution().makesquare(matchsticks= [1569462,2402351,9513693,2220521,7730020,7930469,1040519,5767807,876240,350944,4674663,4809943,8379742,3517287,8034755]))