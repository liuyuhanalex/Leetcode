from collections import Counter
from copy import copy


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        if s == t:
            return s
        c_counter = Counter(t)
        min_length = len(s)
        right, left = 0, 0
        final = ''
        while right < len(s):
            if c_counter.get(s[right]) is not None:
                c_counter[s[right]] = c_counter[s[right]] - 1
            right += 1
            while len([i for i in c_counter.values() if i <= 0]) == len(c_counter.keys()):
                print(right, left)
                if right - left <= min_length:
                    min_length = right - left
                    final = s[left: right]
                if c_counter.get(s[left]) is not None:
                    c_counter[s[left]] = c_counter[s[left]] + 1
                left += 1
        return final


if __name__ == '__main__':
    print(Solution().minWindow(s = "abc", t = "ac"))
