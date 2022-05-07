from typing import List
from copy import copy
from collections import Counter

class Solution:
    # method1 counter
    def findAnagrams1(self, s: str, p: str) -> List[int]:
        p_hash = Counter(p)
        res = []
        for i in range(len(s)):
            counter = Counter(s[i:i+len(p)])
            if counter == p_hash:
                res.append(i)
        return res

    def findAnagrams2(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        pCounter = Counter(p)
        sCounter = Counter(s[:len(p) - 1])
        for i in range(len(p) - 1, len(s)):
            sCounter[s[i]] += 1  # include a new char in the window
            if sCounter == pCounter:  # This step is O(1), since there are at most 26 English letters
                res.append(i - len(p) + 1)  # append the starting index
            sCounter[s[i - len(p) + 1]] -= 1  # decrease the count of oldest char in the window
            if sCounter[s[i - len(p) + 1]] == 0:
                del sCounter[s[i - len(p) + 1]]  # remove the count if it is 0
        return res


if __name__ == '__main__':
    #Solution().findAnagrams(s="abab", p="ab")
    print(Solution().findAnagrams("cbaebabacd", "abc"))
