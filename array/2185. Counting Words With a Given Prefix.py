from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        cnt = 0
        for i in words:
            if i.startswith(pref):
                cnt += 1
        return cnt





if __name__ == '__main__':
    Solution().prefixCount(words = ["pay","attention","practice","attend"], pref = "at")