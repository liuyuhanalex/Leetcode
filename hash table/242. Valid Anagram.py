from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = Counter(s)
        t_counter = Counter(t)
        if s_counter == t_counter:
            return True
        return False


if __name__ == '__main__':
    print(Solution().isAnagram(s="anagram", t="nagaram"))
