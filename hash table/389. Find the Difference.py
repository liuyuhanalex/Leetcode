from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c_s = Counter(s)
        c_t = Counter(t)
        for k, v in c_t.items():
            if v != c_s.get(k):
                return k


if __name__ == '__main__':
    print(Solution().findTheDifference(s = "abcd", t = "abcde"))