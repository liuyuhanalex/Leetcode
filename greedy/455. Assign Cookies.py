from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        sorted_g = sorted(g)
        sorted_s = sorted(s)
        count = 0
        for c in sorted_g:
            min_c = 0
            while min_c < c:
                if len(sorted_s) == 0:
                    return count
                min_c = sorted_s.pop(0)
            count += 1
        return count


if __name__ == '__main__':
    Solution().findContentChildren([10, 9, 8, 7],
                                   [5, 6, 7, 8])
