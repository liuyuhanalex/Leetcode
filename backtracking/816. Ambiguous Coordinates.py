from typing import List
from copy import copy

class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        num_str = s[1:-1]
        result = []
        for i in range(1, len(num_str)):
            result.append((num_str[:i], num_str[i:]))
        for j in result:
            x, y = j
            if len(x) >= 2:
                pass


if __name__ == '__main__':
    Solution().ambiguousCoordinates(s="(123)")
