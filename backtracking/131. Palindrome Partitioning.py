from typing import List
from copy import copy


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []
        def backtracking(index):
            if ''.join(path) == s:
                result.append(copy(path))
            for i in range(index, len(s)+1):
                if len(s[index:i]) > 0 and s[index: i] == s[index:i][::-1]:
                    path.append(s[index:i])
                    backtracking(i)
                    path.pop()
        backtracking(0)
        return result


if __name__ == '__main__':
    Solution().partition(s="aab")
